from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys

USER = sys.argv[1]
PASS = sys.argv[2]
FLAG = sys.argv[3]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
bro = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

bro.get('https://e-report.neu.edu.cn/notes/create')

#标签定位
search_input = bro.find_element_by_id('un')
#标签交互
search_input.send_keys(USER)

#标签定位
search_input = bro.find_element_by_id('pd')
#标签交互
search_input.send_keys(PASS)

#点击搜索按钮
btn = bro.find_element_by_class_name('login_box_landing_btn')
btn.click()

if FLAG == "1":
#点击搜索按钮
    btn = bro.find_element_by_id('bind_email_later')
    btn.click()

#点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[2]')
btn.click()

#点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span')
btn.click()
sleep(1)

#点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span')
btn.click()

#点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="app"]/main/div/form/div[6]/button/span')
btn.click()











