# Tutorial: Running Selenium 3.xxx tests with Python 3.9 (on Cloud Grid)

<img width="634" alt="selenium_python_banner" src="https://github.com/user-attachments/assets/b4d101e5-0a06-4536-a610-dd4224fcf036">

<div><a href="https://i.ytimg.com/vi/rQyi9v6d5i8/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDG5wRcydWIDO3CBbYW-Fenao3N-w">Image Credit</a></div>
<br/>

## Pre-requisites for test execution

This repo is a modified version of the [official Selenium Python Sample](https://github.com/LambdaTest/python-selenium-sample). The changes will help in running Selenium 3 tests with Python 3.9 (on LambdaTest cloud grid).
The desired capabilities (for Selenium 3) can be generated using [LambdaTest Capabilities Generator](https://www.lambdatest.com/capabilities-generator/).

Follow the steps along to trigger the test execution:

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/9b40c9cb-93a1-4239-9fe5-99f33766a23a">

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

**Step 4**

The pre-requisites for this tutorial are: Python 3.9, urllib3 1.26.5 & Selenium 3.141.0. Run the command ```python3.9 --version``` and ```pip3.9 --version``` to check if Python 3.9 & pip (for Python 3.9) are installed on the machine.

<img width="217" alt="python3 9_installation" src="https://github.com/user-attachments/assets/a6d251d1-8ba9-461e-993d-6032987cd0ce">

Next run the command ```pip3.9 install -r requirements.txt``` to install the required packages in the venv.

<img width="1400" alt="python3 9_requirements" src="https://github.com/user-attachments/assets/e62afc91-f7b4-4ef1-8e13-1c10e738f556">

## Steps for test execution

With this, all the dependencies and environment variables are set. Trigger the command ```python3.9 lambdatest.py``` to trigger Selenium 3 tests (with Python 3.9) on the LambdaTest dashboard.

Shown below is the terminal screenshot of the test execution (success & intended failure scenario):

<img width="713" alt="python3 9_selenium3 14_success" src="https://github.com/user-attachments/assets/ef84f508-53ab-42c7-bc3d-0bd8e808c445">
<br></br>

<img width="1399" alt="python3 9_selenium3 14_failure" src="https://github.com/user-attachments/assets/6dfab085-ea8f-4cdd-8052-158eb9bdd088">

As seen below, the test execution was successful and the status is "Completed". You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1440" alt="lambdatest_dashboard_screenshot" src="https://github.com/user-attachments/assets/42028aa4-6f33-4d42-929a-b9d89a79e3c2">

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)