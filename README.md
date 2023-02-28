# Reto QA - Python y Selenium (SQUADMAKERS)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Built With

This following suite uses the following technologies and frameworks:
* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Behave](https://behave.readthedocs.io/en/stable/)
* [POM](https://www.browserstack.com/guide/page-object-model-in-selenium)


## Install lib


To run the suite you need to execute: 
```
pip install -r requirements.txt
```

## Running the tests

### Run the Suite

To run the suite you need to execute: 
```
behave features/Patrons/login.feature
```

##Project Structure


features - This folder contains the Gherkin .feature files, one per website page. By separating out the tests for each page into separate feature files we continue the Page Object Model theme of page independence and make it easier to extend the framework in the future.


allocator - This folder contains the webdriver configuration and its standard methods to be reused by the pages. 

pages - This folder contains a page and its locators, one for each page of the web

settings - This folder contains the configuration of the web driver, browser and base url

steps - This folder contains the steps that each feature will perform
  
requirements.txt - contains project dependencies


