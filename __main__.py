from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    app.run()

@app.route('/')
@app.route('/index')
def index():
    return render_template('buttons1.html')


@app.route('/history')
def history():
    return render_template('buttons_history.html')



if __name__ == '__main__':
    main()