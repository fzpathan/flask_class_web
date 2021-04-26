from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.template_folder = 'templates'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mir@5689@localhost/clapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
db = SQLAlchemy(app)
app.secret_key = 'super secret key'


# def create_table():
#     db.create_all()
#     print('Table Created')
#
# create_table()