*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Succeed

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page