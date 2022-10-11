#Steps to automate brower:

#Step 1:
#Install selenium package
#pip install selenium /selenium automates browsers

#Step 2:
#Import webdriver package from selenium 
#pip list /check version
python #enter into python script
from selenium import webdriver

#Step 3:
#Browser navigation using command
browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.maximize_window()
browser.get('https://youtube.com')

#Step 4:
#Navigate an element in web page using inspect element. Navigate browser options using containers.
#Container can be identified using id, class_name, xpath, selector, jspath , tag name, link_text.
#(Different website's container may be identified with different elements).
#After identifing the container, copy the xpath. 

#//*[@id="search"]

#Import By:
from selenium.webdriver.common.by import By

#Step5: Storing the container id in a variable. Variable would be used to identify the container. 
search_box = browser.find_element(By.XPATH, '//input[@id="search"]')

print(search_box)

#List functions 
#dir(browser)

#Step 6:
#Input key in search box
search_box.send_keys("Fearless")

#Import Keys:
from selenium.webdriver.common.keys import Keys

#Search the input key:
search_box.send_keys(Keys.ENTER)

#Step 7:
#Navigate the desired video link
#help(browser.find_element)

#search the link via key word
song = browser.find_element(By.PARTIAL_LINK_TEXT, "Lost Sky") 
song.click() #Click on the navigated link