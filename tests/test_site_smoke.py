
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the Mexico development website.
BASE_URL = "https://dev-new.progambling.bet/"


def test_website_opens(driver):
    # Open the website in Chrome.
    driver.get(BASE_URL)

    # Wait until the page body is present in the DOM.
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Verify that the browser opened the expected website.
    assert "dev-new.progambling.bet" in driver.current_url

    # Find the body element.
    page_body = driver.find_element(By.TAG_NAME, "body")

    # Verify that the page body is visible.
    assert page_body.is_displayed()

    # Print diagnostic information to help investigate the page.
    print("Current URL:", driver.current_url)
    print("Page title:", repr(driver.title))


# - BASE_URL: Website ka address ek jagah store karta hai.
# - By.TAG_NAME: HTML ke body element ko locate karta hai.
# - WebDriverWait(driver, 20): Condition poori hone ke liye maximum 20 seconds wait karta hai.
# - EC.presence_of_element_located(...): Check karta hai ki page ka body element DOM mein available hai.
# - assert: Expected result ko verify karta hai. Condition false hui, toh test fail hoga.
# test_ se shuru hone wala function name pytest ko test discover karne mein help karta hai. 