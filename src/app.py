# src/app_geo.py    
from flask import Flask, jsonify, request, render_template
from src.get_data import load_data, clean_data

app = Flask(__name__)

# --- Load & clean data ---
df = clean_data(load_data())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/restaurants")
def api_restaurants():
    stars = request.args.get("stars")
    green = request.args.get("green")  # "all", "only", "none"
    dff = df.copy()
    if stars:
        wanted = [int(s) for s in stars.split(",") if s.isdigit()]
        dff = dff[dff["stars"].isin(wanted)]
    if green == "only":
        dff = dff[dff["green_star"] == True]
    elif green == "none":
        dff = dff[dff["green_star"] == False]

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for _, row in dff.iterrows():
        feat = {
            "type": "Feature",
            "properties": {
                "name": row["Name"],
                "award": row["Award"],
                "stars": int(row["stars"]),
                "green_star": bool(row["green_star"]),
                "cuisine": row.get("Cuisine",""),
                "city": row.get("City",""),
                "country": row.get("Country",""),
                "phone": row.get("PhoneNumber",""),
                "website": row.get("WebsiteUrl","")
            },
            "geometry": {
                "type": "Point",
                "coordinates": [row["Longitude"], row["Latitude"]]
            }
        }
        geojson["features"].append(feat)

    return jsonify(geojson)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
