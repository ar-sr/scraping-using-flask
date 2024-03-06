from flask import Flask
import requests
import json
import requests
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'price intelligence software is up and running'

#sample url: http://127.0.0.1:8000/api/v1/getwegmans/apples/apples
        
  
  
#wegmans      
@app.route('/api/v1/getwegmans/<category>/<item>')
def getwegmans(category,item):

    with open('competitor.json','r') as file:
        competitor = json.load(file)['wegmans'] #all 
           
           
                     
    URL = f"{competitor['store_api']}{category}/{item}" #xlsx
    
    HEADERS = { 
               
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':competitor['cookie']
}
    response = requests.get(URL,headers=HEADERS)
    data = response.json()
    #return data#['items'][0]['name']
    items=data["items"]
    
    
    for i in items:
        categories=i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict["name"].lower())
                if item in i['name'].lower():
                    item_found={
                        "name": i['name'],
                        "price":i['base_price']
                    }
                    
                    
    return ({"items":item_found})




#sprouts
@app.route('/api/v1/getsprouts/<category>/<item>')
def getsprouts(category,item):

    with open('competitor.json','r') as file:
        competitor = json.load(file)['sprouts']  
           
    URL = f"{competitor['store_api']}{category}/{item}"
    HEADERS = { 
               
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':competitor['cookie']
}
    response = requests.get(URL,headers=HEADERS)
    data = response.json()
    items=data["items"]
    
    
    for i in items:
        categories=i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict["name"].lower())
                if item in i['name'].lower():
                    item_found={
                        "name": i['name'],
                        "price":i['base_price']
                    }
                    
                    
                    
    return ({"items":item_found})






#tfm

@app.route('/api/v1/gettfm/<category>/<item>')
def gettfm(category,item):

    with open('competitor.json','r') as file:
        competitor = json.load(file)['tfm']  
           
    URL = f"{competitor['store_api']}{category}/{item}"
    HEADERS = { 
               
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':competitor['cookie']
}
    response = requests.get(URL,headers=HEADERS)
    data = response.json()
    #return data#['items'][0]['name']
    items=data["items"]
    
    
    for i in items:
        categories=i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict["name"].lower())
                if item in i['name'].lower():
                    item_found={
                        "name": i['name'],
                        "price":i['base_price']
                    }
                    
                    
    return ({"items":item_found})













if __name__ == '__main__':
#    debug mode
    app.run(debug=True, port=8000)