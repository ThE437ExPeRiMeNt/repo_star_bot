# github_starer.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from undetected_chromedriver import Chrome, ChromeOptions

def create_github_account_and_star(email, password, target_repo):
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)

    # GitHub Account Creation
    driver.get("https://github.com/signup")
    time.sleep(2)

    # Find the email input field
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(email)
    time.sleep(2)

    # Click the continue button
    continue_button = driver.find_element(By.ID, "email-container")
    continue_button.click()
    time.sleep(2)

    # Find the password input field
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    time.sleep(2)

    # Click the continue button
    continue_button = driver.find_element(By.ID, "password-container")
    continue_button.click()
    time.sleep(2)

    # Find the username input field
    username_field = driver.find_element(By.ID, "login")
    username_field.send_keys(email.split('@')[0])
    time.sleep(2)

    # Click the continue button
    continue_button = driver.find_element(By.ID, "username-container")
    continue_button.click()
    time.sleep(2)

    # Find the verification input field
    verification_field = driver.find_element(By.ID, "verification")
    verification_field.send_keys("n")
    time.sleep(2)

    # Click the continue button
    continue_button = driver.find_element(By.ID, "verification-container")
    continue_button.click()
    time.sleep(2)

    # Find the create account button
    create_account_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div/form/div[5]/button")
    create_account_button.click()
    time.sleep(120) # Solve Captcha Manually

    # Navigate to the repository page
    driver.get(f"https://github.com/{target_repo}")
    time.sleep(2)

    # Check if already logged in, if not, log in
    try:
        login_button = driver.find_element(By.LINK_TEXT, "Sign in")
        login_button.click()
        time.sleep(2)

        # Find the username input field
        username_field = driver.find_element(By.ID, "login_field")
        username_field.send_keys(email)
        time.sleep(2)

        # Find the password input field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        time.sleep(2)

        # Find the sign in button
        sign_in_button = driver.find_element(By.NAME, "commit")
        sign_in_button.click()
        time.sleep(2)
    except:
        print("Already Logged In")

    # Star the repository
    try:
        star_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-sm') and contains(@class, 'js-toggler-target') and contains(@aria-label, 'Star')]")
        star_button.click()
        print(f"Starred repository {target_repo} with account {email}")
    except Exception as e:
        print(f"Could not star repository {target_repo} with account {email}: {e}")

    driver.quit()
