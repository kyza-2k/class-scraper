from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/scrape", methods=["GET"])
def scrape_endpoint():
    config = {
        "url": "https://example.com",
        "format": {
            "name": ".name-class",
            "price": ".price-class",
        },
    }
    data = scrape_website(config)
    return jsonify(data)


def scrape_website(config):
    url = config["url"]
    format_config = config["format"]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching URL:", response.status_code)
        return None

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Initialize dictionary to hold JSON objects
    data = []

    # Iterate over format config and extract content
    for key, value in format_config.items():
        matches = soup.select(value)
        for idx, elem in enumerate(matches):
            key_matches = {
                key: elem.get_text()
            }  # Create a new dictionary for each match
            if idx < len(data):
                # If the index already exists in the list, update the existing dictionary object
                data[idx].update(key_matches)
            else:
                # If the index doesn't exist in the list, append the new dictionary object
                data.append(key_matches)

    # Return the resulting JSON table
    return data


if __name__ == "__main__":
    app.run(debug=True)
