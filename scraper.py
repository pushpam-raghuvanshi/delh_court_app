from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_case_data(case_type, case_number, year):
    try:
        # Setup headless browser
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Use new headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 20)

        print(f"🔍 Searching for: {case_type} {case_number} / {year}...")

        # Open Delhi High Court case status page
        driver.get("https://delhihighcourt.nic.in/case.asp")

        # Select Case Type
        case_type_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "ctype")))
        Select(case_type_dropdown).select_by_visible_text(case_type)

        # Enter Case Number and Year
        driver.find_element(By.NAME, "cno").send_keys(case_number)
        driver.find_element(By.NAME, "cyear").send_keys(year)

        # Submit
        driver.find_element(By.NAME, "B1").click()

        # Wait for result to load or error message
        time.sleep(3)

        # Look for result table
        try:
            table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'caseStatusTable')]")))
            rows = table.find_elements(By.TAG_NAME, "tr")
        except TimeoutException:
            return None  # Probably case not found or site changed

        # Parse rows into dictionary
        data = {}
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 2:
                key = cols[0].text.strip().rstrip(":")
                value = cols[1].text.strip()
                data[key] = value

        driver.quit()

        if not data:
            return None

        return {
            "case_title": data.get("Case Title", "N/A"),
            "petitioner": data.get("Petitioner", "N/A"),
            "respondent": data.get("Respondent", "N/A"),
            "status": data.get("Status", "N/A"),
            "last_hearing_date": data.get("Last Listed On", "N/A"),
            "next_hearing_date": data.get("Next Listed On", "N/A"),
            "court": "Delhi High Court",
            "bench": data.get("Bench", "N/A")
        }

    except Exception as e:
        print("⚠️ Error:", e)
        try:
            driver.quit()
        except:
            pass
        return None
