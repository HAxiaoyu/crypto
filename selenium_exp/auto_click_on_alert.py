'''
Author: xyu
Date: 2023-03-23 15:42:16
LastEditors: xyu
LastEditTime: 2023-03-23 17:03:49
FilePath: \pyfiles\test\auto_click_on_alert.py
Description: 

'''
from selenium import webdriver                                      # allow launching browser
from selenium.webdriver.common.by import By                         # allow search with parameters
from selenium.webdriver.support import expected_conditions as EC    # determine whether the web page has loaded
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#不配置option会输出一堆东西
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-webgl")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path='D:\download\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service,options=options)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

while(1):

    alert=driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button')

    alert.click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)