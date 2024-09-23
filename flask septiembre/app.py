from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image')
def image():
    return send_file('static/img/flor.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
