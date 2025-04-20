from flask import Flask, jsonify, request

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    from datetime import datetime
    import pytz
# This is a dictionary of capital cities and their matching timezone names.
    city_timezones = {
        "Paris": "Europe/Paris",
        "London": "Europe/London",
        "Washington": "America/New_York",
        "Tokyo": "Asia/Tokyo",
        "Delhi": "Asia/Kolkata",
        "Canberra": "Australia/Sydney"
    }

    city = request.args.get("city") #This gets the city from the URL.

    if not city:
        return jsonify({"error": "Please provide a capital city using ?city=CityName"}), 400

    if city not in city_timezones: #Return an informative message if the city isn't in your database.
        return jsonify({"error": f"{city} not found in our list. Try another capital."}), 404

    timezone = pytz.timezone(city_timezones[city]) # finds the timezone name based on the city.
    now = datetime.now(timezone) #This gives the current time in the city’s timezone.

    local_time = now.strftime("%Y-%m-%d %H:%M:%S") #Formats the time into a clean string like: "year-month-day hour:minute:second"
    utc_offset = now.strftime("%z") #This gives the UTC offset

    return jsonify({
        "city": city,
        "local_time": local_time,
        "utc_offset": utc_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)