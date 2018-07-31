from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get('http://www.bolivia-sms.com/tigo.html')

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(2)

for i in range(10):
	image = driver.find_element_by_name('imgcaptcha')
	src = image.get_attribute('src')

	print(src)
	print("We are in de %s iteration" % (i))

	os.system("wget %s" % (src))
	time.sleep(2)

driver.close()
