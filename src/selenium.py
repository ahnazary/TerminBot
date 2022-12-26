from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random

class BotInterface:
    def __init__(self):
        driverPath = os.path.abspath(os.path.dirname(__file__)) + '/chromedriver_linux64/chromedriver'
        self.driver = webdriver.Chrome(driverPath)
        self.driver.get('https://termine.staedteregion-aachen.de/auslaenderamt/?rs')


        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="buttonfunktionseinheit-1"]'))
        )
        button.click()
        time.sleep(random.uniform(2, 3))