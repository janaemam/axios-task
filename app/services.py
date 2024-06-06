from .model import Account, Transaction
from . import db


def open_account(name):
    account=Account(owner=name)
    db.session.add(account)
    db.session.commit()
    return account

def get_balance(id):
    account=Account.query.get(id)
    return account if account else None

def withdraw(id, amount):
    account = Account.query.get(id)
    if not account:
        return " Account not found", 404
    elif account.balance < amount:
        return "Insufficient funds", 400
    else:
        account.balance -= amount
        transaction = Transaction(amount=amount, type='withdraw', account_id=id)
        db.session.add(transaction)
        db.session.commit()
        return transaction, 200


def deposit(id, amount):
    account=Account.query.get(id)
    if not account:
        return "Account not found", 404
    else:
        account.balance += amount
        transaction = Transaction(amount=amount, type='deposit', account_id=id)
        db.session.add(transaction)
        db.session.commit()
        return transaction,200