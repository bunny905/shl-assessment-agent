from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import json


URL = "https://www.shl.com/solutions/products/product-catalog/"


def scrape_shl_catalog():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(URL)

    time.sleep(5)

    links = driver.find_elements(By.TAG_NAME, "a")

    assessments = []

    added = set()

    for link in links:

        href = link.get_attribute("href")
        text = link.text.strip()

        if href and "/products/product-catalog/view/" in href:

            if href in added:
                continue

            added.add(href)

            assessments.append({
                "name": text if text else "Unknown Assessment",
                "url": href,
                "test_type": "General",
                "skills": [text.lower()] if text else []
            })

    driver.quit()

    with open("app/data/assessments.json", "w") as file:
        json.dump(assessments, file, indent=4)

    print(f"Saved {len(assessments)} assessments")


if __name__ == "__main__":
    scrape_shl_catalog()