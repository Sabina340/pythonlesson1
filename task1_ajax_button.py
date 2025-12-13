from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
button = wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton")))
button.click()

# Дождаться появления зелёной плашки
green_text = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
).text

print(green_text)  # Data loaded with AJAX get request.

driver.quit()