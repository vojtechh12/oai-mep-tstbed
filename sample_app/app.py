from flask import Flask


app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>VEC testbed root page</h1>"

@app.route('/hello')
def hello():
    return '<h1>Hello I am a VEC testbed in the making</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)