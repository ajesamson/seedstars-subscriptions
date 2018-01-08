# Seedstars Subscription

A simple Django application which stores names and email addresses in a database (SQLite)

### Features
1. Has welcome page in http://localhost/
    Note: this page has links to list and create functions
2. Lists all stored names/email address in http://localhost/list
3. Adds a name/email address to the database in http://localhost/add

### Installation Requirements
1. Python 3

### Usage
After cloning the repo and changing directory to the project, follow the following steps to run the application

* Run Migration for db setup
    ```
        python3 seedstars/manage.py migrate
    ```

* Run the application
    ```
        python3 seedstars/manage.py runserver
    ```

* Go to the url generated on your terminal which should be similar to this
    ```http://127.0.0.1:8000```

* To close the application press `ctrl + c` from your terminal

