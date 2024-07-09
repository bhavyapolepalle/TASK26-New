from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.imdb.com/search/name/"

    def load(self):
        self.driver.get(self.url)

    def fill_name_field(self, name):
        name_field = self.find_element(By.NAME, 'name')
        name_field.send_keys(name)

    def select_birth_month(self, month):
        birth_month = self.find_element(By.ID, 'birth_month')
        Select(birth_month).select_by_visible_text(month)

    def select_birth_day(self, day):
        birth_day = self.find_element(By.ID, 'birth_day')
        Select(birth_day).select_by_visible_text(day)

    def select_birth_year(self, year):
        birth_year = self.find_element(By.ID, 'birth_year')
        Select(birth_year).select_by_visible_text(year)

    def click_search(self):
        search_button = self.find_element(By.XPATH, '//button[@type="submit"]')
        search_button.click()