from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.cowin.gov.in/")

# Click on "FAQ" link and open a new window
faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
faq_link.click()

# Get the handle of the original window
original_window = driver.current_window_handle

# Click on "Partners" link and open another new window
partners_link = driver.find_element(By.LINK_TEXT, "Partners")
partners_link.click()

# Get all window handles
all_windows = driver.window_handles

# Display the window handles on the console
for index, window_handle in enumerate(all_windows):
    print(f"Window {index + 1} ID: {window_handle}")

# Close the new windows and switch back to the Home page
for window_handle in all_windows[1:]:
    driver.switch_to.window(window_handle)
    driver.close()

# Switch back to the original window (Home page)
driver.switch_to.window(original_window)

# Close the original window
driver.close()

# Quit the browser session
driver.quit()




