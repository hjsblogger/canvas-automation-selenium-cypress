<img width="826" height="500" alt="Banner" src="https://github.com/user-attachments/assets/a2bf5a77-df44-41a0-96a5-4021204042b0">

This repo contains implementation for automating interactions with Canvas elements using Selenium (+ Python) and Cypress. The tests are executed on the [LambdaTest cloud grid](http://www.lambdatest.com?fp_ref=himanshu15), but the same tests can also work with the respective test frameworks installed on the local machine.

Here are the overall usecases covered in the repo:

## Canvas Element Handling With Selenium Python

Follow the steps along to trigger the test execution:

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8"><br/>

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

**Step 4**

Install the dependencies by triggering the ```pip3 install -r requirements.txt``` command on the terminal.

<img width="1403" alt="selenium-chart-execution-1" src="https://github.com/user-attachments/assets/99e6f4d2-70fb-494b-8e23-1e325fb60be4"><br/>

#### Cloud Execution

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/9b40c9cb-93a1-4239-9fe5-99f33766a23a"><br/>

Set LambdaTest **Username** and **Access Key** in environment variables.

* For **Linux/macOS**:
  
```bash
export LT_USERNAME="LT_USERNAME" 
export LT_ACCESS_KEY="LT_ACCESS_KEY"
```
* For **Windows**:
```bash
set LT_USERNAME="LT_USERNAME" 
set LT_ACCESS_KEY="LT_ACCESS_KEY"
```

For demonstration, I am extracting tool-tip text from a bar-graph located in [CanvasJS](https://canvasjs.com/) website.

<img width="950" alt="CanvasBarGraph" src="https://github.com/user-attachments/assets/5002e7b3-bcb8-41b9-a9be-8c8d01258bd8"><br/>

<br/> Here, I have used Selenium and the PyUnit (or unittest) framework in Python.

The example code is available in the [following](https://github.com/hjsblogger/canvas-automation-selenium-cypress/tree/main/selenium-python-demo) location. Run the command ```python3 canvas_bar_graph.py``` command on the terminal to extract content from the bar-graph.

<img width="1293" alt="selenium-bar-chart-1" src="https://github.com/user-attachments/assets/e5ecf043-7662-4b91-a875-ce302a7a06d6"><br/>

<img width="709" alt="selenium-bar-chart-2" src="https://github.com/user-attachments/assets/e43b6b19-d81e-494e-a75e-bbb491212525"><br/>

Once the execution is triggered, navigate to the [LambdaTest automation dashboard](https://automation.lambdatest.com/) to check the status of the tests.

<img width="1440" alt="selenium-bar-graph-lambdatest-1" src="https://github.com/user-attachments/assets/cce6f9d0-54d3-4698-8f6f-e38482f89a23"><br/>

<img width="1440" alt="selenium-bar-graph-lambdatest-2" src="https://github.com/user-attachments/assets/6b5bb754-44b9-4cac-8f08-a82e470231b6"><br/>

As seen above, the tool-tip text from the Canvas element (i.e. bar graph) was successfully read using Selenium Python.

#### Local Execution

Automating [LambdaTest Bug Smasher](https://www.lambdatest.com/bug-smasher) game play with [PyAutoGUI](https://github.com/asweigart/pyautogui). PyAutoGUI is a cross-platform GUI automation Python module used for programmatically controlling the mouse & keyboard. Please note that you might need to adjust the co-ordinate positions in case the clicks are not occurring at the right positions!

Trigger the command ```python3 canvas_autogui.py``` on the terminal to automate game-play using [PyAutoGUI](https://github.com/asweigart/pyautogui).

<img width="1371" alt="pyautogui-1" src="https://github.com/user-attachments/assets/06adeef2-bb6f-4ff4-a468-ae2dae7d1ce7">

Here are some game-play screenshots that I captured using the Phone camera, since the browser window was in control of PyAutoGUI!

![pyauto-gui-2](https://github.com/user-attachments/assets/9dff1afd-e242-4898-8176-0966ffcdf440)<br/>
![pyauto-gui-3](https://github.com/user-attachments/assets/34738d93-761c-4bb4-b25d-07b930b04d9b)<br/>

With this, the game play automation (using PyAutoGUI) and bar-graph data extraction (Selenium Python on LambdaTest) is successful.

## Need Assistance?

Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)
<br/>
<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)