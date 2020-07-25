from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
a=str(input("Masukan nama kontak target anda <=>"))
a2=str(input("Masukan pesan yang ingin di kirim <=>"))

driver =webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
time.sleep(60)
m=a2
person =driver.find_element_by_xpath('//span[@title = "{}"]'.format(a))
person.click()
while True:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(p)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)

