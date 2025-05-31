import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_password_length_16(driver):
    url = "https://www.browserling.com/tools/random-password"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # Wait for length input box and set value to 16
    length_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="random-password-length"]')))
    length_input.clear()
    length_input.send_keys("16")

    # Wait for dropdown and select "a-z lowercase"
    dropdown = wait.until(EC.presence_of_element_located((By.ID, "random-password-format")))
    select = Select(dropdown)
    select.select_by_visible_text("a-z lowercase")

    # Wait for Generate button and click it
    generate_button = wait.until(EC.element_to_be_clickable((By.ID, "random-password-generate")))
    generate_button.click()

    # Wait for the generated password textarea to have value
    password_textarea = wait.until(EC.presence_of_element_located((By.ID, "random-password-result")))

    # Give a moment for password to update
    time.sleep(1)

    generated_password = password_textarea.get_attribute("value")
    print("Generated Password:", generated_password)

    # Assert password length is 16
    assert len(generated_password) == 16, f"Expected length 16 but got {len(generated_password)}"
