import requests
import os

FACE_KEY = os.environ.get('FACE_KEY')
FACE_URL = "https://westus.api.cognitive.microsoft.com/face/v1.0/detect"

def face(image_url):
    headers = { 
                'Ocp-Apim-Subscription-Key': FACE_KEY
                }

    payload = {
                'returnFaceId': 'true',
                'returnFaceAttributes': 'emotion'
                }

    # image_url = 'https://i1.wp.com/www.usmagazine.com/wp-content/uploads/2019/12/Jamie-Lynn-Spears-Posts-Epic-Throwback-Photo-of-Britney-Spears-and-Justin-Timberlake.jpg?crop=0px%2C0px%2C2000px%2C1131px&resize=1200%2C675&ssl=1'
    response = requests.post(FACE_URL,
                            headers=headers,
                            params=payload,
                            json={"url": image_url})

    data = response.json()

    total_emotions = {
                        'anger': 0,
                        'contempt': 0,
                        'disgust': 0,
                        'fear': 0,
                        'happiness': 0,
                        'neutral': 0, 
                        'sadness': 0,
                        'surprise': 0
                        }

    for face in data:
        emotion_dict = face['faceAttributes']['emotion']
        total_emotions['anger'] = total_emotions['anger'] + emotion_dict['anger']
        total_emotions['contempt'] = total_emotions['contempt'] + emotion_dict['contempt']
        total_emotions['disgust'] = total_emotions['disgust'] + emotion_dict['disgust']
        total_emotions['fear'] = total_emotions['fear'] + emotion_dict['fear']
        total_emotions['happiness'] = total_emotions['happiness'] + emotion_dict['happiness']
        total_emotions['neutral'] = total_emotions['neutral'] + emotion_dict['neutral']
        total_emotions['sadness'] = total_emotions['sadness'] + emotion_dict['sadness']
        total_emotions['surprise'] = total_emotions['surprise'] + emotion_dict['surprise']
    
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


# print(face())
