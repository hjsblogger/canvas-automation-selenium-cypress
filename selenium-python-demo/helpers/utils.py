import random
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable declarations
username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")
home_page_url_1 = "https://canvasjs.com/"
home_page_url_2 = "https://www.lambdatest.com/bug-smasher"
iFrameWaitTime = 30
iSmallWaitTime = 2
iWaitTime = 5

# Output of getBoundingRect()
# document.getElementsByClassName("canvasjs-chart-canvas hover")[0].getBoundingClientRect()
# bottom : 495.1875
# height : 441
# left : 329.046875
# right : 1275.046875
# top : 54.1875
# width : 946
# x : 329.046875
# y :  54.1875

# Get the width, height, and other dimensions of the canvas

def get_canvas_properties(driver, canvas_elem):
    """
    Retrieve properties of a canvas element's bounding rectangle.

    Parameters:
    driver: WebDriver instance
    canvas_elem: WebElement for the canvas element

    Returns:
    Dictionary of canvas properties including width, height, x, y, top, left, right, and bottom.
    """
    canvas_properties = driver.execute_script("""
        const canvas = arguments[0];
        const rect = canvas.getBoundingClientRect();
        return {
            width: rect.width,
            height: rect.height,
            x: rect.x,
            y: rect.y,
            top: rect.top,
            left: rect.left,
            right: rect.right,
            bottom: rect.bottom
        };
    """, canvas_elem)

    # Return the properties in case they are needed further
    return canvas_properties


# The challenge with moving to an offset in canvas is that
# you never know whether the coordinates being moved to
# is within the canvas or not

# Took help from AI for designing this logic
def show_click_coordinates(driver, element, x, y):
    # Get the position of the element relative to the viewport
    rect = driver.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        return { top: rect.top, left: rect.left };
    """, element)

    # Calculate the coordinates
    adjusted_x = rect['left'] + x
    adjusted_y = rect['top'] + y

    # JavaScript to create a dot at the specified coordinates
    driver.execute_script(f"""
        const dot = document.createElement('div');
        dot.style.position = 'absolute';
        dot.style.width = '10px';
        dot.style.height = '10px';
        dot.style.backgroundColor = 'blue';
        dot.style.borderRadius = '50%';
        dot.style.zIndex = '9999';
        dot.style.top = '{adjusted_y}px';
        dot.style.left = '{adjusted_x}px';
        
        // Append the dot to the body
        document.body.appendChild(dot);

        // Remove the dot after 3 seconds
        setTimeout(() => {{
            dot.remove();  /* remove the dot after 3 seconds */
        }}, 3000);
    """)

# Define the function to get random coordinates within the canvas
def get_random_coordinates(canvas_properties, canvas_width, 
        canvas_height, canvas_center_x, canvas_center_y):
    # Convert float values to integers
    left = int(canvas_properties['left'])
    top = int(canvas_properties['top'])
    width = int(canvas_properties['width'])
    height = int(canvas_properties['height'])
    
    random_x = random.randint(left, left + width + 100)
    random_y = random.randint(top, top + height + 200)

    # Adjust coordinates if they are outside the viewport size
    if (random_x >= canvas_width):
        random_x = canvas_center_x

    if (random_y >= canvas_height):
        random_y = canvas_center_y

    print(random_x, random_y)
    return random_x, random_y