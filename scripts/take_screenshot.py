import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Run Chrome in headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-dev-shm-usage")
options.accept_insecure_certs = True

# Point directly to chromedriver in the EE
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1500, 1000)

# Get URL from environment variable
weburl = os.environ.get("WEBURL")

if not weburl:
    print("ERROR: environment variable 'WEBURL' is required", file=sys.stderr)
    driver.quit()
    sys.exit(1)

# Get screenshot path from environment variable
screenshot_path = os.environ.get("SCREENSHOT_PATH", "/tmp/screenshot.png")
os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

print(f"Opening: {weburl}")
driver.get(weburl)
driver.implicitly_wait(2)

# Capture screenshot
full_body_element = driver.find_element(By.TAG_NAME, "body")
full_body_element.screenshot(screenshot_path)
print(f"Screenshot saved: {screenshot_path}")

driver.quit()