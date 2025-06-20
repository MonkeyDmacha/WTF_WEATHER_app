from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "eb3b653b9b7528d7fc5979e4934e1f42"  

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"].strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "main" in data:
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                }
            else:
                error = f"No weather data found for '{city}'."
        else:
            error = f"City '{city}' not found."

    return render_template("index.html", weather=weather, error=error)



if __name__ == "__main__":
    app.run(debug=True)
