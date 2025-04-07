# Task 2

Appium script for HKO App, pytest script for verify 9-day forecast actually showing correct date reuslt


### Prerequisite commands

#### Appium set-up
- Ensure `npm` is installed, `JAVA_HOME`, `ANDROID_HOME` are set in `environment variables`
- can use `appium-doctor` to verify configs
- if android do not exist is warned by `appium-doctor`, can safely ignore
- Using Android Studio device as mobile device for test, params are set in `test_appium_main.py`


#### To start appium server (CLI)
```
npm i -g appium
npm i -g appium-doctor
appium
appium driver install uiautomator2
appium setup
appium setup mobile
appium --use-plugins=inspector --allow-cors
```

### Running test 
(don't forget keep appium running, optionally inspector)

- using `-s` flag while running `pytest` to instantaneously see debug prints, can omit flag if too much info during runs

```
cd ./task2
poetry init
poetry env activate
pytest ./tests/ -s
```



### For future reference
- To use inspector, run `appium --use-plugins=inspector --allow-cors` and reach [localhost](http://localhost:4723/inspector) to begin
  - for configuration, please use 
  ```
  {
  "platformName": "Android",
  "appium:automationName": "UiAutomator2"
  }
  ```
  reference: https://appium.github.io/appium-inspector/latest/quickstart/starting-a-session/


### Backlog
- Enhance retry mechanism 
- Add further assertions to ensure capture unexpected events/jump/prod popups
