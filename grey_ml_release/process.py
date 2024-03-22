import csv
import json
import time

from grey_ml_release.settings import settings


def process(company=None):
    fname = f"raw-{company}-results.json" if company else "raw-results.json"
    with open(settings.DATA_DIR / fname, "r") as f:
        results = json.load(f)

    # extract urls
    urls = [
        {"url": result.get("url"), "title": result.get("title"), "date": result.get("date")}
        for result in results
    ]

    # write urls to file
    fname = f"raw-{company}-urls.csv" if company else "raw-urls.csv"
    with open(settings.DATA_DIR / fname, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "title", "date"])
        writer.writeheader()
        writer.writerows(urls)


def main():
    if not settings.DATA_DIR.exists():
        settings.DATA_DIR.mkdir(parents=True)

    print("processing data")
    process()
    start_time = time.time()
    for company in settings.COMPANIES:
        process(company)
    duration = time.time() - start_time
    print(f"processed data in {duration:.2f} seconds")
