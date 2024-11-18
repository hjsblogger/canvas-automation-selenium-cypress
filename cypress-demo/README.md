<img width="826" height="500" alt="Banner" src="https://github.com/user-attachments/assets/a2bf5a77-df44-41a0-96a5-4021204042b0">

This repo contains implementation for automating interactions with Canvas elements using Selenium (+ Python) and Cypress. The tests are executed on the [LambdaTest cloud grid](http://www.lambdatest.com?fp_ref=himanshu15), but the same tests can also work with the respective test frameworks installed on the local machine.

## Canvas Element Handling With Cypress

Automating [LambdaTest Bug Smasher](https://www.lambdatest.com/bug-smasher) game play with Cypress on the LambdaTest cloud grid. The automated game play also works seamlessly on Cypress installed on local machine (i.e. macOS Sequoia 15.1). The resolution & viewport size is set to 1024*768.

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

#### Cloud Execution

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

For execution on LambdaTest, add the credentials (i.e. LambdaTest username & access-key) to the [following lines](https://github.com/hjsblogger/canvas-automation-selenium-cypress/blob/main/cypress-demo/lambdatest-config.json#L3).

**Step 5**

Now that the credentials are all set, trigger the command ```lambdatest-cypress run``` on the terminal to run Canvas element tests on LambdaTest.

<img width="1235" alt="cypress-lambdatest" src="https://github.com/user-attachments/assets/53cad0d3-7d4c-4546-8672-60c8124ac7ad">

Once the execution is triggered, navigate to the [LambdaTest automation dashboard](https://automation.lambdatest.com/) to check the status of the tests.

<img width="1435" alt="cypress-lambdatest-execution" src="https://github.com/user-attachments/assets/8fb4f8b7-a453-47dc-9f29-45f96db8b36f">

Shown below is the snapshot of the test execution where the game play is automated using Cypress (on LambdaTest cloud grid):

<img width="1435" alt="game-play-cypress-1" src="https://github.com/user-attachments/assets/c49e59a5-23d9-4c57-8d5e-502084b1b96b"><br/>

<img width="1435" alt="game-play-cypress-2" src="https://github.com/user-attachments/assets/98e2e72f-99b4-4275-9482-dedfa72bb058"><br/>

As seen above, I scored 85 points in the game :) Not a bad attempt at all :D.

#### Local Execution

**Step 3**

You can run the same test on Cypress (local machine) with Chrome (headed mode) browser by triggering the command ```npx cypress run --browser chrome --headed``` on the terminal. Please note that the Canvas implementation might require changes if the tests have to be executed on a different browser (e.g. Firefox, etc.).

**Step 4**

Shown below are some screenshots from game play automated on local machine:

<img width="1040" alt="cypress-local-execution" src="https://github.com/user-attachments/assets/5b1686e9-4339-4604-b978-7cf3c294cbd7"><br/>

<img width="1435" alt="game-play-canvas-local-1" src="https://github.com/user-attachments/assets/84324f06-33da-4acb-9bb7-b2a465d77260"><br/>

<img width="1440" alt="game-play-canvas-local-2" src="https://github.com/user-attachments/assets/b694d267-c3df-453f-b01a-4dd1daaffd74"><br/>

<img width="1440" alt="game-play-canvas-local-3" src="https://github.com/user-attachments/assets/22c9ace4-4921-4dd6-abf1-37b67540924d"><br/>

## Need Assistance?

Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)
<br/>
<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)
