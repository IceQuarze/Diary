from flask import Flask,request,make_response,jsonify,Response
from Auth import auth
import os
import json
import ReqMaker
import uuid

os.chdir(r'/var/Diary')
app = Flask(__name__)
SERVE_URL=r'http://39.108.217.186:5000'

def cor_wrap(r):
    response=make_response(r)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/register',methods=['POST'])
def register():
    userName=request.form.get('userName')
    userEmail = request.form.get('userEmail')
    userPwd = request.form.get('userPwd')
    if auth.hasUserEmail(userEmail):
        state=False
    else:
        state=True
        auth.addUser(userName,userEmail,userPwd)
    return cor_wrap(jsonify({'status':state}))

@app.route('/login',methods=['POST'])
def login():
    userEmail = request.form.get('userEmail')
    userPwd = request.form.get('userPwd')
    res=auth.userLogin(userEmail,userPwd)
    if res!="":
        token, userName, userId=res
        return cor_wrap(jsonify({'status':True,'token':token,'userName':userName,'userId':userId}))
    else:
        return cor_wrap(jsonify({'status':False}))

@app.route('/verify_token',methods=['POST'])
def verify_token():
#    print(request.data)
#    data=json.loads(request.data)
#    token=data['token']
    token=request.form.get('token')
    res=auth.hasToken(token)
    if res['status']==True:
        return cor_wrap(jsonify({'status':True,'userId':res['userId']}))
    else:
        return cor_wrap(jsonify({'status':False}))

@app.route('/upload_head_image',methods=['POST'])
def upload_head_image():
    token = request.form.get('token')
    res=ReqMaker.post(SERVE_URL+r'/verify_token',{'token':token})
    if res['status']==True:
        file=request.files['file']
        rd_name=str(uuid.uuid4())
        _,ext=os.path.splitext(file.filename)
        file_path=os.path.join(r'image',rd_name+ext)
        file.save(file_path)
        auth.udp_user_head_image(token,rd_name+ext)
        return cor_wrap(jsonify({'status':True}))
    else:
        return cor_wrap(jsonify({'status': False}))

# @app.route('/get_user_id',methods=['POST'])
# def get_user_id():
#     token = request.form.get('token')
#     return cor_wrap(jsonify({'status':True,'userId':auth.get_user_id(token)}))

@app.route('/get_user_info_js',methods=['POST'])
def get_user_info_js():
    userId = request.form.get('userId')
    # print('##'+str(request.data))
    # data = json.loads(request.data)
    # userId=data['userId']
    # tk_res = ReqMaker.post(SERVE_URL + r'/verify_token', {'userId': userId})
    # if tk_res['status'] == True:
    res=auth.get_user_info(userId)
    print(res)
    return cor_wrap(jsonify({'status':True,'userName':res['userName'],
                                 'headImageURL':SERVE_URL+r'/static/image/'+res['headImageURL'],
                                 'userId':userId}))


@app.route('/get_user_info',methods=['POST'])
def get_user_info():
    userId = request.form.get('userId')
    # print('##'+str(request.data))
    # data = json.loads(request.data)
    # userId=data['userId']
    # tk_res = ReqMaker.post(SERVE_URL + r'/verify_token', {'userId': userId})
    # if tk_res['status'] == True:
    res=auth.get_user_info(userId)
    print(res)
    return cor_wrap(jsonify({'status':True,'userName':res['userName'],
                                 'headImageURL':SERVE_URL+r'/static/image/'+res['headImageURL'],
                                 'userId':userId}))
    # else:
    #     return cor_wrap(jsonify({'status': False}))

@app.route('/postErr',methods=['POST'])
def getErr():
    data=request.form.get('data')
    f=open('out.html','w')
    f.write(data)
    f.close()

# @app.route('/static/image/<file_name>',methods=['GET'])
# def get_image(file_name):
#     image=open(os.path.join('image',file_name),'rb')
#     # res=make_response(image)
#     # res.headers['Content-Type']='image/png'
#     res=Response(image,mimetype='image/jpeg')
#     return res

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
