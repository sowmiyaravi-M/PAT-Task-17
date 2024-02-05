from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set the path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the URL
driver.get('https://labour.gov.in/')

# Task 1: Download Monthly Progress Report
documents_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Documents')]")
documents_menu.click()

# Task 2: Download 10 photos from the Photo Gallery
media_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Media')]")
media_menu.click()

photo_gallery_submenu = driver.find_element(By.XPATH, "//a[contains(text(),'Photo Gallery')]")
photo_gallery_submenu.click()

# close the browser window
driver.quit()
