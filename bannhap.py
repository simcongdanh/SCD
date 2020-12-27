from selenium import webdriver
from time import sleep
import random, requests
import pytesseract
from PIL import Image
from io import BytesIO



url = "https://bayvip.vin/"
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(firefox_profile=profile)
browser.get(url)
sleep(2)
try:
    browser.find_element_by_class_name("btn-register").click()
except:
    browser.find_element_by_xpath("//*[@id='dvheader']/div/div[1]/div[1]").click()
sleep(1)
try:
    link = browser.find_element_by_id("captcha_image_register").get_attribute("src")
except:
    link = browser.find_element_by_xpath("//*[@id='captcha_image_register']").get_attribute("src")
link = str(url) + str(link)
r = requests.get(url)
im = Image.open(BytesIO(r.content))
im.save("bayvip.jfif")
sleep(2)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('bayvip.jfif')
capcha = pytesseract.image_to_string(img, lang="eng")
print(capcha)
