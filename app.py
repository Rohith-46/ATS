from flask import Flask, request, jsonify 
from dotenv import load_dotenv
from routes.init import register_blueprint
import os
load_dotenv()

SAVE_UPLOADED_FILE = os.getenv('SAVE_UPLOADED_FILE')

app = Flask(__name__)

os.makedirs(SAVE_UPLOADED_FILE,exist_ok=True)

register_blueprint(app)

if(__name__=="__main__"):
    print("running as an main file")
    app.run(debug= True, use_reloader = False)