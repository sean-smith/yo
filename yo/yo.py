import requests
from flask import Flask, request, render_template
import urllib

app = Flask(__name__, static_url_path='')

api_key_yo_letter = "28a107be-5396-4e25-9760-e951e24893cd"
api_key_dc4lyfe = "048fd446-d462-4524-93c0-ad644d3387ee"

def send_yo(username, url='', loc=("", "")):
    data={'api_token': api_key_yo_letter, 'username': username}
    if url != "" and loc==("",""):
        data["link"] = url
    elif url == "" and  loc != ("",""):
        data["location"] = loc
    r = requests.post("http://api.justyo.co/yo/", data)
    return r.status_code

@app.route('/')
def load_static():
    return app.send_static_file("index.html")


@app.route('/sent')
def sent():
    username = request.args.get("username")
    if username != None:
        r = send_yo(username, "http://yomessage.me/?name="+username)
        return str(r)
    else:
        return '500'


@app.route('/subscriber_count')
def first():
    num = requests.get("https://api.justyo.co/subscribers_count?api_token=28a107be-5396-4e25-9760-e951e24893cd")
    num = num.json()["result"]
    return str(num)


@app.route('/yo', methods=["POST"])
def send_yo_handler():
    username = request.form["username"]
    username = username.lower()
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

@app.route("/yo_message", methods=["POST"])
def yo_message():
    message = request.form["message"]
    name = request.form["name"].lower()
    username = request.form["username"].lower()
    name = urllib.quote_plus(name)
    message = urllib.quote_plus(message)
    username_encoded = urllib.quote_plus(username)
    ip = "185.56.84.38"
    url = "http://"+ip+"/yo_message_recieved?message="+message+"&name="+name+"&username="+username_encoded
    #url = "http://54.148.80.59:81/yo_message_recieved?message="+message+"&name="+name
    if len(url) >= 2083:
        return "Message too long. Max length is 2,083 characters"
    try:
        r = send_yo(username, url)
    except:
        return "Yo not sent :("
    if r == 200:
        return "Message sent to "+username
    else:
        return "Error, please try again :("

@app.route("/yo_message_recieved")
def yo_send_recieved():
    message = request.args.get("message")
    name = request.args.get("name")
    username = request.args.get("username")
    return render_template("message.html", data={"message": message, "name": name, "username": username})


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=80)
