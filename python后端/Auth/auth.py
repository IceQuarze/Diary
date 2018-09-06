import sqlite3
import uuid

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

def hasUserName(userName):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select * from user where name="%s"'
                %(userName))
    if len(cur.fetchall()) == 0:
        return False
    else:
        return True

def hasUserEmail(userEmail):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select * from user where email="%s"'
                %(userEmail))
    if len(cur.fetchall()) == 0:
        return False
    else:
        return True

def hasToken(token):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select userId from user where token="%s"'
                %(token))
    res=cur.fetchone()
    if len(res) == 0:
        return {'status':False}
    else:
        return {'status':True,'userId':res['userId']}

def addUser(userName,userEmail,userPwd):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    userId=str(uuid.uuid4())
    cur.execute(r'insert into user(name,email,passwd,head_image,userId)values("%s","%s","%s","%s","%s")'
                %(userName,userEmail,userPwd,'default.jpg',userId))
    db.commit()

def userLogin(userEmail,userPwd):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select * from user where email="%s" and passwd="%s"'
                %(userEmail,userPwd))
    if len(cur.fetchall())==1:
        token=str(uuid.uuid4())
        cur.execute(r'update user set token="%s" where email="%s"'
                    %(token,userEmail))
        db.commit()
        cur.execute(r'select name,userId from user where token="%s"'
                    %(token))
        res=cur.fetchone()
        userName,userId=[res['name'],res['userId']]
        return [token,userName,userId]
    else:
        return ""
def udp_user_head_image(token,file_name):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'update user set head_image="%s" where token="%s"'
                %(file_name,token))
    db.commit()

def get_user_id(token):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select userId from user where token="%s"'
                % (token))
    userId=cur.fetchone()['userId']
    return userId

def get_user_info(userId):
    db = sqlite3.connect(r'user.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(r'select name,head_image from user where userId="%s"'
                %(userId))
    res=cur.fetchone()
    # name,head_image=res
    return {'userName':res['name'],'headImageURL':res['head_image']}