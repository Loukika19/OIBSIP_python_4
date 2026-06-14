from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "fecc49b7f8644b651d42bc7e6fb467ff"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please enter a city name"})

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Print API response in terminal
        print("\nAPI Response:")
        print(data)

        if response.status_code != 200:
            return jsonify({
                "error": data.get("message", "City not found")
            })

        return jsonify({
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "error": "Unable to fetch weather data"
        })

if __name__ == "__main__":
    app.run(debug=True)