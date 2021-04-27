from flask import render_template ,request ,flash,session
from flask_class_web.config import app,db
from flask_class_web.model import *
from flask_class_web.pwd_check import password_check ,mail_otp

import random

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        print(formdata)
        temp_user_info=UserInfo(firstname = formdata.get('firstname'),
                    lastname = formdata.get('lastname'),
                    dob = formdata.get('dob'),
                    mob = formdata.get('mob'),
                    email = formdata.get('email'),
                    pwd = formdata.get('password1'),
                    cnfpwd = formdata.get('password2'),
                    qual = formdata.get('qual'),
                    cour=formdata.get('cour'))
        db.session.add(temp_user_info)
        db.session.commit()
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(username='email').first()
        if user:
            msg = 'Email ID already exist'
            flash('Email ID already exist')
        elif len(email) < 4 :
            msg = 'Email id should be correct'
            flash('Email id should be correct')
        elif len(first_name) < 2:
            msg = 'Length of first name should be more than 2'
            flash('Length of first name should be more than 2')
        elif password1 != password2:
            msg  ='password doesnt match'
            flash('password doesnt match')
        elif password_check(password1):
            msg = password_check(password1)
            if msg == True:
                msg = 'Email authorization required'
                flash('Email authorization required')
                status = Status(status = 2)

                db.session.add(status)
                db.session.commit()
                temp_user = User(username = email, pwd = password1 ,usid = temp_user_info.userid)
                db.session.add(temp_user)
                db.session.commit()
                # otp = mail_otp(email)
                otp = random.randint(100000, 999999)
                session['response'] = str(otp)

                return render_template('email_auth.html' , msg =msg , user = temp_user ,status = status)

    return render_template('signup.html', msg = msg)

@app.route('/email_auth' , methods = ['GET', 'POST'])
def email_check():
    if request.method == 'POST':
        OTP = request.form.get('OTP')
        print(OTP)
        if 'response' in session:
            # flash('account created succusfully')
            s = session['response']
            session.pop('response',None)
            print(s)
            if s == OTP:
                print(s)
                flash('account created succusfully')

                return render_template('login.html')
            else:

                flash('incorrect OTP')
                return render_template('email_auth.html')
            # stid = Status.query.filter_by(user.request.get('stid')).first()
            # if Status.sid == stid:
            #     Status.status = 1
            #     db.session.commit()
    return render_template('email_auth.html')

@app.route('/login', methods =['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        if not username:
            flash('username is empty',category='error')
            msg = 'username is empty'
            return render_template('login.html',msg = msg)

        if not password:

            flash('password is empty',category='error')
            msg = 'password is empty'
            return render_template('login.html', msg = msg)

        user = User.query.filter_by(username=username).first()
        if user:
            if user.pwd == password :
                flash('login succusfully',category='succuss')
                session['user_id'] = user.uid
                return render_template('user.html',user = user)
            else:
                flash('password is incorrect', category='error')
                msg = 'password is incorrect'
                return render_template('login.html',msg = msg )

    return render_template('login.html')

if __name__ =="__main__":
    db.create_all()
    app.run(debug=True)