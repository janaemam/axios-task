import unittest
from app import create_app, db
from app.services import open_account, get_balance, delete_account

class AccountTestCase(unittest.TestCase):
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

    def test_open_account(self):
        with self.app.app_context():
            account = open_account("lily")
            self.assertIsNotNone(account.id)

    def test_check_balance(self):
        with self.app.app_context():
            account = open_account("lily")
            acc = get_balance(account.id)
            self.assertEqual(acc.balance, 0.0)

    def test_close_account(self):
        with self.app.app_context():
            account = open_account("lily")
            delete_account(account.id)
            balance = get_balance(account.id)
            self.assertIsNone(balance)

if __name__ == '__main__':
    unittest.main()