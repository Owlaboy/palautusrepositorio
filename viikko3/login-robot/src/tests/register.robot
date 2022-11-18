*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  andrei  andrei123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  hoikkamies123123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username and Valid Password
    Input New Command
    Input Credentials  ka  hoikkamies123123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  hoik
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  hoikkamies
    Output Should Contain  Password must contain at least one number

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
    Input  kalle
    Input  kalle123

