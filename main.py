from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

import time
#open disocrd
chrome_path = r"Chrome Driver Path"  #example: C:\Users\YourName\Downloads\chromedriver_win32\chromedriver.exe
driver = webdriver.Chrome(chrome_path)
driver.get("https://discord.com/login")
time.sleep(2)
#input email
driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input""").send_keys("Your Email")
time.sleep(2)
#input password
driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input""").send_keys("Your Password")
time.sleep(2)
#login click
driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]/div""").click()
time.sleep(10)
#discord server click
driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/div[2]/div[3]/div/div[2]""").click()
time.sleep(3)

#start bot
i = 0
timing = 0
while True:
    time.sleep(random.randint(5, 10))
    driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";s \n")
    print("SOLD")
    time.sleep(random.randint(2, 4))
    if i == 0:
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";up p max \n")
        print("PIC UPGRADE")
        i += 1
    else:
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";up b max \n")
        print("BACKPACK UPGRADE")
        i = 0
    time.sleep(random.randint(5, 8))
    bot_posts = driver.find_elements_by_class_name("message-2qnXI6")
    if "You can now ;rebirth" in bot_posts[-1].text:
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";rebirth \n")
        print("REBIRTH")
    if timing > 620:
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";f \n")
        print("FISHED")
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";h \n")
        print("HUNTED")
        time.sleep(3)
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";use 11 \n")
        time.sleep(3)
        driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div""").send_keys(";use 21 \n")
        timing = 0
    timing += 15

