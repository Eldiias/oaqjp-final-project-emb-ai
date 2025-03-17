'''
This file defiens a emotion detection function
'''
import requests

def emotion_detector(text_to_analyse):
    """Function that performs the emotion detection
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json = myobj, headers=headers, timeout=30)
    if response.status_code==200:
        dct = response.json()['emotionPredictions'][0]['emotion']
        dct['dominant_emotion'] = [i for i,j in dct.items() if j==max(dct.values())][0]
        return dct
    elif response.status_code==400: 
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None}
        
