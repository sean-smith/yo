import requests
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='')



def send_yo(username, url='', loc=("", "")):
    data={'api_token': "048fd446-d462-4524-93c0-ad644d3387ee", 'username': username}
    if url != "" and loc==("",""):
        data["link"] = url
    elif url == "" and  loc != ("",""):
        data["location"] = loc
    r = requests.post("http://api.justyo.co/yo/", data)
    return r.status_code

@app.route('/')
def load_static():
    return app.send_static_file("index.html")

@app.route('/subscriber_count')
def first():
    num = requests.get("https://api.justyo.co/subscribers_count?api_token=048fd446-d462-4524-93c0-ad644d3387ee")
    num = num.json()["result"]
    return str(num)

@app.route('/first_time_user')
def load_static_first():
        return app.send_static_file("first.html")

@app.route('/yo', methods=["POST"])
def send_yo_handler():
    username = request.form["username"]
    url = request.form["url"]
    status = send_yo(username, url)
    if status != 200:
        return "Yo not sent check the username and try again"
    return "Yo sent to "+username+"!"

@app.route('/yo_recieved')
def yo_recieved():
    username = str(request.args.get("username"))
    location = str(request.args.get("location"))
    print("location: "+location)
    link = str(request.args.get("link"))
    print("link: "+link)
    r = send_yo(username, "", (location[0]+5, location[1]-2))
    return r


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=80)
