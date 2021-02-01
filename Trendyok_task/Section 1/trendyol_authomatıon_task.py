from selenium import webdriver
import logging
import time
import configparser
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Direction of webdriver has designated
driver = webdriver.Chrome(executable_path=r'D:\Automation\selenium\chromedriver.exe')

#Log file created and format designated
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.txt', level=logging.INFO)
logger = logging.getLogger()

#Variables will be get from a configure file
config = configparser.ConfigParser()
configFilePath = r'C:\Users\azatd\OneDrive\Desktop\otomasyon_practices\trendyol_task\config.properties'
config.read(configFilePath, encoding ="utf8")

class account_proceses:
    def login_account(self):

        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[class='link account-user']"))).click()
        time.sleep(2)

        #Enter cridential and enter
        driver.find_element_by_css_selector("input[id='login-email']").send_keys(config.get('variables', 'username'))
        driver.find_element_by_css_selector("input[id='login-password-input']").send_keys(config.get('variables', 'password'))

        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(2)

        #Check Logged in or not
        if driver.find_element_by_css_selector("div[class='link account-user']").is_displayed():
            logger.info("Logged in successfully")
        else:
            logger.info("Login failed")

class check_butiques:
    def butique_pages(butique_name):
        #Butique pages will be trigered. WebDriverWait structure will wait for page to load.
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//a[text()='{butique_name}']"))).click()
        time.sleep(1)

        #We are going to check each butique page if they loaded successfully or not
        path = driver.current_url
        r = requests.head(path)
        if r.status_code == 200:
            logger.info(f"{butique_name} page loaded successfully")
        else:
            logger.info(f"{butique_name} page failed")

class Products:
    def check_images_for_erkek(self):
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='ERKEK']"))).click()
        time.sleep(1)
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='component-list component-big-list']/article[1]/a[1]/span[1]"))).click()
        time.sleep(1)

    def add_product(self):
        #select Product
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='prdct-cntnr-wrppr']/div[1]/div[1]/a[1]/div[1]/div[1]/img[1]"))).click()
        time.sleep(1)
        #Add Product
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//div[text()='Sepete Ekle']"))).click()

        if driver.find_element_by_xpath(f"//div[text()='Sepete Eklendi']").is_displayed():
            logger.info("Product added successfully")
        else:
            logger.info("Product add process failed. Please Check")

#Website that we are going to work on, has opened
driver.get(r'https://www.trendyol.com/')
driver.maximize_window()

#Close Occured Popup
WebDriverWait(driver, 20).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[class='fancybox-item fancybox-close']"))).click()
time.sleep(2)

#Login
account_proceses.login_account(driver)

#Hit every butique page with loop
counter = 1
while counter != 10:
    butique_name = config.get('variables', f'boutique{counter}')
    check_butiques.butique_pages(butique_name)
    #Check images for selected butiques
    counter += 1

#Check every image at erkek butique(There are 24 product at first page)
Products.check_images_for_erkek(driver)
counter = 1
while counter != 25:
    if driver.find_element_by_xpath(f"//div[@class='prdct-cntnr-wrppr']/div[{counter}]/div[1]/a[1]/div[1]/div[1]/img[1]").is_displayed():
        logger.info(f"{counter}. Image displayed for ERKEK successfully")
    else:
        logger.info(f"{counter}. Image could not displayed. Please Check")
    counter += 1

#Add First Product at Erkek Butique
Products.add_product(driver)











