from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
from capture import capture_feed
 
# change this to point to chromedriver location
driver = webdriver.Chrome('/Users/owner/Desktop/all/tools/chromedriver')

# internet connection must be off
driver.get('http://www.google.com/')
time.sleep(2)
page = driver.find_element_by_class_name('offline')
page.send_keys(u'\ue00d')

capture_feed.start()

while True:
    pass


