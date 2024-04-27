from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

# Define API request handlers
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/get_settings')
def get_settings():
    idInstance = request.args.get('idInstance')
    apiTokenInstance = request.args.get('apiTokenInstance')
    APIUrl = 'https://7103.api.greenapi.com'

    url = f"{APIUrl}/waInstance{idInstance}/getSettings/{apiTokenInstance}"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.text.encode('utf8')


@app.route('/get_state_instance')
def get_state_instance():
    idInstance = request.args.get('idInstance')
    apiTokenInstance = request.args.get('apiTokenInstance')
    APIUrl = 'https://7103.api.greenapi.com'

    url = f"{APIUrl}/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.text.encode('utf8')


@app.route('/send_message')
def send_message():
    phone_number = request.args.get('phone_number')
    message_context = request.args.get('message_context')
    idInstance = request.args.get('idInstance')
    apiTokenInstance = request.args.get('apiTokenInstance')
    APIUrl = 'https://7103.api.greenapi.com'
    print(message_context)

    url = f"{APIUrl}/waInstance{idInstance}/sendMessage/{apiTokenInstance}"

    payload = {
      "chatId": f"{phone_number}@c.us",
      "message": message_context
    }
    headers = {
      'Content-Type': 'application/json'
    }
  
    response = requests.post( url, headers=headers, json = payload)

    return response.text.encode('utf8')

@app.route('/send_file_by_url')
def send_file_by_url():
    file_url = request.args.get('file_url')
    idInstance = request.args.get('idInstance')
    apiTokenInstance = request.args.get('apiTokenInstance')
    APIUrl = 'https://7103.api.greenapi.com'
    phone_number = request.args.get('phone_number')

    url = f"{APIUrl}/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"

    payload = {
        "chatId": f"{phone_number}@c.us",
        "urlFile": file_url,
        "fileName": "simple.png",
        "caption": ""
    }
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json = payload)

    return response.text.encode('utf8')

if __name__ == '__main__':
    app.run(debug=True)
