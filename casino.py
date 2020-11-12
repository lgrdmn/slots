from flask import Flask, render_template, request, url_for
import main

app = Flask(__name__)

INDEX_PATH = "index.html"


@app.route('/')
def index():
    info = main.get_info()
    credit = info["credit"]
    return render_template(INDEX_PATH, credit=credit)


@app.route('/send')
def web_send():
    if request.args.get('submit_button') == "ROLL":
        first_value, second_value, third_value = main.values_generator()
        first_url, second_url, third_url = main.value_to_url(first_value, second_value, third_value)

        info = main.get_info()  # получаем информацию из файла
        credit, bet = int(info["credit"]), int(request.args.get('bet'))  # определяем переменные Баланса и Ставки
        bonus = main.bonus(first_value, second_value, third_value)  # расчитываем бонус
        win = main.game(bet, bonus)  # определяем размер выигрыша
        info["credit"] = str((credit - bet) + win)  # расчитываем новое значение Баланса
        info["bet"] = str(bet)
        main.write_info(info)  # записываем информацию в файл

        image_1 = url_for('static', filename=first_url)
        image_2 = url_for('static', filename=second_url)
        image_3 = url_for('static', filename=third_url)
        return render_template(INDEX_PATH, image_1=image_1, image_2=image_2, image_3=image_3,
                               credit=info["credit"], bet=bet, win=win)


if __name__ == '__main__':
    app.run()
