from flask import Flask
import json

app = Flask(__name__)

json_file_path = 'data.json'

with open(json_file_path, 'r') as f:
    json_data = f.read()

data = json.loads(json_data)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/api')
def api():
    return data

if __name__=='__main__':
    app.run(debug=True)