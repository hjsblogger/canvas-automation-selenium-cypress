from selenium import webdriver
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from helpers.utils import get_canvas_properties, show_click_coordinates
# This is for the variables
from helpers.utils import *

class TestCanvasGraphAutomation(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.browser_version = "latest"
        options.platform_name = "Windows 11"

        lt_options = {}
        lt_options["username"] = username
        lt_options["accessKey"] = access_key
        lt_options["video"] = True
        lt_options["resolution"] = "1440x819"
        lt_options["network"] = True
        lt_options["build"] = "[Canvas] Automatic data extraction from bar graphs"
        lt_options["name"] = "[Canvas] Automatic data extraction from bar graphs"
        lt_options["visual"] = True
        lt_options["w3c"] = True
        lt_options["plugin"] = "python-python"

        # Initialize the remote WebDriver session
        # driver = webdriver.Chrome()
        self.driver = webdriver.Remote(
            command_executor = "http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )
        self.driver.set_page_load_timeout(iWaitTime)
        self.driver.set_window_size(1440, 819)
        self.driver.maximize_window()
        self.driver.get(home_page_url_1)

        # Wait until the page is fully loaded
        WebDriverWait(self.driver, iWaitTime).until(lambda d: 
                d.execute_script("return document.readyState") == "complete")

        # time.sleep(iWaitTime)

    def test_canvas_automation(self):
        # Close the Chat button so that it does not hinder with the main page content
        try:
            # Switch to iFrame
            driver = self.driver
            iframe_elem = WebDriverWait(driver, iFrameWaitTime).until(
                EC.presence_of_element_located((By.ID, "hubspot-conversations-iframe"))
            )

            if iframe_elem:
                # Close the chat window
                driver.switch_to.frame(iframe_elem) 
                button_elem = WebDriverWait(driver, iFrameWaitTime).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                        "body > div.widget > div:nth-child(1) > div > div > button"))
                )
                print("Button Element found")
                button_elem.click()
                time.sleep(iSmallWaitTime)
        except Exception as e:
            print("Button Element not found:", e)
            status = "failed"
            self.update_lambdatest_status(status=status)

        # Switch back to the main document (parent frame)
        driver.switch_to.default_content()

        # Scroll to the end and back so that the dynamic content is loaded on the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Scroll to the start of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Waits for 5 seconds

        actions = ActionChains(driver)

        try:
            # Locate the graph
            canvas_elem = WebDriverWait(driver, iFrameWaitTime).until(
                EC.presence_of_element_located((By.ID, "themes-chart"))
            )
            print("Canvas Element found")
            actions.move_to_element(canvas_elem).perform()
            time.sleep(2)
        except Exception as e:
            print("Element not found:", e)
            status = "failed"
            self.update_lambdatest_status(status=status)

        # Get the canvas properties
        canvas_properties = get_canvas_properties(driver=driver, canvas_elem=canvas_elem)
        time.sleep(2)

        # Extracting each property from the returned dictionary for printing or usage
        canvas_left = int(canvas_properties["left"])
        canvas_x = int(canvas_properties["x"])
        canvas_y = int(canvas_properties["y"])
        canvas_top = int(canvas_properties["top"])
        canvas_width = int(canvas_properties["width"])
        canvas_height = int(canvas_properties["height"])
        canvas_right = int(canvas_properties["right"])
        canvas_bottom = int(canvas_properties["bottom"])

        # Print retrieved properties
        print(f"Canvas width: {canvas_width}")
        print(f"Canvas height: {canvas_height}")
        print(f"Canvas top: {canvas_top}")
        print(f"Canvas left: {canvas_left}")
        print(f"Canvas X: {canvas_x}")
        print(f"Canvas Y: {canvas_y}")
        print(f"Canvas right: {canvas_right}")
        print(f"Canvas bottom: {canvas_bottom}")

        # Define actual canvas width (in pixels) and calculate the scale factor
        canvas_actual_width = (canvas_width * 2)
        canvas_actual_height = (canvas_height * 2)

        # Find the scale factor
        scale_factor = canvas_width / canvas_actual_width

        # Calculate the center coordinates of the canvas
        canvas_center_x = canvas_width / 2
        canvas_center_y = canvas_height / 2

        print(f"Canvas center width: {canvas_center_x}")
        print(f"Canvas center height: {canvas_center_y}")

        # @hjsblogger - make this dynamic from the center of the canvas
        # start_x_coord = 245
        common_offset_value = 100
        start_x_coord = (canvas_width / 4) - common_offset_value
        start_y_coord = canvas_center_y

        # Define the number of iterations and offset step
        # January ~ August
        num_clicks = 8
        # x_offset_coord = 100
        # y_offset_coord = 100
        x_offset_coord = common_offset_value
        y_offset_coord = common_offset_value

        ############################ January - August #########################################
        for co_ord_value in range((num_clicks * x_offset_coord), 0, (-x_offset_coord)):
            x_click_coord = start_x_coord - co_ord_value
            y_click_coord = start_y_coord - y_offset_coord

            # Move to the calculated offset, click, and perform the action
            actions.move_to_element_with_offset(canvas_elem, x_click_coord, y_click_coord) \
                    .click().perform()
            
            time.sleep(2)

            # Call your function to show click coordinates
            show_click_coordinates(self.driver, canvas_elem, x = x_click_coord, y = y_click_coord)

            tooltip_elem = driver.find_elements(By.CLASS_NAME, "canvasjs-chart-tooltip")
            if (tooltip_elem[1]):
                print(tooltip_elem[1].text)

            time.sleep(2)

        ############################ September #########################################
        x_click_coord = start_x_coord
        y_click_coord = start_y_coord - y_offset_coord

        actions.move_to_element_with_offset(canvas_elem, x_click_coord,
                y_click_coord).click().perform()

        time.sleep(2)
        show_click_coordinates(self.driver, canvas_elem, x = x_click_coord,
            y = y_click_coord)

        tooltip_elem = driver.find_elements(By.CLASS_NAME, "canvasjs-chart-tooltip")
        if (tooltip_elem[1]):
            print(tooltip_elem[1].text)
        time.sleep(2)

        ############################ October - December #########################################
        # start_x_coord = 245
        x_offset_coord = 100
        y_offset_coord = 100
        # x_end_coord = 400
        num_clicks = 5

        for cnt in range(1, num_clicks):
            # Calculate new x and y offsets for this iteration
            x_click_coord = (start_x_coord + (cnt * x_offset_coord))
            y_click_coord = (start_y_coord - y_offset_coord)

            # Move to the calculated offset, click, and perform the action
            actions.move_to_element_with_offset(canvas_elem, x_click_coord, y_click_coord) \
                    .click().perform()
            
            time.sleep(2)

            # Call your function to show click coordinates
            show_click_coordinates(self.driver, canvas_elem, x = x_click_coord, y = y_click_coord)

            tooltip_elem = driver.find_elements(By.CLASS_NAME, "canvasjs-chart-tooltip")
            if (tooltip_elem[1]):
                print(tooltip_elem[1].text)

        status = "passed"

        # Update status on LambdaTest dashboard
        self.update_lambdatest_status(status=status)

        time.sleep(2)

    def update_lambdatest_status(self, status):
        """
        Update the test status on LambdaTest dashboard.
        
        Parameters:
        status (str): "passed" or "failed"
        """
        if status.lower() == "passed":
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

        self.driver.quit()

# Run the test
if __name__ == "__main__":
    unittest.main()