from shortener import app

@app.route('/hello')
def helloWorld():
    return "Hello World!"