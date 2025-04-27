from flask import Flask, render_template, redirect
from data import db_session
from forms.user import RegisterForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    app.run()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return redirect('/base')
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/base')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/base', methods=['GET', 'POST'])
def index():
    return render_template('buttons1.html')


@app.route('/history')
def history():
    return render_template('buttons_history.html')

@app.route('/sight')
def sight():
    return render_template('buttons_sightseeing.html')



if __name__ == '__main__':
    main()