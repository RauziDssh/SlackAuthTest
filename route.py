from bottle import route, run, view, request,HTTPResponse,response
import slackconf
import slackutil

@route('/')
@view("index")
def index():
    _token = request.get_cookie("_access_token")
    if _token is not None:
        r = HTTPResponse(status=302)
        r.set_header('Location', 'http://localhost:8080/info')
        return r
    return dict()

@route('/callback',method='GET')
def callback():
    #preserve Code into Cookie
    code = request.query.code
    state = request.query.state
    
    #Get Access token
    token,user = slackutil.GetAccessToken(code)
    if token is not -1:
        response.set_cookie("_access_token",token,max_age=3888000)
        #when authorization successed
        return "authorization success."
    else:
        #when authorization failed
        return "authorization failed."

@route("/info")
def info():
    _token = request.get_cookie("_access_token")
    if _token is None:
        r = HTTPResponse(status=302)
        r.set_header('Location', 'http://localhost:8080/')
        return r
    #return "youre code is " + _code
    return _token

run(host='localhost', port=8080)