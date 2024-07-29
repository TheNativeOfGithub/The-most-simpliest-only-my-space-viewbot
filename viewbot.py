from selenium import webdriver as w
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user = input("Username: ")

delay = input("Delay: ")

views = int(input("Views: "))

driver = w.Firefox()

driver.get(f"https://only-my.space/{user}")

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

window_size = driver.get_window_size()

width = window_size['width']

height = window_size['height']

middle_x = width / 100 * 45

middle_y = height / 100 * 45

action = ActionChains(driver)

action.move_by_offset(middle_x, middle_y).click().perform()

for i in range(views):
    time.sleep(float(delay))
    driver.refresh()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    action.move_by_offset(middle_x, middle_y).click().perform()

driver.close()
