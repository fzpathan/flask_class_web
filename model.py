from class_web.config import db

class AdminUser(db.Model):
    a_id = db.Column('aid',db.Integer(),primary_key=True)
    username = db.Column('ausername',db.Integer(),unique=True)
    password = db.Column('apassword',db.String(30))
    cpassword = db.Column('acpassword', db.String(30))

class UserInfo(db.Model):
    userid = db.Column('userid', db.Integer(), primary_key=True)
    firstname = db.Column('firstname', db.String(30))
    lastname = db.Column('lastname', db.String(30))
    dob = db.Column('dob', db.String(50))
    mob = db.Column('mob', db.String(50))
    email = db.Column('email', db.String(50), unique = True)
    pwd = db.Column('pwd', db.String(30))
    cnfpwd = db.Column('cpwd', db.String(30))
    qual = db.Column('qual', db.String(30))
    cour = db.Column('cour', db.String(60))
    # usid = db.Column('us_id', db.ForeignKey('user.uid'), unique=True, nullable=False)

class User(db.Model):
    uid = db.Column('uid', db.Integer(), primary_key=True)
    username = db.Column('u_name', db.String(30), unique = True)
    pwd = db.Column('u_pwd', db.String(30))
    usid = db.Column('us_id', db.ForeignKey('user_info.userid'), unique=True, nullable=False)
    # usid = db.Column('us_id', db.ForeignKey('userinfo.id'), unique=True, nullable=False)
    # stid = db.Column('status_id', db.ForeignKey('status.sid'), unique=True, nullable=False)

class Status(db.Model):
    sid = db.Column('sid', db.Integer(), primary_key=True)
    status = db.Column('stat', db.String(60),default = 'PENDING')

class Courses(db.Model):
    cid = db.Column('cid', db.Integer(), primary_key=True)
    course_name = db.Column('cnm', db.String(30))

if __name__ =="__main__":
    db.create_all()
    # status = Status(status = 2)
    # db.session.add(status)
    # db.session.commit()