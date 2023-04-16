import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumWebInteraction:

    def __init__(self, driver_path = None):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver_path = webdriver.Chrome(r'C:/scraper_dependencies/chromedriver.exe')

    def scraper_directory(self):
        '''
        Sets up the directory dependency to drop the save files into by default.
        '''
        import os

        if not os.path.exists('./screenshot/'):
            os.mkdir('./screenshot/')
        else: 
            print("screenshot directory exists")

    def navigate_to_url(self, url):
        '''
        Instructs the chromedriver to load the webpage
        '''

        self.driver.get(url)

    def launch_browser(self, options=None):
        from selenium import webdriver
        
        self.driver = webdriver.Chrome(self.driver_path, options=options)

    def click_XPATH_element(self, xpath:str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def fill_form(self, xpath:str, value):
        field = self.driver.find_element(By.XPATH, xpath)
        field.clear()
        field.send_keys(value)

    def close(self):
        self.driver.quit()





