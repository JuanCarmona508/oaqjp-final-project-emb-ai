import requests
import json

def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj = {"raw_document":{"text": text_to_analyse }}
    response = requests.post(url, json = myObj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        highest = 'anger'
        for emote in emotion:
            if emotion[highest] < emotion[emote]:
                highest = emote
        emotion['dominant_emotion'] = highest
    elif response.status_code == 400:
        emotion = {'anger':None, 'disgust':None, 'fear':None, 'joy':None,'sadness':None}
        emotion['dominant_emotion'] = None
    return emotion