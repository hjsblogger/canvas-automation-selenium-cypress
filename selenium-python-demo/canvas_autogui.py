# Inspiration - https://www.youtube.com/watch?v=lfk_T6VKhTE

import pyautogui
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from helpers.utils import get_canvas_properties, show_click_coordinates, get_random_coordinates
# This is for the variables
from helpers.utils import *

class TestCanvasGraphAutomation(unittest.TestCase):
    def setUp(self):
        # Initialize the remote WebDriver session
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(iWaitTime)
        self.driver.set_window_size(1024, 768)
        self.driver.maximize_window()
        self.driver.get(home_page_url_2)

        # Wait until the page is fully loaded
        WebDriverWait(self.driver, iWaitTime).until(lambda d: 
                d.execute_script("return document.readyState") == "complete")

        # time.sleep(iWaitTime)

    def test_canvas_automation(self):
        driver = self.driver
        try:
            # Locate the graph
            canvas_elem = WebDriverWait(driver, iFrameWaitTime).until(
                EC.presence_of_element_located((By.ID, "unity-canvas"))
            )
            print("Canvas Element found")
            # Scroll to the element
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", canvas_elem)
            time.sleep(iWaitTime)
        except Exception as e:
            print("Element not found:", e)
            status = "failed"
            self.update_lambdatest_status(status=status)

        # Get the canvas properties
        canvas_properties = get_canvas_properties(driver=driver, canvas_elem=canvas_elem)
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

        time.sleep(iWaitTime)

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

        # Coordinates for the button within the canvas (substitute with actual button coordinates)
        # Working
        button_x_in_canvas = 600  # example x position within canvas
        button_y_in_canvas = 620  # example y position within canvas

        # Calculate the absolute coordinates for the button
        absolute_x = canvas_x + button_x_in_canvas
        absolute_y = canvas_y + button_y_in_canvas

        canvasDisplayedWidth = canvas_properties['width']
        canvasDisplayedHeight = canvas_properties['height']

        # time.sleep(iWaitTime)

        show_click_coordinates(self.driver, canvas_elem, absolute_x, absolute_y)

        # Perform the click with PyAutoGUI at the calculated coordinates
        pyautogui.click(absolute_x, absolute_y)

        # time.sleep(iWaitTime)

        # Perform 60 random clicks inside the canvas
        for i in range(60):
            random_x, random_y = get_random_coordinates(canvas_properties, canvas_width,
                    canvas_height, canvas_center_x, canvas_center_y)
            
            # Log the coordinates to verify
            print(f"Clicking at X: {random_x}, Y: {random_y}")
            
            # Move to the coordinates and click using PyAutoGUI
            pyautogui.moveTo(random_x, random_y)
            show_click_coordinates(self.driver, canvas_elem, random_x, random_y)
            pyautogui.click()

            # Add a delay to see the clicks happen in real-time
            time.sleep(0.5)  # Adjust delay as needed

        print("Canvas Game Completed")

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
        # if status.lower() == "passed":
        #     self.driver.execute_script("lambda-status=passed")
        # else:
        #     self.driver.execute_script("lambda-status=failed")

        self.driver.quit()

# Run the test
if __name__ == "__main__":
    unittest.main()