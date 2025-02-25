from flask import render_template, request

jogadores = ['Midna', 'Vt', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']


def init_app(app):
    # Criando a primeira rota do site

    @app.route('/')
    # Criando função do python
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Dicionário em Python (Objeto)
        game = {
            'titulo': 'CS-GO',
            'ano': 2012,
            'categoria': 'FPS Online'
        }

        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'Jogador' existe
            if request.form.get('jogador'):
                # Adicionando um novo jogador ao dicionário
                jogadores.append(request.form.get('jogador'))

        jogos = ['GTA V', 'Valorant', 'Elden Ring',
                 'Sekiro', 'Free Fire', 'Mad Max', 'Dying Light']
        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
