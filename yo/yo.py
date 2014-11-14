import requests
from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='')

def send_yo(username, api_token):
    return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': username})

@app.route('/')
def load_static():
    return app.send_static_file("index.html")


@app.route('/yo/<username>')
def send_yo(username):
    requests.post("http://api.justyo.co/yo/", data={'api_token': "048fd446-d462-4524-93c0-ad644d3387ee", 'username': username})
    return "Yo sent to "+username+"!"

@app.route('/yo_recieved')
def yo_recieved():
    username = str(request.args['username'])
    print(type(username))
    print(request.data)
    print(request.header)
    return requests.post("http://api.justyo.co/yo/", data={'api_token': "048fd446-d462-4524-93c0-ad644d3387ee", 'username': username, link:"https://www.kickstarter.com/projects/bdommie/sea-rover"})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=80)
