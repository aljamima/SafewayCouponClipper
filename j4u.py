#!/usr/bin/python3
#### You MUST Install  Selenium(`pip install selenium`)
### and a WebDriver utility('http://chromedriver.chromium.org/downloads'). I Chose Chrome. 
## Maybe I will create a windows installer!!!!!
# maybe.
#localStorage.getItem('abCoupons')
#browser.execute_script("localStorage.getItem('abCoupons'))
#document.getElementById('couponAddBtn*').dispatchEvent(new MouseEvent("click"));
######## JavaScript snippet borrowed from "https://github.com/kton/Safeway-Just-for-u"
import os
import js2py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


usernameStr = 'email'
passwordStr = 'password'
##
chrome_options = Options()  
#chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),   options=chrome_options) 
urldeals = '''https://www.safeway.com/content/www/(banner)/en/justforu/coupons-deals.html'''
browser.get(('https://www.safeway.com/content/www/(banner)/en/justforu/coupons-deals.html'))
#browser.get(('https://www.safeway.com/CMS/account/login/?FullSite=Y&goto=https:%2F%2Fwww.safeway.com%2FShopStores%2FjustforU.page'))

js_crap = '''javascript:(function() {"use strict";var coupons = angular.element("#lt-coupon-area").scope().sharedValues.unfilteredItems.slice(); var token = localStorage.getItem("oktathenticateAccessToken"); if (token && coupons) { coupons.filter(function(x){return x.clipStatus==="U";}).forEach(function(item){ var data = {"items":[]}; var clip = {}; clip.clipType="C";clip.itemId=item.offerId;clip.itemType=item.offerPgm;clip.vndrBannerCd=""; var list = {}; list.clipType="L";list.itemId=item.offerId;list.itemType=item.offerPgm; data.items.push(clip);data.items.push(list); var request = new Request('https://nimbus.safeway.com/Clipping1/services/clip/items', { method: 'POST', mode: 'cors', redirect: 'error', headers: new Headers({ 'X-SWY_VERSION': '1.0', 'X-SWY_BANNER': 'safeway', 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json;charset=UTF-8', 'X-SWY_API_KEY': 'emjou', 'X-swyConsumerDirectoryPro': token }), body: JSON.stringify(data) }); fetch(request).then(function(){ document.querySelector("#headerMyListCount").textContent = parseInt(document.querySelector("#headerMyListCount").textContent,10)+1; }); }); } if (!token) { alert('not logged in or a website change broke this again'); }}());'''
xpath = '''/html/body/div[1]/div/div/div[1]/div/div/div/div[3]/div[2]/div[1]/div/div/div[3]/ul/li[1]/a/span[1]'''
x2 = '''//*[@id="sign-in-modal-link"]'''
#button = browser.find_element_by_xpath('//*[@id="label-email"]')
#button.click()
'''
button = browser.find_element_by_xpath(xpath)
button.click()
time.sleep(2)
button2 = browser.find_element_by_xpath(x2)
button2.click()
'''
time.sleep(2)
username = browser.find_element_by_id('label-email')
username.send_keys(usernameStr)
time.sleep(4)
password = browser.find_element_by_id('label-password')
password.send_keys(passwordStr)
time.sleep(2)
print("bout to hit sign in button")
signInButton = browser.find_element_by_id('btnSignIn') 
signInButton.click()
print("just clicked sign in button")


time.sleep(5)
signInClose = browser.find_element_by_id('onboardingCloseButton') 
signInClose.click()
time.sleep(5)
totaller = 0

def getem():
    for each in addButton1:
        each.click()
        global totaller 
        totaller = totaller + 1
        from random import randint
        from time import sleep
        sleep(randint(1,10))

addButton1 = browser.find_elements_by_xpath("//*[contains(@id, 'couponAddBtn')]")
if ! len(addButton1):
    print("empty list, no more coupons left. Or they caught on hahaha")
while len(addButton1) > 1:
    getem() 
    addButton1 = browser.find_elements_by_xpath("//*[contains(@id, 'couponAddBtn')]")
    

print(totaller)
'''

alertMessage = 'clipped a total of' + str(totaller) + ' coupons!!!'
print(alertMessage)

try:
    browser.execute_script("alert(alertMessage);")
except WebDriverException:
    pass
'''
