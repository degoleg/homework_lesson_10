from flask import Flask
from utils import get_all, get_by_pk

app = Flask(__name__)

@app.route("/")
def index():
    """
    Представление для роута /  (главная страница)
    выводит список с тегом <pre> - преформатирования
    :return:
    """
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f'<pre>{result}</pre>'


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    """
       Представление для роута candidates/<x>
       выводит данные про кондидата:
       картинка
       список
       :param pk:
       :return:
    """
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден'

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f"""
        <img src="{candidate['picture']}">
        <pre>{result}</pre>
    """


if __name__ == '__main__':
    app.run(debug=True)
