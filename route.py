from bottle import route, run, view, request,HTTPResponse,response

@route('/')
@view("index")
def index():
    return dict()

@route('/callback',method='GET')
def callback():
    code = request.query.code
    state = request.query.state
    response.set_cookie("_code",code,max_age=3888000)
    return str(code) + str(state)

@route("/info")
def info():
    _code = request.get_cookie("_code")
    if _code is None:
        r = HTTPResponse(status=302)
        r.set_header('Location', 'http://localhost:8080/')
        return r
    return "youre code is " + _code

run(host='localhost', port=8080)