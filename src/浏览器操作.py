from selenium import webdriver
from time import sleep
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 隐式等待，超出时间还没有找到元素，将抛出异常
driver.get("http://www.baidu.com")

driver.refresh() #刷新网页







sleep(10)
driver.quit()