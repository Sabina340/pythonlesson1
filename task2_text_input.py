from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/textinput")

# Ввести текст SkyPro
input_field = wait.until(EC.visibility_of_element_located((By.ID, "newButtonName")))
input_field.send_keys("SkyPro")

# Нажать на кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получить текст кнопки
print(button.text)  # SkyPro

driver.quit()