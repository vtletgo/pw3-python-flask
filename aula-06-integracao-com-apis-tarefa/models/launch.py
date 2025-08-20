from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Launch:
    id: str
    name: str
    date: datetime
    patch_small: str = ""
    patch_large: str = ""
    details: str = ""
    rocket_id: str = ""
    rocket_name: str = ""
    launchpad_id: str = ""
    launchpad_name: str = ""
    webcast: str = ""
    article: str = ""
    wikipedia: str = ""

    @staticmethod
    def from_api(data: dict) -> "Launch":
        date_str = data.get("date_utc")
        dt = datetime.fromisoformat(date_str.replace("Z","+00:00")) if date_str else datetime.utcnow()
        links = data.get("links", {})
        patch = links.get("patch", {}) or {}
        return Launch(
            id=data.get("id",""),
            name=data.get("name",""),
            date=dt,
            patch_small=patch.get("small","") or "",
            patch_large=patch.get("large","") or "",
            details=data.get("details","") or "",
            rocket_id=data.get("rocket","") or "",
            launchpad_id=data.get("launchpad","") or "",
            webcast=links.get("webcast","") or "",
            article=links.get("article","") or "",
            wikipedia=links.get("wikipedia","") or "",
        )
