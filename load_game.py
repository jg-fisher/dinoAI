from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
from dinosaur import dinosaur
from capture import capture_feed
 
driver = webdriver.Chrome('/Users/owner/Desktop/all/tools/chromedriver')

# internet connection must be off
driver.get('http://www.google.com/')
time.sleep(2)

# main page to send key commands to
page = driver.find_element_by_class_name('offline')

# start game
page.send_keys(u'\ue00d')

# instance of dinosaur
dino = dinosaur.Dino(driver=driver)

# How I got pixel location
#import pyautogui, sys
#print('Press Ctrl-C to quit.')
#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True)
#except KeyboardInterrupt:
#    print('\n')

capture_feed.start()

while True:
    dino.up()



