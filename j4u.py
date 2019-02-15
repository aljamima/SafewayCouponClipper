#!/usr/bin/python3
#### You MUST Install  Selenium(`pip install selenium`)
### and a WebDriver utility('http://chromedriver.chromium.org/downloads'). I Chose Chrome. 
## Maybe I will create a windows installer!!!!!
# maybe.
######## JavaScript snippet borrowed from "https://github.com/kton/Safeway-Just-for-u"
import os
import js2py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

usernameStr = 'email'
passwordStr = 'password'
##
chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),   chrome_options=chrome_options) 
##

#browser = webdriver.Chrome()
browser.get(('https://www.safeway.com/CMS/account/login/?FullSite=Y&goto=https:%2F%2Fwww.safeway.com%2FShopStores%2FjustforU.page'))
js_crap = '''javascript:(function() {"use strict";var coupons = angular.element("#lt-coupon-area").scope().sharedValues.unfilteredItems.slice(); var token = localStorage.getItem("oktathenticateAccessToken"); if (token && coupons) { coupons.filter(function(x){return x.clipStatus==="U";}).forEach(function(item){ var data = {"items":[]}; var clip = {}; clip.clipType="C";clip.itemId=item.offerId;clip.itemType=item.offerPgm;clip.vndrBannerCd=""; var list = {}; list.clipType="L";list.itemId=item.offerId;list.itemType=item.offerPgm; data.items.push(clip);data.items.push(list); var request = new Request('https://nimbus.safeway.com/Clipping1/services/clip/items', { method: 'POST', mode: 'cors', redirect: 'error', headers: new Headers({ 'X-SWY_VERSION': '1.0', 'X-SWY_BANNER': 'safeway', 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json;charset=UTF-8', 'X-SWY_API_KEY': 'emjou', 'X-swyConsumerDirectoryPro': token }), body: JSON.stringify(data) }); fetch(request).then(function(){ document.querySelector("#headerMyListCount").textContent = parseInt(document.querySelector("#headerMyListCount").textContent,10)+1; }); }); } if (!token) { alert('not logged in or a website change broke this again'); }}());'''
print(js_crap)
username = browser.find_element_by_id('input-email')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password-password')
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('create-account-btn') 
signInButton.click()
print('sleeping for 10 secs..')
time.sleep(10)
browser.execute_script(js_crap)
