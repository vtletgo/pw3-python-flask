import time
import requests
from flask import Blueprint, render_template, request, abort, url_for, redirect
from models.launch import Launch

spacex_bp = Blueprint("spacex", __name__)

API_BASE = "https://api.spacexdata.com/v4"

# cache simples em memória para reduzir chamadas repetidas
_cache = {"launches": {"value": None, "ts": 0}}
TTL = 60  # segundos

def _get_launches():
    now = time.time()
    if _cache["launches"]["value"] is not None and now - _cache["launches"]["ts"] < TTL:
        return _cache["launches"]["value"]
    url = f"{API_BASE}/launches"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    # ordenar mais recentes primeiro
    data.sort(key=lambda l: l.get("date_utc",""), reverse=True)
    _cache["launches"]["value"] = data
    _cache["launches"]["ts"] = now
    return data

def _get_rocket_name(rocket_id: str) -> str:
    if not rocket_id:
        return ""
    r = requests.get(f"{API_BASE}/rockets/{rocket_id}", timeout=30)
    if r.status_code != 200: return rocket_id
    return r.json().get("name", rocket_id)

def _get_launchpad_name(lp_id: str) -> str:
    if not lp_id:
        return ""
    r = requests.get(f"{API_BASE}/launchpads/{lp_id}", timeout=30)
    if r.status_code != 200: return lp_id
    return r.json().get("name", lp_id)

@spacex_bp.route("/")
def index():
    q = (request.args.get("q") or "").strip().lower()
    year = (request.args.get("year") or "").strip()
    launches_raw = _get_launches()

    launches = []
    for l in launches_raw:
        li = Launch.from_api(l)
        if q and q not in li.name.lower():
            continue
        if year:
            try:
                if li.date.year != int(year):
                    continue
            except Exception:
                pass
        launches.append(li)

    # anos para o filtro
    years = sorted({l.date.year for l in (Launch.from_api(x) for x in launches_raw)}, reverse=True)
    return render_template("index.html", launches=launches, years=years, selected_year=year, q=q)

@spacex_bp.route("/launch/<launch_id>")
def details(launch_id):
    launches_raw = _get_launches()
    match = next((l for l in launches_raw if l.get("id")==launch_id), None)
    if not match:
        abort(404)
    li = Launch.from_api(match)
    # enriquecer com nomes
    li.rocket_name = _get_rocket_name(li.rocket_id) if li.rocket_id else ""
    li.launchpad_name = _get_launchpad_name(li.launchpad_id) if li.launchpad_id else ""
    return render_template("details.html", launch=li)
