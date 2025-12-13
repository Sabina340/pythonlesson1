from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# 1. Ждём, пока загрузится минимум 3 картинки
wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)

images = driver.find_elements(By.TAG_NAME, "img")

# 2. Ждём, пока у третьей картинки появится src
wait.until(lambda d: images[2].get_attribute("src") != "")

# 3. Получаем src
third_image_src = images[2].get_attribute("src")
print(third_image_src)

driver.quit()