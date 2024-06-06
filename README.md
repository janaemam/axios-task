# Axis Backend Task

## Overview
Simple fintech application for managing accounts and financial transactions.

## Features
- Open an account
- Deposit funds
- Withdraw funds
- Check balance
- Delete an account

## Setup

### Prerequisites
- Docker (optional)
- Python 3.10.4

### Running the application

#### Using Docker
1. Build the Docker image:

    docker build -t backend .

    
2. Run the Docker container:

    docker run -p 5000:5000 -e DATABASE_URL=<your_database_url_here> backend




#### Without Docker
1. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate
    
2. Install the dependencies:
    pip install -r requirements.txt


3. Set the environment variable for the database URL:
    either create a .env file with the db url or update the config file manually


4. Run the application:
    flask run


### Running Tests
1. Activate the virtual environment if not already activated.
2. Run the tests:

    python -m unittest discover -s tests


## API Endpoints

- *POST /account*: Open a new account.
    takes a name in body 
    {"name": "jana"}

- *POST /deposit*: Deposit funds.
    takes amount and id
    {"id":"2",
    "amount":500}

- *POST /withdraw*: Withdraw funds.
    takes amount and id
    {"id":"1",
    "amount":50}

- *GET /balance/<account_id>*: Check the balance of an account.
    takes id as parameter

- *DELETE //close/<int:id>*: Deletes account 
    takes id as parameter