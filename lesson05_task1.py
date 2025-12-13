
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("http://uitestingplayground.com/classattr")
        time.sleep(30)

        # Ждём, пока синяя кнопка станет кликабельной, и кликаем
        btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
        btn.click()
        time.sleep(30)

        # Можно подождать чуть-чуть, чтобы увидеть результат
        wait.until(lambda d: True)  # placeholder (необязательно)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()