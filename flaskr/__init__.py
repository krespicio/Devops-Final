import os

from flask import Flask, render_template, request
from .Battleship import Battleship
import random


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # the main game
    @app.route('/')
    def home():
        global game
        game = Battleship()
        return render_template('main.html', grid=game.grid)

    @app.route('/calculate', methods = ["POST"])
    def calculate():
        global game       
        data = request.form

        X = data['X']
        Y = data['Y']
        if game.validateInput(X,Y):
            won = game.checkResult(int(X), int(Y))
            if won:
                print("we have a winner")
                return render_template('winner.html')

        return render_template('main.html', grid=game.grid) 

    return app