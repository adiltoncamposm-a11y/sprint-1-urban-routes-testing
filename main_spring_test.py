from selenium import webdriver
from trio import sleep_until

from locators import UrbanRoutesPage
import time


def test_numbers_to():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_to("9176517385")

    assert urban_routes_page.get_to_value() == "9176517385"

    driver.quit()

def test_numbers_from():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from("9176517385")

    assert urban_routes_page.get_from_value() == "9176517385"

    driver.quit()

def test_non_latin_characters_accept_from_field():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from("ελληνικά")

    assert urban_routes_page.get_error_message() == "Incorrect address"

    driver.quit()

def test_invalid_data_from_field():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from("漢字")

    assert urban_routes_page.get_error_message() == "Incorrect address"

    driver.quit()

def test_invalid_data_to_field():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("漢字")
    assert urban_routes_page.get_error_message() == "Incorrect address"
    driver.quit()

def test_destination_point_to_field():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1300 1st St")
    assert urban_routes_page.get_to_value() == "1300 1st St"
    driver.quit()


def test_transportation_icon_taxi():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from("eas 2nd")
    urban_routes_page.enter_to("1300 1st St")

    assert urban_routes_page.get_taxi_icon() == "Call a taxi"

    driver.quit()

def test_from_field_is_empty():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    assert urban_routes_page.get_from_value() == ""

    driver.quit()

def test_not_icon_transportation_shows():
    driver = webdriver.Chrome()

    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    assert not urban_routes_page.get_mode_active()
    driver.quit()

def test_not_latin_charracters_are_not_accepted_into_To_field():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("ελληνικά")
    assert urban_routes_page.get_error_message() == "Incorrect address"
    driver.quit()

def test_From_field_accept_latin_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East 2nd st")
    assert urban_routes_page.get_from_value() == "East 2nd st"
    driver.quit()

def test_to_field_accept_latin_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1300 1st")
    assert urban_routes_page.get_to_value() == "1300 1st"
    driver.quit()

def test_system_shows_error_message_when_leaving_from_field_empty():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("")
    urban_routes_page.enter_to("1300 1st")
    assert urban_routes_page.get_error_message() == "Enter the address"
    driver.quit()

def test_system_shows_error_message_when_leaving_to_field_empty():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East 2nd st")
    urban_routes_page.enter_to("")
    assert urban_routes_page.get_error_message() == "Enter the address"
    driver.quit()

def test_to_field_accept_one_character():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1")
    assert urban_routes_page.get_to_value() == "1"
    driver.quit()

def test_from_field_accept_one_character():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("1")
    assert urban_routes_page.get_from_value() == "1"
    driver.quit()

def test_from_field_accept_49_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("230 manhattan ave apartament 4a, Brooklyn, maspet")
    assert urban_routes_page.get_from_value() == "230 manhattan ave apartament 4a, Brooklyn, maspet"
    driver.quit()

def test_to_field_accept_49_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("230 manhattan ave apartament 4a")
    assert urban_routes_page.get_to_value() == "230 manhattan ave apartament 4a"
    driver.quit()

def test_from_field_accept_50_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("230 manhattan ave apartament 4a, Brooklyn, maspeth")
    assert urban_routes_page.get_from_value() == "230 manhattan ave apartament 4a, Brooklyn, maspeth"
    driver.quit()

def test_to_field_accept_50_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("230 manhattan ave apartament 4a, Brooklyn, maspeth")
    assert urban_routes_page.get_to_value() == "230 manhattan ave apartament 4a, Brooklyn, maspeth"
    driver.quit()

def test_from_field_does_not_accept_51_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("230 manhattan ave apartament 4a, Brooklyn, maspethe")
    assert urban_routes_page.get_from_value() == ""
    driver.quit()


def test_to_field_does_not_accept_51_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("230 manhattan ave apartament 4a, Brooklyn, maspethee")
    assert urban_routes_page.get_to_value() == ""
    driver.quit()

def test_from_field_does_not_accept_52_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("230 manhattan ave apartament 4a, Brooklyn, maspethee")
    assert urban_routes_page.get_from_value() == ""
    driver.quit()

def test_fto_field_does_not_accept_52_characters():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("230 manhattan ave apartament 4a, Brooklyn, maspethee")
    assert urban_routes_page.get_to_value() == ""
    driver.quit()

def test_from_field_trims_leading_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from(" East 2nd st")
    urban_routes_page.enter_to("1300 1st")

    assert urban_routes_page.get_from_value() == "East 2nd st"

    driver.quit()

def test_to_field_trims_leading_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_to(" 1300 1st")
    urban_routes_page.enter_from("East 2nd st")

    assert urban_routes_page.get_to_value() == "1300 1st"

    driver.quit()

def test_from_field_trims_trailing_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_from("East 2nd st ")
    urban_routes_page.enter_to("1300 1st")

    assert urban_routes_page.get_from_value() == "East 2nd st"

    driver.quit()

def test_to_field_trims_trailing_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()

    urban_routes_page.enter_to("1300 1st ")
    urban_routes_page.enter_from("East 2nd st")

    assert urban_routes_page.get_to_value() == "1300 1st"

    driver.quit()

def test_from_field_accept_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East 2nd st")
    assert urban_routes_page.get_from_value() == "East 2nd st"
    driver.quit()

def test_to_field_accept_spaces():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("git init1300 1st")
    assert urban_routes_page.get_to_value() == "1300 1st"
    driver.quit()

def test_from_field_accept_dashes():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East-2nd-st")
    assert urban_routes_page.get_from_value() == "East-2nd-st"
    driver.quit()

def test_to_field_accept_dashes():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1300-1st")
    assert urban_routes_page.get_to_value() == "1300-1st"
    driver.quit()

def test_from_field_accept_periods():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East.2nd.st")
    assert urban_routes_page.get_from_value() == "East.2nd.st"
    driver.quit()

def test_to_field_accept_periods():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1300.1st")
    assert urban_routes_page.get_to_value() == "1300.1st"
    driver.quit()

def test_from_field_accept_commas():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_from("East,2nd,st")
    assert urban_routes_page.get_from_value() == "East,2nd,st"
    driver.quit()

def test_to_field_accept_commas():
    driver = webdriver.Chrome()
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.open_page()
    urban_routes_page.enter_to("1300,1st")
    assert urban_routes_page.get_to_value() == "1300,1st"
    driver.quit()

