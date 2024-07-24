from flask import Flask, render_template

app = Flask(__name__)

pizzas = [['Маргарита', 'Томатный соус, моцарелла, свежие помидоры, базилик, оливковое масло.', '120 грн'],
          ['Пепперони', 'Томатный соус, моцарелла, пепперони.', '180 гривен'],
          ['Гавайская','Томатный соус, моцарелла, ветчина, ананас.','200 гривен']]

@app.route('/pizza/')
def pizza():
    return render_template('index2.html',
                           name1=pizzas[0][0], made1=pizzas[0][1], price1=pizzas[0][2],
                           name2=pizzas[1][0], made2=pizzas[1][1], price2=pizzas[1][2],
                           name3=pizzas[2][0], made3=pizzas[2][1], price3=pizzas[2][2])


app.run()