import urllib.request
import json
import os

logos = {
    "LIC": "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Life_Insurance_Corporation_of_India_logo.svg/1024px-Life_Insurance_Corporation_of_India_logo.svg.png",
    "Star Health": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Star_Health_and_Allied_Insurance_Company_Limited_Logo.png/800px-Star_Health_and_Allied_Insurance_Company_Limited_Logo.png",
    "Aditya Birla Health": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Aditya_Birla_Capital_logo.svg/512px-Aditya_Birla_Capital_logo.svg.png",
    "ICICI Prudential": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/ICICI_Prudential.svg/1200px-ICICI_Prudential.svg.png",
    "HDFC Life": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/HDFC_Life.svg/1200px-HDFC_Life.svg.png",
    "Niva Bupa": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Niva_Bupa_Logo.svg/1024px-Niva_Bupa_Logo.svg.png",
    "Reliance Nippon": "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Reliance_Nippon_Life_Insurance.svg/1024px-Reliance_Nippon_Life_Insurance.svg.png",
    "Bajaj Allianz": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bajaj_Allianz_Life_Insurance.svg/1024px-Bajaj_Allianz_Life_Insurance.svg.png"
}

os.makedirs("logos", exist_ok=True)

for name, url in logos.items():
    if not url: continue
    filename = name.lower().replace(" ", "-") + ".png"
    filepath = os.path.join("logos", filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {name} to {filepath}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
