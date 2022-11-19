*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Mr.WORLDWIDE
    Set Password  culo305culo
    Set Confirm Password  culo305culo
    Register Account
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Mr
    Set Password  culo305culo
    Set Confirm Password  culo305culo
    Register Account
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Mr.WORLDWIDE
    Set Password  cu
    Set Confirm Password  cu
    Register Account
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  Mr.WORLDWIDE
    Set Password  culo305culo
    Set Confirm Password  culo503culo
    Register Account
    Register Should Fail With Message  Password and password confirmation must match

Login After Succesful Registration
    Set Username  pekka
    Set Password  python13
    Set Confirm Password  python13
    Register Account
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Go To Login Page
    Set Username  pekka
    Set Password  python13
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  wowza
    Set Password  colormesurprised
    Register Account
    Register Should Fail
    Go To Login Page
    Set Username  wowza
    Set Password  colormesurprised
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Fail
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Account
    Click Button  Register

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirm Password
    [Arguments]  ${password}
    Input Password  id:password_confirmation  ${password}  

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open


