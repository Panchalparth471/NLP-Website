import pymongo
import requests
import os
from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)


client = MongoClient(os.getenv('MONGODB_URL'))

db = client['NLP'] 
edenai_api_key = os.getenv('EDENAI_API_KEY')
@app.route('/')
def index():
    
    #render_template is used to render the file 
     return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_data', methods=['POST']) 
def add_data(): 
    # Get data from request 
    name=request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("password") 
    
    collection = db['data'] 
  
    # Insert data into MongoDB 
    collection.insert_one({"name":name, "email":email, "password":password,}) 
  
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    email=request.form.get("email")
    password=request.form.get("password")
    collection=db['data']
    result=collection.find_one({"email":email})
    
    
    if result and result.get("password") == password:
        return redirect("/home")
    elif result and result.get("password")!=password:
        return render_template("index.html",error="Invalid password")
    else:
        return render_template("index.html",error="Email not found");
    
@app.route('/home')
def home():
   return render_template('home.html')


@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/emotion')
def emotion():
    return render_template('emotion.html')

@app.route('/do_sentiment',methods=['POST'])
def do_sentiment():
     text=request.form.get("text")
     url = "https://api.edenai.run/v2/text/sentiment_analysis"


     payload = {
         "response_as_dict": True,
         "attributes_as_list": False,
         "show_original_response": False,
         "providers": "sapling,google,microsoft,emvista,tenstorrent,connexun,ibm,lettria,openai,amazon,nlpcloud",
         "language": "en",
         "text": text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization":  f"Bearer {edenai_api_key}"
     }

     response = requests.post(url, json=payload, headers=headers)
     data= response.json()
     openai_data = data.get('openai', {})
     openai_sentiment = openai_data.get('general_sentiment', 'N/A')
     openai_sentiment_rate = openai_data.get('general_sentiment_rate', 'N/A')
     return render_template('sentiment.html',message='{}->{}'.format(openai_sentiment,openai_sentiment_rate))
    
    
@app.route('/do_ner',methods=['POST'])
def do_ner():
     text=request.form.get("text")
     url = "https://api.edenai.run/v2/text/named_entity_recognition"

     payload = {
         "response_as_dict": True,
         "attributes_as_list": False,
         "show_original_response": False,
         "providers": "microsoft,amazon,google,neuralspace,lettria,tenstorrent,ibm,openai,nlpcloud",
         "language": "en",
         "text":text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization": f"Bearer {edenai_api_key}"
     }
     
     response = requests.post(url, json=payload, headers=headers)
     data=response.json()
     openai_data = data.get('openai', {})
     openai_data1 = openai_data.get('items', 'N/A')[0]
     openai_cat=openai_data1['category']
     openai_importance=openai_data1['importance']
     return render_template('ner.html',message='{} -> {}'.format(openai_cat,openai_importance)) 

@app.route('/do_emotion',methods=['POST'])
def do_emotion():
     text=request.form.get("text")
     url = "https://api.edenai.run/v2/text/emotion_detection"


     payload = {
      "providers": "nlpcloud,vernai",
      "text": text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization": f"Bearer {edenai_api_key}"
     }

     response = requests.post(url, json=payload, headers=headers)
     data= response.json()
     nlpcloud_data = data.get('nlpcloud', {})
     nlpcloud_data1 = nlpcloud_data.get('items', 'N/A')[0]
     nlpcloud_emotion=nlpcloud_data1['emotion']
     nlpcloud_score=nlpcloud_data1['emotion_score']
     return render_template('emotion.html',message='{} -> {}'.format(nlpcloud_emotion,nlpcloud_score)) 
     
#Debug is like nodemon for flask used for reflection continous changes
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
