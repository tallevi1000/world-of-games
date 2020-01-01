from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions as selexcept
from time import sleep  # TODO: remove in final version


def test_scores_service():
    access_url = requests.get("http://127.0.0.1:5000/")  # Access the site
    if access_url.status_code == 200:
        print("Site is up")  # TODO: remove in final version
        print(access_url.status_code)
        try:
            chrome_drive.get("http://127.0.0.1:5000/")  # Access the site
            player_score = chrome_drive.find_element_by_id("score")
            print(f"Player score is: {player_score.text}")  # TODO: remove in final version

            if 0 < int(player_score.text) < 1000:
                print("Score is within a valid range")  # TODO: remove in final version
                return 0
            else:
                print("Score is out of range")  # TODO: remove in final version
                return -1

        except selexcept.NoSuchElementException:
            print("Element not found")  # TODO: remove in final version
            return -1

        except Exception as ex:  # Catch generic exception
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            print("Page not found")
            return -1
        finally:
            sleep(5)  # TODO: remove in final version
            chrome_drive.close()
    else:
        print("Site is down")  # TODO: remove in final version
        print(access_url.status_code)


def main_function():
    return_code = test_scores_service()
    if return_code == 0:
        print("Test run successfully.")  # TODO: remove in final version
        return 0
    elif return_code == -1:
        print("Something happened.")  # TODO: remove in final version
        return -1


# Set the chrome driver with headless option
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_drive = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

# Run the main test function
rc = main_function()
print(f"The return code is {rc}")  # TODO: remove in final version
