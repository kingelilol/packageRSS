from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

def update(link):
    if re.search('www\.myhermes\.de/.+',link):
        return de(link)


def de(link):
    options = webdriver.firefox.options.Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options, log_path='/dev/null')
    driver.get(link)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'm-parcelhistory-date')))
    times = [entry.get_attribute('innerHTML').strip() for entry in driver.find_elements_by_class_name('m-parcelhistory-date')]
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'm-parcelhistory-status')))
    discriptions = [entry.get_attribute('innerHTML').strip() for entry in driver.find_elements_by_class_name('m-parcelhistory-status')]
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'm-parcelstatus-estimateddate')))
    estimate = driver.find_element_by_class_name('m-parcelstatus-estimateddate').text.split('\n')[2]
    driver.quit()
    
    return list(reversed([{'link':link, 'date': time , 'text': discription , 'edd': estimate} for time, discription in zip(times,discriptions)]))
