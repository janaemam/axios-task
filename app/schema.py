from . import ma
from .model import Account, Transaction

class AccountSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model=Account
        load_instance=True

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model=Transaction
        load_instance=True