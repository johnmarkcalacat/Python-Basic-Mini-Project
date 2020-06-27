from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/home')
def home():
    return "home webpage"

if __name__ == "__main__":
    app.run(debug=True)