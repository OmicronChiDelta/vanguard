#basic python file to architect the webscraping component in selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path_driver = "C:\\Program Files (x86)\\geckodriver.exe"
url = "https://www.vanguardinvestor.co.uk/investments/vanguard-lifestrategy-100-equity-fund-accumulation-shares/price-performance"

#open connection to url
driver = webdriver.Firefox(executable_path=path_driver)
driver.get(url)
time.sleep(5)

#locate and click button: "Search for more historical prices"
search = driver.find_element_by_css_selector(".mat-focus-indicator.short-button.mt-4.mb-4.mat-stroked-button.mat-button-base")
time.sleep(5)
search.send_keys(Keys.RETURN)
time.sleep(5)

