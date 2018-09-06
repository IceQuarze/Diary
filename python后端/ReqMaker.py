from urllib import request,parse
import json
# url=r'http://127.0.0.1:5000/verify_token'
# data={'token':'985d704c-3093-4860-bfa6-75f2aab72899'}
def post(url,data):
    data=parse.urlencode(data).encode('utf-8')
    req=request.Request(url,data=data)
    res=json.loads(request.urlopen(req).read())
    return res

def get(url,data):
    data=parse.urlencode(data).encode('utf-8')
    # req=request.Request(url,data=data)
    req=url+'?'+str(data)
    res=json.loads(request.urlopen(req).read())
    return res