from flask import Flask
import requests
import json


app=Flask(__name__)


@app.route('/')

def home():
    return '<h1>home</h1>'



@app.route('/api/v1/getwegmans/<category>/<item>')

def getwegmans(category,item):
    
    
    with open('competitor.json','r') as file:
        competitor=json.load(file)['wegmans']
        
    URL=f"{competitor['store_api']}{category}/{item}" 
    
    
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': competitor ['cookie']    
        
    }
    response=requests.get(URL,headers=HEADERS)
    data=response.json()
    return data['items']


if __name__ == '__main__':
    app.run(debug=True,port=5000)
