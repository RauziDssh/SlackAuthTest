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
    _token = request.get_cookie("_access_token")
    if _token is not None:
        r = HTTPResponse(status=302)
        r.set_header('Location', 'http://localhost:8080/info')
        return r

    #preserve Code into Cookie
    code = request.query.code
    state = request.query.state
    
    #Get Access token
    token,user = slackutil.GetAccessToken(code)
    if token is not -1:
        #when authorization successed
        if slackutil.isInSpecificTeam(token):
            #when user is in denx team
            response.set_cookie("_access_token",token,max_age=3888000)
            return '<!DOCTYPE html><html lang="ja"><head><meta http-equiv="Refresh" content="0;URL=http://localhost:8080/info"></head><body>authorization success.</body></html>'
        else:
            #when user is not in denx team
            return "This service is for only denx member."
    else:
        #when authorization failed
        return "authorization failed.If you're already authorized, you should go toppage."

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