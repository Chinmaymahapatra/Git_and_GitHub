from flask import Flask, render_template, request
import requests

BACKEND_URL=""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    try:
        requests.post(BACKEND_URL + '/submittodoitem', json=form_data)
        return "Data submitted successfully"
    except Exception as e:
        return e


if __name__=='__main__':
    app.run(debug=True)