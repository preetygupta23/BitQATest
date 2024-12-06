from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def setpath():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield
    driver.close()


def test_browser_open(setpath):
    driver.get("https://www.britinsurance.com/")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
    # Locate the "Accept" button and click it
    accept_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    accept_button.click()
    search_button = driver.find_element(By.XPATH, "//button[@type='button']")
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
    search_button.send_keys('IFRS 17')
    main_window = driver.current_window_handle
    window_handles = driver.window_handles  # Switch to the new window (assuming it is the last one opened)
    for handle in window_handles:
        driver.switch_to.window(handle)
        if driver.current_url == "https://www.britinsurance.com/":
            print("this is the main window")
        else:
            driver.close()  # Now you can interact with the new window
