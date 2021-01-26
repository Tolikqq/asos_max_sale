from flask import Flask, render_template, request
from parse import parse_asos
# from flask_env import MetaFlaskEnv
import requests

#
#
# class Configuration(metaclass=MetaFlaskEnv):
#     DEBUG = False
#     PORT = 5000
#     BOT_TOKEN = ''
#     SENTRY_DSN = None
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('example.html')

@app.route("/shops", methods=['GET', 'POST'])
def shops():
    lists = []
    if request.method == 'POST':
        url = request.form['url']
        lists = parse_asos(url)
    return render_template('index.html', lists=lists)


# if __name__ == "__main__":
#     app.run(debug=True, port=33507)
