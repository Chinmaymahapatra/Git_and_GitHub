from flask import Flask, request
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
uri = os.getenv('MONGO_URI')
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["flask-tutorial-db"]

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return "Data submitted"

if __name__=='__main__':
    app.run(debug=True)