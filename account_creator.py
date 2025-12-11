# account_creator.py

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
import random
from dotenv import load_dotenv
import os

load_dotenv()

def create_google_account():
    # Implement Google account creation here using Selenium
    # This part is complex and requires handling various Google's security measures.
    # You'll need to find elements, input data, solve captchas (if any), etc.

    print("Starting Google Account Creation")
    options = uc.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'--user-agent={user_agent}')
    driver = uc.Chrome(options=options)

    # Go to Google account creation page
    driver.get("https://accounts.google.com/signup")

    # Find the input fields
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )
    last_name_field = driver.find_element(By.ID, "lastName")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.NAME, "Passwd")
    confirm_password_field = driver.find_element(By.NAME, "ConfirmPasswd")

    # Generate random data
    first_name = "John" + str(random.randint(100, 999))
    last_name = "Doe" + str(random.randint(100, 999))
    username = "testuser" + str(random.randint(1000, 9999))
    password = "Password123!"

    # Fill the fields
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    username_field.send_keys(username)
    password_field.send_keys(password)
    confirm_password_field.send_keys(password)

    # Click the next button for password
    next_button = driver.find_element(By.ID, "passwdNext")
    next_button.click()
    time.sleep(2)

    # Click the next button for name
    next_button = driver.find_element(By.ID, "nameNext")
    next_button.click()
    time.sleep(2)

    # Phone Number Page
    try:
        phone_number_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "phoneNumberId"))
        )
        phone_number_field.send_keys(os.getenv('PHONE_NUMBER'))
        next_button = driver.find_element(By.ID, "phoneNext")
        next_button.click()
        time.sleep(2)

        verification_code = input("Enter verification code: ")
        verification_code_field = driver.find_element(By.ID, "verificationCode")
        verification_code_field.send_keys(verification_code)
        next_button = driver.find_element(By.ID, "verifyNext")
        next_button.click()
        time.sleep(2)
    except:
        print("Phone number not required")

    # Recovery Email Page
    try:
        recovery_email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "recoveryEmailId"))
        )
        recovery_email_field.send_keys("test@example.com")
        next_button = driver.find_element(By.ID, "recoveryNext")
        next_button.click()
        time.sleep(2)
    except:
        print("Recovery email not required")

    # Birthday and Gender Page
    month_field = driver.find_element(By.ID, "month")
    month_field.send_keys("January")
    day_field = driver.find_element(By.ID, "day")
    day_field.send_keys("1")
    year_field = driver.find_element(By.ID, "year")
    year_field.send_keys("2000")
    gender_field = driver.find_element(By.ID, "gender")
    gender_field.send_keys("Male")
    next_button = driver.find_element(By.ID, "genderNext")
    next_button.click()
    time.sleep(2)

    # Terms and Conditions Page
    agree_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "iagreebutton"))
    )
    agree_button.click()
    time.sleep(2)
    print("Google Account Created")

    driver.quit()

    return username + "@gmail.com", password  # Placeholder. Replace with actual email/password
