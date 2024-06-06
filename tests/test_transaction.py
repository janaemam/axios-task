import unittest
from app import create_app, db
from app.services import open_account, deposit, withdraw

class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2811@localhost/axios'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_deposit(self):
        with self.app.app_context():
            account = open_account("jana")
            transaction, status = deposit(account.id, 100.0)
            self.assertIsNotNone(transaction.id)
            self.assertEqual(transaction.amount, 100.0)

    def test_withdraw(self):
        with self.app.app_context():
            account = open_account("jana")
            deposit(account.id, 100.0)
            transaction, status = withdraw(account.id, 50.0)
            self.assertIsNotNone(transaction.id)
            self.assertEqual(transaction.amount, 50.0)

if __name__ == '_main_':
    unittest.main()