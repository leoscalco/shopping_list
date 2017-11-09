# Shopping List and TDD

Project used for teaching full stack django development and Test Driven Development concepts to a class at the University of Sao Paulo.

## Getting Started

You need to start the django server:

* python manage.py runserver

### Prerequisites

To run the software you have to install:

* Django;
* Selenium;
* Coverage;

If you use Mac OS, it`s necessary install geckodriver to execute Selenium`s automated tests.

## Running the tests

To visualize where is missing tests, you may use the following command:

* coverage html

This command, show in HTML pages whats is already covered by tests.

To execute the tests (the code for tests is in the 'app'/tests.py file), you may use:

* coverage run manage.py test -v 2