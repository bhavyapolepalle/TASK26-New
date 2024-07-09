import pytest
from pages.search_page import SearchPage

def test_imdb_search(driver):
    search_page = SearchPage(driver)
    search_page.load()

    search_page.fill_name_field("Kumari")
    search_page.select_birth_month("November")
    search_page.select_birth_day("11")
    search_page.select_birth_year("1994")
    search_page.click_search()

