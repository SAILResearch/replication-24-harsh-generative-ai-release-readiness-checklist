import csv
import json
import time

from grey_ml_release.settings import settings


def dedup(company=None):
    fname = f"raw-{company}-urls.csv" if company else "raw-urls.csv"
    with open(settings.RUN_DIR / "old" / fname, "r") as f:
        old_results = csv.DictReader(f)
        old_urls = [result["url"] for result in old_results]

    # update results file
    with open(settings.DATA_DIR / fname, "r") as f:
        results = csv.DictReader(f)
        results = [result for result in results if result["url"] not in old_urls]

    # write urls to file
    fname = f"raw-{company}-urls.csv" if company else "raw-urls.csv"
    with open(settings.DATA_DIR / fname, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "title", "date"])
        writer.writeheader()
        writer.writerows(results)


def main():
    if not settings.DATA_DIR.exists():
        settings.DATA_DIR.mkdir(parents=True)

    print("processing data")
    dedup()
    start_time = time.time()
    for company in settings.COMPANIES:
        dedup(company)
    duration = time.time() - start_time
    print(f"processed data in {duration:.2f} seconds")
