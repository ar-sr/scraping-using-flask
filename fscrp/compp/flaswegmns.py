from flask import Flask
import requests
import json
import requests
import pandas as pd
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'price intelligence software is up and running'

#sample url: http://127.0.0.1:5000/api/v1/gettfm/apples/apple
@app.route('/api/v1/getwegmens/<category>/<item>')
def gettfm(category,item):

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
    #return data#['items'][0]['name']
    items=data["items"]


# for item in items:
#     categories=item['categories']







    
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


df_items=pd.DataFrame(items)
cleaned_items=df_items[['name','base_price']]

cleaned_items.to_excel(f"scraped/{search_term}.xlsx",index=False)

if __name__ == '__main__':
#    debug mode
    app.run(debug=True, port=8000)