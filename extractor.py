import requests
from datetime import datetime

def fetch_foa(opp_id):
    url = "https://apply07.grants.gov/grantsws/rest/opportunity/details"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        response = requests.post(url, data={"oppId": opp_id}, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed — site temporarily blocking. Try again in 30 seconds.")
        return {}
    except Exception as e:
        print(f"❌ Error: {e}")
        return {}

def parse_date(date_str):
    if not date_str or date_str == "N/A":
        return "N/A"
    try:
        clean = date_str.replace(" EDT", "").replace(" EST", "").strip()
        dt = datetime.strptime(clean, "%b %d, %Y %I:%M:%S %p")
        return dt.strftime("%Y-%m-%d")
    except:
        return date_str

def extract_fields(data, source_url):
    synopsis = data.get("synopsis", {})
    return {
        "foa_id": data.get("opportunityNumber", "N/A"),
        "title": data.get("opportunityTitle", "N/A"),
        "agency": synopsis.get("agencyName", "N/A"),
        "open_date": parse_date(synopsis.get("postingDate", "N/A")),
        "close_date": parse_date(synopsis.get("responseDate", "N/A")),
        "eligibility": synopsis.get("applicantEligibilityDesc", "N/A"),
        "program_description": synopsis.get("synopsisDesc", "N/A"),
        "award_ceiling": synopsis.get("awardCeilingFormatted", "N/A"),
        "award_floor": synopsis.get("awardFloorFormatted", "N/A"),
        "source_url": source_url
    }