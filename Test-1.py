from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def launchBrowser():

    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("http://amiss.npc.com.vn/Login.aspx")

    return browser

browser = launchBrowser()

#Nhap ten dang nhap
ele_input = browser.find_element(value="txtUserName")

ele_input.send_keys("DLBABE")

time.sleep(3)
#Nhap mat khau
pw_input = browser.find_element(value="txtPassword")

pw_input.send_keys("Dlbabe@123")

time.sleep(3)
#Bam nut dang nhap
click_button = browser.find_element(value="btnLogin")

click_button.send_keys(Keys.ENTER)

time.sleep(3)
# Chon menu Du lieu khai thac
Menu_dlkt = browser.find_element(value="menuVh")

Menu_dlkt.click()

time.sleep(3)
# Chon menu Thong so van hanh
Menu_TSVH = browser.find_element(value="menuTsvh")

Menu_TSVH.click()

time.sleep(3)