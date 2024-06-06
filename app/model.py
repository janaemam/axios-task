from . import db
from datetime import datetime

class Account(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    balance=db.Column(db.Float, default=0.0)
    created_at=db.Column(db.DateTime, default=datetime.now())
    owner=db.Column(db.String(100), nullable=False)

class Transaction(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    amount=db.Column(db.Float, nullable=False)
    type=db.Column(db.String(50), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    account_id=db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    account=db.relationship('Account', backref=db.backref('transactions', lazy=True)) 
