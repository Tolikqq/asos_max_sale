from flask import Flask, render_template, request
from parse import parse_asos

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
        lists = [{'name': 'Зеленая курткаб.', 'url': 'https://www.asos.com/ru/elle', 'price': 4790.0, 'price_sale': 3190.0, 'sale': -33}]
    return render_template('index.html', lists=lists)


if __name__ == "__main__":
    app.run()
