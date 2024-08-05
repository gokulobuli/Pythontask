from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

webpage_title=driver.title
print(webpage_title)

curr_url=driver.current_url
print(curr_url)

content=(driver.find_element(By.XPATH, "//*[@id='root']/div").text)
with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
    file.write(content)
