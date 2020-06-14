import requests

headers = {
    'Content-Type': 'application/json',
}

params = (
    ('version', '2018-05-01'),
)

text_to_convert = ''

language_code = 'zh'

data = '{"text":["'+text_to_convert+'"],"model_id":"en-'+language_code+'"}'

# response = requests.post('https://api.kr-seo.language-translator.watson.cloud.ibm.com/instances/1adb2727-c4ed-47a7-be9a-d3b56b40b47f/v3/translate?version=2018-05-01', headers=headers, data=data, auth=('apikey', 'v_1zA_9RZN_4XshF4_IKfg_qbIvADKjNuQqB-58a4Y7K'))
# print(response.text)

import requests

params = (
    ('url', 'https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/fruitbowl.jpg'),
    ('version', '2018-03-19'),
    ('classifier_ids', 'DefaultCustomModel_1634610019'),
)

# response = requests.get('https://gateway.watsonplatform.net/visual-recognition/api/v3/classify', params=params, auth=('apikey', '{apikey}'))

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# url = "https://www.straitstimes.com/sites/default/files/styles/article_pictrure_780x520_/public/articles/2018/06/17/yq-jbcarinci1-17062018.jpg"
# apikey = 'kPmmPhDT1KGM5Dm8XwXsOae76MISjxxGaWK9DphOh7cV'
# response = requests.get(f'https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?url={url}&version=2018-03-19&classifier_ids=DefaultCustomModel_1634610019', auth=('apikey', f'{apikey}'))

# print(response.text)

import json
def get_results_from_image_recognition():
    url = "https://scdf-incognito.us-south.cf.appdomain.cloud/temp.png"
    # url = '127.0.0.1/latest_image'
    apikey = 'kPmmPhDT1KGM5Dm8XwXsOae76MISjxxGaWK9DphOh7cV'
    response = requests.get(f'https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?url={url}&version=2018-03-19&classifier_ids=DefaultCustomModel_1634610019', auth=('apikey', f'{apikey}'))

    print(response.text)
    return json.loads(response.text)


print(get_results_from_image_recognition()['images'][0]['classifiers'][0]['classes'])