from google.cloud import translate_v2 as translate
import os, json

from dotenv import load_dotenv
load_dotenv()


CREDENTIALS = json.loads(os.environ.get('CREDENTIALS'))

if os.path.exists('credentials.json'):
    pass
else:
    with open('credentials.json','w') as credFile:
        json.dump(CREDENTIALS, credFile)
    

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
translateClient = translate.Client()
 
detectResponse = translateClient.detect_language('hej amiko')
print(detectResponse)

#Translate the text
translateResponse = translateClient.translate('hej amiko','en')

print(translateResponse)