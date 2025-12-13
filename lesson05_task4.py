from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # путь к geckodriver
    service = Service(r"C:\Users\hasan\Downloads\geckodriver.exe")

    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Открыть страницу логина
        driver.get("http://the-internet.herokuapp.com/login")

        # Ввести username
        username = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username.send_keys("tomsmith")

        # Ввести password
        password = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys("SuperSecretPassword!")

        # Нажать кнопку Login
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()

        # Найти зелёную плашку и вывести текст в консоль
        flash_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Убираем лишний символ '×' и пробелы
        text = flash_message.text.replace("×", "").strip()
        print("Текст с зелёной плашки:", text)

    finally:
        # Закрыть браузер
        driver.quit()

if __name__ == "__main__":
    main()