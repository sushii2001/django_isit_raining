# Is It Raining?

This application tracks the rain status for a specified location and notifies the user if it starts to rain.

## Prerequisites
*   WSL (Ubuntu on Windows, refer [here](https://learn.microsoft.com/en-us/windows/wsl/install))
*   Python 3.10+ for Backend.

## Setup

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd is_it_raining
    ```

## Backend

0. Setup python virtual environment:
    ```bash
    python -m venv rojak
    source rojak/bin/activate
    ```

    Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

1. Create djanggo project:

    ```bash
    # pip install django
    django-admin startproject mysite .
    ```

2. Run the server:
    ```bash
    python manage.py runserver
    ```

3. Create new application:
    ```bash
    python manage.py startapp homepage
    ```

4. Adding PostgreSQL support:
    ```bash
    pip install dj-database-url psycopg2-binary
    ```


## Frontend

0. Source code in `homepage/templates/homepage`


## Tests


## FAQ