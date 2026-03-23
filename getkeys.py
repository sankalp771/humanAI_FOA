#for getting the keys from the website

import requests

raw = requests.post(
    "https://apply07.grants.gov/grantsws/rest/opportunity/details",
    data={"oppId": "354588"}
).json()

# Synopsis ke saare keys dekho
synopsis = raw.get("synopsis", {})
for key in synopsis.keys():
    print(key)