from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

def update(link):
    if re.search('www\.dhl\.de/de/.+',link):
        return de(link)


def de(link):
    options = webdriver.firefox.options.Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options, log_path='/dev/null')
    driver.get(link)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shipmentCourseEntry')))
    times = [entry.get_attribute('innerHTML').strip() for entry in driver.find_element(By.CLASS_NAME, 'shipmentCourse').find_elements(By.CLASS_NAME, 'header')]
    discriptions = [entry.get_attribute('innerHTML').strip() for entry in driver.find_element(By.CLASS_NAME, 'shipmentCourse').find_elements(By.CLASS_NAME, 'status')]
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'eventDate')))
    estimate = driver.find_element(By.CLASS_NAME, 'eventDate').text
    driver.close()

    return list(reversed([{'link': link, 'date': time , 'text': discription , 'edd': estimate} for time, discription in zip(times,discriptions)]))
