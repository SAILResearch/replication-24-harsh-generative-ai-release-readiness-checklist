import json
import time

import requests

from grey_ml_release.settings import settings


def collect(company=None):
    search_string = (
        settings.SEARCH_STRING if not company else f"{company} AND {settings.SEARCH_STRING}"
    )
    print(f"search string: {search_string}")
    headers = {
        "apikey": settings.SERP_API_KEY,
    }
    params = {
        "q": search_string,
        "search_engine": "google.com",
        "tbs": "sbd:1,cdr:1,cd_min:06/01/2018,cd_max:09/01/2023",
        "start": 1,
        "num": 100,
        "gl": "us",
        "hl": "en",
    }

    api_result = requests.get(
        "https://app.zenserp.com/api/v2/search", params=params, headers=headers
    )
    api_response = api_result.json()
    organic_results = api_response["organic"]

    print(f"Total {api_response['number_of_results']} results found")
    print(f"Total {len(organic_results)} results collected")
    # write urls to file
    fname = f"raw-{company}-results.json" if company else "raw-results.json"
    with open(settings.DATA_DIR / fname, "w") as f:
        json.dump(organic_results, f)


def main():
    if not settings.DATA_DIR.exists():
        settings.DATA_DIR.mkdir(parents=True)

    print("collecting data")
    start_time = time.time()
    collect()
    for company in settings.COMPANIES:
        collect(company)
    duration = time.time() - start_time
    print(f"collected data in {duration:.2f} seconds")
