# BitQATest
Tech Stack :-
Programming Language:- Python
Framework :- Pytest
Libraries :- Selenium WebDriver(UI), Requests(API)
Web Browser :- Chrome

How to run the code:-
a) Take the pull from GitHub at your desktop.
b) Open the code in PyCharm code Editor.
c) Run with command on command prompt:-
d) Command to run both the test cases:- pytest 
e) command to execute a specific test case(e.g: the first UI test case) :- pytest Tests/test_BitQA01_UI.py


About the Assignment :-
It has two test cases for 2 questions given.
Pytest frmaework is to handle the execution of test cases.
For UI test case, Selenium 4 is used and chrome webdriver manager is used to launch the browser to remove the dependency of version of web browser drivers.
Pytest Fixture is used to provide the base information about the browser launch.
Explicit wait is used to perform the operation on expected conditions.

For API test case,
patch request is send and assert is used to verify the results. Assert statemnet are validations(or tests) on the response of API.
