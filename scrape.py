import sys
import requests
import re
import json
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print('Usage: python scrape.py <config_file>')
    sys.exit(1)

config_file = sys.argv[1]

# Load the config file
with open(config_file) as f:
    config = json.load(f)

url = config["url"]
format_config = config["format"]

response = requests.get(url)

if response.status_code != 200:
    print('Error fetching URL:', response.status_code)
    sys.exit(1)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Initialize dictionary to hold JSON objects
data = []

# Iterate over format config and extract content
for key, value in format_config.items():
    matches = soup.find_all(class_=re.compile(value))
    for idx, elem in enumerate(matches):
        key_matches = {key: elem.get_text()}  # Create a new dictionary for each match
        if idx < len(data):

            # If the index already exists in the list, update the existing dictionary object
            data[idx].update(key_matches)
        else:

            # If the index doesn't exist in the list, append the new dictionary object
            data.append(key_matches)

# Print the resulting JSON table
print(json.dumps(data, indent=2))
