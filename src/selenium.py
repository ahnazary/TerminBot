import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.utils import beep


class BotInterface:
    def __init__(self):
        driverPath = (
            os.path.abspath(os.path.dirname(__file__))
            + "/chromedriver_linux64/chromedriver"
        )
        self.driver = webdriver.Chrome(driverPath)
        self.driver.get("https://termine.staedteregion-aachen.de/auslaenderamt/?rs")

        # maximize window
        self.driver.maximize_window()

    def get_to_third_step(self):

        # accept cookies
        self.press_button('//*[@id="cookie_msg_btn_yes"]')

        # go to second step
        self.press_button('//*[@id="buttonfunktionseinheit-1"]')

        # click on the superC drop down menu
        self.press_button('//*[@id="header_concerns_accordion-114"]')

        # reserve one time
        self.press_button('//*[@id="button-plus-191"]')

        # press weiter button
        self.press_button('//*[@id="WeiterButton"]')

        # press ok button
        self.press_button('//*[@id="OKButton"]')

        
    def press_button(self, XPATH, wait_time: int = 5):
        button = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, XPATH))
        )
        self.driver.execute_script("arguments[0].click()", button)

    def check_for_appointment(self):
        # check if "Kein freier Termin verfügbar" text is present
        if "Kein freier Termin verfügbar" in self.driver.page_source:
            print("No free appointment available")
        else:
            # generate a beeo sound it there is a free appointment
            print("Free appointment available")
            for i in range(10):
                beep()
                time.sleep(15)
