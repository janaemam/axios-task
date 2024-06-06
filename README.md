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
    sh
    docker build -t fintech-app .
    
2. Run the Docker container:
    sh
    docker run -p 5000:5000 fintech-app
    

#### Without Docker
1. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate
    
2. Install the dependencies:
    pip install -r requirements.txt
    
3. Run the application:
    flask run
    

### Running Tests
1. Activate the virtual environment if not already activated.
2. Run the tests:

    python -m unittest discover -s tests
    

## API Endpoints

- *POST /account*: Open a new account.
- *POST /deposit*: Deposit funds.
- *POST /withdraw*: Withdraw funds.
- *GET /balance/<account_id>*: Check the balance of an account.
- *DELETE //close/<int:id>*: Deletes account 