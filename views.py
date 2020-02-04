from app import app
from flask import jsonify, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm
from models import UserModel
from resources import UserRegistration, UserLogin

@app.route('/')
def index():
    return render_template('base.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        check = UserRegistration.post('', form.data)
        '''email = form.email.data
        name = form.fname.data
        phone = form.phone.data
        state = form.state.data
        city = form.city.data
        country = form.country.data
        username = form.username.data
        password = form.password.data
        add = UserModel(fname=name,
                        email=email,
                        username=username,
                        password=password,
                        phone=phone,
                        city=city,
                        country=country,
                        state=state)
        add.save_to_db()'''
        flash(check['message'])
        return redirect(url_for('index'))
    else:
        flash('User did not register')

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        check = UserLogin.post('', form.data)
        flash(check['message'])
        return redirect(url_for('index'))
    else:
        flash('Data entered is not valid')

    return render_template('login.html', title='Register', form=form)