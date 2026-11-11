from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://www.themealdb.com/api/json/v1/1"


@app.route("/", methods=["GET", "POST"])
def index():
    meals = []
    keyword = ""

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()

        if keyword:
            try:
                url = f"{API_URL}/search.php?s={keyword}"
                response = requests.get(url, timeout=15)
                response.raise_for_status()

                data = response.json()
                meals = data.get("meals") or []

            except requests.exceptions.RequestException:
                meals = []
                keyword = "ERROR_API"

    return render_template(
        "index.html",
        meals=meals,
        keyword=keyword
    )


@app.route("/detail/<meal_id>")
def detail(meal_id):
    meal = None
    error = None

    try:
        url = f"{API_URL}/lookup.php?i={meal_id}"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()
        meals = data.get("meals")

        if meals:
            meal = meals[0]
        else:
            error = "Detail resep tidak ditemukan."

    except requests.exceptions.RequestException:
        error = "Gagal mengambil detail resep."

    return render_template(
        "detail.html",
        meal=meal,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
