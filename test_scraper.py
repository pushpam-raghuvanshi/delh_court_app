from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
# Comment this for now to show the browser
# options.add_argument("--headless")  

print("🚀 Setting up Chrome...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print("✅ Chrome launched successfully")

driver.get("https://www.google.com")
print("🌐 Google opened")

time.sleep(5)
driver.quit()
print("✅ Browser closed")
