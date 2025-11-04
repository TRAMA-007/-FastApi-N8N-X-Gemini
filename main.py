from fastapi import FastAPI , HTTPException
import requests 

app = FastAPI()

@app.get('/') 
def root ():
    return {'everything is good ! ⭐'}


@app.get('/ai')
def ai_reply(name : str , query : str , id) :
    response = requests.post('https://n8n.hjhj.me/webhook/4293fd14-e226-4730-9663-37d7b10c37cc' 
                             , json= {'userName' : name ,'userMessage' : query , 'userID': id})
    return (response.text)
