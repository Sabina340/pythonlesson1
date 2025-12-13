from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    service = Service(r"C:\Users\hasan\Downloads\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Открыть страницу
        driver.get("http://the-internet.herokuapp.com/inputs")

        # Найти поле ввода
        input_field = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        # 🔹 Меняем тип input с number на text
        driver.execute_script(
            "arguments[0].setAttribute('type', 'text');",
            input_field
        )

        # Вводим "Sky"
        input_field.send_keys("Sky")

        # Очищаем поле
        input_field.clear()

        # Вводим "Pro"
        input_field.send_keys("Pro")

    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    main()