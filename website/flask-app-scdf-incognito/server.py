from flask import Flask, render_template, request,jsonify
import base64
from flask import send_from_directory

from datetime import datetime, timedelta

import os
app = Flask( __name__, static_url_path='' )
# https://stackoverflow.com/questions/34066804/disabling-caching-in-flask
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

import json
import logging
import requests
from PIL import Image


last_image = []
port = int( os.getenv( 'PORT', 8000 ) )

@app.route('/')
def root():
    return app.send_static_file( 'index.html' )
    

@app.route('/responder')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    print(user)
    return app.send_static_file( 'blank.html' )

@app.route('/latest_image')
def help():
    # global last_image
    # print(last_image)
    return app.send_static_file('temp.png')

@app.route("/upload", methods=["POST"])
def upload():
    user = request.args.get('user')
    print(user)
    if request.method == "POST":
        files = request.files.getlist("file")
        print(files)
        for filex in files:
            filex.save('temp_picture')
            im = Image.open('temp_picture')
            im.save('static/temp.png')

    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    result_json = get_results_from_image_recognition()['images'][0]['classifiers'][0]['classes']
    # [{'class': 'sparse_traffic', 'score': 0.899}]
    type_incident = result_json[0]['class'] 
    confidence = result_json[0]['score']
    global table_json

    table_json.insert(0,{
        "Name":str(user),
        "Location":str(latitude)+'\n'+str(longitude),
        "Type":type_incident,
        "Severity":"Pending",
        "Status":"Pending Approval",
        "Time":str((datetime.utcnow() + timedelta(hours=8)).strftime("""%I:%M%p"""))
    })


    return app.send_static_file( 'responder_two.html' )
    # Store files



# @app.route('/send_image', methods=['GET','POST'])
# def send_image():
#     post = request.get_data()
#     print(post)
#     jsondata = json.loads((post.decode('utf8')))
#     global last_image
#     last_image = jsondata['image']
#     # print(get_results_from_image_recognition())
#     return jsonify({'success':True})



table_json = [
    {
        "Name":"Henry Lee",
        "Location":"Serangoon",
        "Type":"Road Accident",
        "Severity":"Mid",
        "Status":"Incoming ambulance",
        "Time":"05:50PM"
    },
    {
        "Name":"Aiman Ahmad",
        "Location":"Bedok",
        "Type":"Road Accident",
        "Severity":"Low",
        "Status":"Incoming ambulance",
        "Time":"05:50PM"
    },
    {
        "Name":"Yee Peng Yip",
        "Location":"Hougang",
        "Type":"Cardiac Arrest",
        "Severity":"High",
        "Status":"Administering CPR",
        "Time":"05:48PM"
    },
    {
        "Name":"Alicia Lim",
        "Location":"Sengkang",
        "Type":"Fire",
        "Severity":"Mid",
        "Status":"Incoming fire engine",
        "Time":"05:45PM"
    },
    {
        "Name":"Vijay Singh",
        "Location":"Jurong East",
        "Type":"Cardiac Arrest",
        "Severity":"High",
        "Status":"Ambulance arrived",
        "Time":"05:42PM"
    },
    {
        "Name":"Nadia Noor",
        "Location":"Novena",
        "Type":"Road Accident",
        "Severity":"Mid",
        "Status":"Ambulance arrived",
        "Time":"05:40PM"
    },
    {
        "Name":"Soh Jia Yi",
        "Location":"Yishun",
        "Type":"Fire",
        "Severity":"Low",
        "Status":"Fire engine arrived",
        "Time":"05:38PM"
    },
    {
        "Name":"Ramli Sarip",
        "Location":"Woodlands",
        "Type":"Road Accident",
        "Severity":"Mid",
        "Status":"Ambulance arrived",
        "Time":"05:37PM"
    },
    {
        "Name":"Chan Kim Fong",
        "Location":"Lavender",
        "Type":"Cardiac Arrest",
        "Severity":"High",
        "Status":"Ambulance arrived",
        "Time":"05:35PM"
    },
    {
        "Name":"Swee Yee Fei",
        "Location":"Kallang",
        "Type":"Cardiac Arrest",
        "Severity":"High",
        "Status":"Ambulance arrived",
        "Time":"05:34PM"
    },
]


@app.route('/table.json')
def table():
    x = []
    for y in table_json:
        x.append(list(y.values()))
    return jsonify({'data': x})

@app.route('/image_type')
def image_type():
    return (table_json[0]['Type'])

def get_results_from_image_recognition():
    url = "https://scdf-incognito.us-south.cf.appdomain.cloud/temp.png"
    # url = '127.0.0.1/latest_image'
    apikey = 'kPmmPhDT1KGM5Dm8XwXsOae76MISjxxGaWK9DphOh7cV'
    response = requests.get(f'https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?url={url}&version=2018-03-19&classifier_ids=DefaultCustomModel_1634610019', auth=('apikey', f'{apikey}'))

    print(response.text)
    return json.loads(response.text)

@app.route('/login')
def login():
    return app.send_static_file( 'login.html' )




# if __name__ == '__main__':
#     app.run( host='127.0.0.1', port=port, debug=True)


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
