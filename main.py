from flask import Flask, render_template

app = Flask(__name__)

pizzas = [{'name': 'Маргарита',
           'made': 'Томатный соус, моцарелла, свежие помидоры, базилик, оливковое масло.',
           'price': '120 грн'},

          {'name': 'Пепперони',
           'made': 'Томатный соус, моцарелла, пепперони.',
           'price': '220 грн'},

          {'name': 'Гавайская',
           'made': 'Томатный соус, моцарелла, ветчина, ананас.',
           'price': '200 грн'}]


@app.route('/pizza/')
def pizza():
    return render_template('index2.html', pizzas=pizzas)


app.run(debug=True)
