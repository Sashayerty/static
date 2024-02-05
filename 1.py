from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return f'''Миссия Колонизация Марса'''


@app.route('/index')
def index():
    return f'''И на Марсе будут яблони цвести!'''


@app.route('/promotion')
def promotion():
    return f'''Человечество вырастает из детства.</br>Человечеству мала одна планета.</br>
    Мы сделаем обитаемыми безжизненные пока планеты.
    </br>И начнем с Марса!</br>Присоединяйся!'''


@app.route('/image_mars')
def text_img():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion_image')
def promo_img():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась"></br>
                    Человечество вырастает из детства.</br>Человечеству мала одна планета.</br>
    Мы сделаем обитаемыми безжизненные пока планеты.
    </br>И начнем с Марса!</br>Присоединяйся!
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
