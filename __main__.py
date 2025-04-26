from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    return render_template('buttons1.html', title='Домашняя страница',)


@app.route('/history')
def history():
    pass

if __name__ == '__main__':
    app.run()