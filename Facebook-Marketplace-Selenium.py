# facebook marketplace
import os
import json
import pyautogui
import requests
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

response = requests.request("GET", "https://dixhomes.com/mlsdata/auto_posting_json.php")
data = response.json()

property_type = data[0]["posting_type"]
no_of_bedroom = data[0]["bedrooms"]
no_of_bathrooms = data[0]["bathrooms"]
property_sqr_ft = data[0]["sqft"]
property_price = data[0]["price"]
property_description = data[0]["description"]
property_address = data[0]["address"]


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

main_url = "https://www.facebook.com/login/?next=%2Fmarketplace%2F"
email = "clpostingtest@outlook.com"
password = "Tyler.1969!!!"

class App:
    def __init__(self, path='D:\FacebookAutomation'):
        driver.maximize_window()
        driver.get(main_url)
        self.log_in()
        self.create_new_listing()

    def log_in(self):
        try:
            email_input = driver.find_element(By.ID, "email")
            email_input.send_keys(email)
            sleep(0.5)
            password_input = driver.find_element(By.ID, "pass")
            password_input.send_keys(password)
            sleep(0.5)
            login_button = driver.find_element(By.XPATH, "//*[@type='submit']")
            login_button.click()
            sleep(15)
        except Exception:
            print('Some exception occurred while trying to find username or password field')

    def create_new_listing(self):
        try:
            # create a list of Home for sale or Rent section
            create_new_listing = driver.find_element(By.XPATH, "//a[@aria-label='Create new listing']")
            create_new_listing.click()
            sleep(10)

            home_for_sell_or_rent = driver.find_element(By.XPATH,
                                                        "//span[contains(text(), 'Property for sale or rent')]")
            home_for_sell_or_rent.click()
            sleep(10)

            add_photo = driver.find_element(By.XPATH, "//span[text()='Add Photos']")
            add_photo.click()
            sleep(8)
            pyautogui.write(r"D:\homeImage.png")
            pyautogui.press('enter')
            sleep(10)

            home_for_sell_or_rent_field = driver.find_element(By.XPATH,
                                                              "//div[@role='main']//span[contains(text(), 'Property for sale or rent')]/following-sibling::div[contains(@id, 'jsc_c_')]")
            home_for_sell_or_rent_field.click()
            if(property_type == 'For Rent'):
                property_type = 'Rent'
            if(property_type == 'For Sale'):
                property_type = 'Sale'
            rent_dropdown_value = driver.find_element(By.XPATH, "//span[text()='" + property_type + "']")
            rent_dropdown_value.click()
            sleep(5)

            rental_type_field = driver.find_element(By.XPATH,
                                                    "//div[@role='main']//span[contains(text(), 'Type of property for rent')]/following-sibling::*[contains(@id, 'jsc_c_')]")
            rental_type_field.click()
            sleep(5)

            option_for_rental_type = driver.find_element(By.XPATH, "//span[text()='House']")
            option_for_rental_type.click()
            sleep(5)

            number_of_bedroom_field = driver.find_element(By.XPATH,
                                                          "//div[@role='main']//span[text()='Number of bedrooms']/following-sibling::input[contains(@id, 'jsc_c_')]")
            number_of_bedroom_field.send_keys(no_of_bedroom)
            sleep(2)

            number_of_bathroom_field = driver.find_element(By.XPATH,
                                                           "//div[@role='main']//span[text()='Number of bathrooms']/following-sibling::input[contains(@id, 'jsc_c_')]")
            number_of_bathroom_field.send_keys(no_of_bathrooms)
            sleep(2)

            price_per_month_field = driver.find_element(By.XPATH,
                                                        "//div[@role='main']//span[text()='Price per month']/following-sibling::input[contains(@id, 'jsc_c_')]")
            price_per_month_field.send_keys(property_price)
            sleep(2)

            rental_address_field = driver.find_element(By.XPATH,
                                                       "//div[@role='main']//span[text()='Address of property for rent']/following-sibling::input[contains(@id, 'jsc_c_')]")
            rental_address_field.send_keys(property_address)
            sleep(3)

            first_address_option = driver.find_element(By.XPATH,
                                                       "//ul[contains(@aria-label, 'suggested searches')]/li[1]/div")
            first_address_option.click()
            sleep(5)

            property_description_field = driver.find_element(By.XPATH,
                                                             "//div[@role='main']//span[contains(text(), 'Property for rent description')]/following-sibling::textarea[contains(@id, 'jsc_c_')]")
            property_description_field.click()
            property_description_field.send_keys(property_description)
            sleep(2)

            carper_area_field = driver.find_element(By.XPATH,
                                                    "//div[@role='main']//span[contains(text(), 'Carpet area')]/following-sibling::input[contains(@id, 'jsc_c_')]")
            carper_area_field.send_keys(property_sqr_ft)
            sleep(2)

            furniture_field = driver.find_element(By.XPATH,
                                                  "//div[@role='main']//span[text()='Furniture']/following-sibling::*[contains(@id, 'jsc_c_')]")
            furniture_field.click()
            furniture_field_option = driver.find_element(By.XPATH, "//span[text()='Furnished']")
            furniture_field_option.click()
            sleep(2)

            aircondition_type_field = driver.find_element(By.XPATH,
                                                          "//div[@role='main']//span[text()='Air conditioning']/following-sibling::*[contains(@id, 'jsc_c_')]")
            aircondition_type_field.click()
            aircondition_type_field_opt = driver.find_element(By.XPATH, "//span[text()='AC available']")
            aircondition_type_field_opt.click()
            sleep(2)

            listed_by_field = driver.find_element(By.XPATH,
                                                  "//div[@role='main']//span[text()='Listed by']/following-sibling::*[contains(@id, 'jsc_c_')]")
            listed_by_field.click()
            listed_by_field_opt = driver.find_element(By.XPATH, "//span[text()='Listed by owner']")
            listed_by_field_opt.click()
            sleep(5)

            next_button = driver.find_element(By.XPATH, "//div[@role='main']//span[text()='Next']")
            next_button.click()
            sleep(15)

            publish_button = driver.find_element(By.XPATH, "//span[text()='Publish']")
            publish_button.click()


        except Exception:
            print('Some exception occurred while trying to find username or password field')


if __name__ == '__main__':
    app = App()
