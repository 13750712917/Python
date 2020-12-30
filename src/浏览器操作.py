from selenium import webdriver
from time import sleep
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 隐式等待，超出时间还没有找到元素，将抛出异常
driver.get("http://www.qq.com")


# 对网页进行操作，定位到元素，再跟上相应的动作
driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/a").click()
sleep(2)

driver.refresh() #刷新网页







sleep(10)
driver.quit()