import requests
import os

FACE_KEY = os.environ.get('FACE_KEY')
FACE_URL = " https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

def face(image_url):
    headers = { 
                'Ocp-Apim-Subscription-Key': FACE_KEY
                }

    payload = {
                'returnFaceId': 'true',
                'returnFaceAttributes': 'emotion'
                }

    response = requests.post(FACE_URL,
                            headers=headers,
                            params=payload,
                            json={"url": image_url})

    data = response.json()

    total_emotions = {}

    for face in data:
        face_emotions = face['faceAttributes']['emotion']
        for emotion in face_emotions:
            if face_emotions[emotion] != 0:
                total_emotions[emotion] = total_emotions.get(emotion, 0) + face_emotions[emotion]

    num_people = len(data)
    total_emotions['anger'] = total_emotions.get('anger', 0)/num_people
    total_emotions['contempt'] = total_emotions.get('contempt', 0)/num_people
    total_emotions['disgust'] = total_emotions.get('disgust', 0)/num_people
    total_emotions['fear'] = total_emotions.get('fear', 0)/num_people
    total_emotions['happiness'] = total_emotions.get('happiness', 0)/num_people
    total_emotions['neutral'] = total_emotions.get('neutral', 0)/num_people
    total_emotions['sadness'] = total_emotions.get('sadness', 0)/num_people
    total_emotions['surprise'] = total_emotions.get('surprise', 0)/num_people
    
    return {
                        'anger': total_emotions['anger'],
                        'contempt': total_emotions['contempt'],
                        'disgust': total_emotions['disgust'],
                        'fear': total_emotions['fear'],
                        'happiness': total_emotions['happiness'],
                        'neutral': total_emotions['neutral'], 
                        'sadness': total_emotions['sadness'],
                        'surprise': total_emotions['surprise']
            }
