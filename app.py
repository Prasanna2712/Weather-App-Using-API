from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "79346829f1fdaeb44c34da5a04954b68"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city")   #  FIXED

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) == "200":   # FIXED
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
        else:
            weather_data = {"error": "City not found"}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
