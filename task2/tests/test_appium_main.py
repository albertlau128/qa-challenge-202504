from datetime import datetime, timedelta
import time
import re
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Android",
    appPackage="hko.MyObservatory_v1_0",
    # appActivity='hko.homepage3.HomepageActivity', # disabled since will cause appium to crash and not able to start the app
    autoGrantPermissions=True,
    autoAcceptAlerts=True,
    # noReset= True, # do not reset app state before test, so that we can test the app from the start
)

# appPackage = 'hko.MyObservatory_v1_0'
appium_server_url = "http://localhost:4723"
swipe_duration = 700


def _calculate_swipe_coordinates(d, start_ratio, stop_ratio, is_vertical=True):
    """Calculate swipe coordinates based on the given start and stop ratios."""
    width = d.get_window_size()["width"]
    height = d.get_window_size()["height"]

    if is_vertical:
        start_x = int(width * 0.5)
        start_y = int(height * start_ratio)
        stop_x = start_x
        stop_y = int(height * stop_ratio)
    else:
        start_x = int(width * start_ratio)
        start_y = int(height * 0.5)
        stop_x = int(width * stop_ratio)
        stop_y = start_y

    return start_x, start_y, stop_x, stop_y


def swipe_down(d, start_y=0.25, stop_y=0.75, duration=swipe_duration):
    """Swipe down on the screen."""
    x1, y1, x2, y2 = _calculate_swipe_coordinates(d, start_y, stop_y, is_vertical=True)
    d.swipe(x1, y1, x2, y2, duration)


def swipe_up(d, start_y=0.75, stop_y=0.25, duration=swipe_duration):
    """Swipe up on the screen."""
    x1, y1, x2, y2 = _calculate_swipe_coordinates(d, start_y, stop_y, is_vertical=True)
    d.swipe(x1, y1, x2, y2, duration)


def swipe_left(d, start_x=0.75, stop_x=0.25, duration=swipe_duration):
    """Swipe left on the screen."""
    x1, y1, x2, y2 = _calculate_swipe_coordinates(d, start_x, stop_x, is_vertical=False)
    d.swipe(x1, y1, x2, y2, duration)


def swipe_right(d, start_x=0.25, stop_x=0.75, duration=swipe_duration):
    """Swipe right on the screen."""
    x1, y1, x2, y2 = _calculate_swipe_coordinates(d, start_x, stop_x, is_vertical=False)
    d.swipe(x1, y1, x2, y2, duration)


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        print("Setting up the test environment...")
        self.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities),
        )
        self.driver.implicitly_wait(10)  # seconds

        # debug print currently app package
        print(f"Current app package: {self.driver.current_package}")
        print(f"Current app activity: {self.driver.current_activity}")

        if self.driver.current_activity == ".AgreementPage":
            print("App is on the AgreementPage")
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Agree"]')
            for _ in range(2):
                el.click()
            # time.sleep(2)
            print(
                f"Current app activity: {self.driver.current_activity}, expected `.myObservatory_app_SplashScreen`"
            )
            self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.Button[@text="OK"]'
            ).click()
            # swipe left
            time.sleep(10)
            swipe_left(self.driver, start_x=0.9, stop_x=0.1)

            time.sleep(1)
            not_show_again = self.driver.find_elements(
                by=AppiumBy.XPATH, value='//*[@text="Do not show again"]'
            )
            if not_show_again:
                not_show_again[0].click()
            time.sleep(1)
            print(f"Done with setup, {self.driver.current_activity}")

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    # Placeholder test to ensure the test suite runs without errors, specifically to see if setUp works.
    # def test_placeholder_test(self) -> None:
    #     # Placeholder test to ensure the test suite runs without errors.
    #     assert self.driver is not None, "Driver is not initialized"

    def test_hko_get_forecast_next_date(self) -> None:
        """Test to see if the first forecast in the 9-day forecast screen is for tomorrow."""
        assert self.driver is not None, "Driver is not initialized"
        print("Starting test_hko_get_forecast_next_date...")
        # Find the element using XPath
        trials = 0
        while self.driver.current_activity != ".WeatherForecastActivity":

            self.driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.ImageButton[@content-desc="Navigate up"]',
            ).click()

            self.driver.find_element(
                by=AppiumBy.XPATH, value='//*[@text="Forecast & Warning Services"]'
            ).click()
            # self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="9-Day Forecast"]').click() # Noted this behaviour is unreliable, clicking another function
            self.driver.find_elements(
                by=AppiumBy.XPATH,
                value='//android.widget.ImageView[@resource-id="hko.MyObservatory_v1_0:id/icon"]',
            )[4].click()
            print(
                f"Current app activity: {self.driver.current_activity}, expected `.WeatherForecastActivity`"
            )
            # assert self.driver.current_activity == ".WeatherForecastActivity", (
            #     "Current activity is not WeatherForecastActivity, please check the app status."
            # )

            trials += 1
            if trials > 3:
                raise Exception("Cannot find the 9-day forecast screen")

        # is now in the 9-day forecast screen
        # get from top to bottom, the first 20 LinearLayout elements, and check if the first line is a date and is a proper date

        # attempt in implementing by scanning, not working :(

        # found=False
        # idx=0
        # while idx < len(self.driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.LinearLayout")) and idx<20:
        #     try:
        #         linearlayout = self.driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.LinearLayout")[idx]
        #         desc = linearlayout.get_attribute("content-desc")
        #         if desc == 'null':
        #             continue
        #         else:
        #             print(f'looking at {idx}th LinearLayout, content-desc: {desc}')
        #             if re.search(r'\d{1,2} \w{3-9}\n', desc):
        #                 date = desc.split('\n')[0]
        #                 print(f"Found date: {date}")
        #                 # assuming before 6am, the forecast is for today, otherwise will show tomorrow's forecast
        #                 expected_date = (datetime.now() + timedelta(days=1 if datetime.now().hour>6 else 0)).strftime('%d %b')
        #                 assert expected_date in desc, f"First forecast date is not today, expected: {expected_date}, actual: {desc}"
        #                 found=True
        #                 break
        #         idx+=1
        #     except Exception as e:
        #         print(f"Exception: {e}")
        #         idx+=1
        #         continue

        # the above method is not working, so we will just use the first 8 LinearLayout elements, a bit buffer to read till 15th LinearLayout
        # which should be the intermediate cards in the 9-day forecast screen
        # and check if the first line is a date and is a proper date

        # actual behaviour occasionally get stale element exception, will need to retry pytest script (TODO Improve/retry logics)

        cards_top = self.driver.find_elements(
            by=AppiumBy.XPATH, value="//android.widget.LinearLayout"
        )[7:15]
        for c in cards_top:
            desc = c.get_attribute("content-desc")

            if desc != "null":
                print(f"Candidate card content desc: {desc}")
                if re.search(r"\d{1,2} \w{3,}\n.*", desc):
                    date = desc.split("\n")[0]
                    print(f"Found date: {date}")

                    # Recall 9-day forecast screen does not update upon 0000 of the day:
                    # assuming before 6am, the forecast will show first forecast for D+0, otherwise will show D+1's forecast
                    expected_date = (
                        datetime.now()
                        + timedelta(days=1 if datetime.now().hour > 6 else 0)
                    ).strftime("%d %B")
                    print(f"Expected date: {expected_date}")
                    print(f"{desc=}")

                    assert (
                        expected_date in desc
                    ), f"First forecast date is not today, expected: {expected_date}, actual: {desc}"
                    return
                else:
                    print(f"^^ Not a date :(, continuing...")


if __name__ == "__main__":
    unittest.main()
