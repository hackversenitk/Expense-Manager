from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import requests
import time

chromedriver = '/usr/local/bin/chromedriver'
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(chromedriver)

url = "http://localhost:5000/log"
driver.get(url)
# # time.sleep(1)
# element = driver.find_element_by_id("nochapter")
# element.click()
# element.send_keys("1")
# driver.find_element_by_xpath("//input[@value='set']").click() 
# # time.sleep(1)
# driver.find_element_by_xpath("//input[@name='initial_paid']").send_keys("0")
# driver.find_element_by_id("btn0").click()
# # time.sleep(1)
# driver.find_element_by_xpath("//input[@name='item-name0']").send_keys("mango")
# driver.find_element_by_xpath("//input[@name='item-price0']").send_keys("4")
# driver.find_elements_by_tag_name("p")[0].find_elements_by_tag_name("input")[0].click()
# driver.close()
driver.find_elements_by_class_name("submit-btn")[0].click()

driver.find_elements_by_class_name("person-name")[0].find_elements_by_tag_name("input")[0].send_keys("nix")
driver.find_elements_by_class_name("person-name")[1].find_elements_by_tag_name("input")[0].send_keys("shr")
driver.find_elements_by_class_name("person-name")[0].find_elements_by_tag_name("input")[1].send_keys("10")
driver.find_elements_by_class_name("person-name")[1].find_elements_by_tag_name("input")[1].send_keys("0")

driver.find_element_by_xpath("//input[@name='item0']").send_keys("apple")
driver.find_element_by_xpath("//input[@name='price0']").send_keys("10")

driver.find_element_by_xpath("//input[@name='item1']").send_keys("wine")
driver.find_element_by_xpath("//input[@name='price1']").send_keys("10")



# driver.find_elements_by_class_name("group")[1].find_elements_by_tag_name("input")[0].send_keys("idli")
# driver.find_elements_by_class_name("group")[1].find_elements_by_tag_name("input")[1].send_keys("30")

driver.find_elements_by_class_name("submit")[0].click()
# driver.close()




