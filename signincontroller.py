from flask import render_template ,request ,flash,session , url_for ,redirect
from class_web.config import app,db
from class_web.model import *

@app.route('/login', methods =['GET','POST'])
def login():
    if request.form==['POST']:
        username = request.get('email')
        print(username)
        password = request.get('password')
        print(password)
        if not username :
            flash('username is empty',category='error')
            return render_template('login.html')

        if password == None:
            flash('password is empty',category='error')
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()
        if user:
            if user.pwd == password :
                flash('login succusfully',category='succuss')
                session['user_id'] = user.uid
                return render_template('user.html',user = user)
            else:
                flash('password is incorrect', category='error')
                return render_template('login.html')

    return render_template('login.html')

