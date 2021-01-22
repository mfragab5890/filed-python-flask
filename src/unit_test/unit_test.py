import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from src.app import create_app
from src.models.models import *


class FiledApiTestCase(unittest.TestCase):
    """This class represents the Filed API test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'filed_test'
        setup_db(self.app, self.database_name)

        self.new_payment = {
            "CreditCardNumber": "3530111333300000",
            "CardHolder": "mostafa fouad",
            "ExpirationDate": "2200-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }
        self.invalid_card_number = {
            "CreditCardNumber": "35301113333000",
            "CardHolder": "mostafa fouad",
            "ExpirationDate": "2200-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }
        self.no_card_holder = {
            "CreditCardNumber": "3530111333300000",
            "ExpirationDate": "2200-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }
        self.expired_card = {
            "CreditCardNumber": "3530111333300000",
            "CardHolder": "mostafa fouad",
            "ExpirationDate": "2000-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }
        self.no_security_code = {
            "CreditCardNumber": "3530111333300000",
            "CardHolder": "mostafa fouad",
            "ExpirationDate": "2200-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }
        self.invalid_amount = {
            "CreditCardNumber": "3530111333300000",
            "CardHolder": "mostafa fouad",
            "ExpirationDate": "2200-01-21 18:12:33.747907",
            "SecurityCode": "424",
            "Amount": 1990
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all(app=create_app())

    def tearDown(self):
        """Executed after reach test"""
        pass

    # test post a new payment to database(gatway)
    def test_make_new_payment(self):
        """Test if payment will be successfully processed if all data provided correctly """
        res = self.client().post('/payment', json=self.new_payment)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[ 'success' ], True)
        self.assertEqual(data[ 'message' ], 'Payment is processed')

    # test post a new payment to database(gateway) with no security code is valid
    def test_make_new_payment_no_security_code(self):
        """Test if payment will be successfully processed if all data provided correctly but no security code """
        res = self.client().post('/payment', json=self.no_security_code)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[ 'success' ], True)
        self.assertEqual(data[ 'message' ], 'Payment is processed')

    # test error while making a new payment with invalid credit card number
    def test_error_make_payment_invalid_card_number(self):
        """Test if error 400 will be raised if invalid credit card number is provided """
        res = self.client().post('/payment', json=self.invalid_card_number)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data[ 'success' ], False)
        self.assertEqual(data[ 'message' ],'Bad Request!!!! Please make sure the data you entered is correct')

    # test error while making a new payment with no card holder sent
    def test_error_make_payment_no_card_holder(self):
        """Test if error 400 will be raised if card holder is not sent """
        res = self.client().post('/payment', json=self.no_card_holder)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data[ 'success' ], False)
        self.assertEqual(data[ 'message' ], 'Bad Request!!!! Please make sure the data you entered is correct')

    # test error while making a new payment with expired credit card number
    def test_error_make_payment_expired_credit_card(self):
        """Test if error 400 will be raised if expired credit card is provided """
        res = self.client().post('/payment', json=self.expired_card)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data[ 'success' ], False)
        self.assertEqual(data[ 'message' ], 'Bad Request!!!! Please make sure the data you entered is correct')

    # test error while making a new payment with invalid credit card payment amount
    def test_error_make_payment_invalid_amount(self):
        """Test if error 400 will be raised if invalid payment amount is provided """
        res = self.client().post('/payment', json=self.invalid_amount)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data[ 'success' ], False)
        self.assertEqual(data[ 'message' ], 'Bad Request!!!! Please make sure the data you entered is correct')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
