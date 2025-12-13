from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Данные для заполнения формы
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполняем форму
        for field, value in data.items():
            wait.until(EC.presence_of_element_located((By.NAME, field))).send_keys(value)

        # Нажимаем Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждём появления классов валидации
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))

        # Проверяем zip-code — должен быть красным
        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class"), "Zip code не подсвечен красным"

        # Проверяем остальные поля — должны быть зелёными
        success_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
        assert len(success_elements) == len(data), "Не все поля подсвечены зелёным"

    finally:
        driver.quit()