import requests
from flask import Flask, render_template, request # render_template loads HTML from /templates

app = Flask(__name__)

# Define the route for a homepage:


@app.route("/")
def home():
    # Return a simple string that is valid HTML
    # return "<h1>Welcome to my Flask App!</h1>"
    # Return the home template:
    return render_template("home.html")

@app.route("/jokes", methods=["GET", "POST"])
def jokes():
    mood_message = None
    joke = None
    error = None
    moods = ["Chill", "Bored", "Moody", "Aggressive", "Sad", "Focused"]
 
    if request.method == "POST":
        mood = request.form.get("mood")
       
        if mood == "Bored":
            mood_message = "You look so bored — Have a joke"
        if mood == "Chill":
            mood_message = "You're really chill today, just vibing."
        if mood == "Moody":
            mood_message = "Everything will be okay, here have a joke to cheer you up."
        if mood == "Aggressive":
            mood_message = "Seems you're in an aggressive mood, maybe this joke can calm you down."
        if mood == "Sad":
            mood_message = "Here, have a joke to cheer you up."
        if mood == "Focused":
            mood_message = "Hopefully this joke doesn't make you lose focus!"
 
 
 
        api_url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(api_url, headers=headers)
       
        if response.status_code == 200:
            joke = response.json().get("joke")
        else:
            error = "Couldn't find a joke at this time, sorry :("
 
    return render_template("jokes.html", error=error, moods=moods, joke=joke, mood_message=mood_message)

if __name__ == "__main__":
    # debug = True enables automatic reload on changes and better error messages
    app.run(debug=True)