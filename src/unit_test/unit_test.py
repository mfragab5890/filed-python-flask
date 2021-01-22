import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from src.app import create_app
from src.models.models import *


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'trivia_test'
        setup_db(self.app, self.database_name)

        self.new_question = {
            'question': 'who won the us elections 2020?',
            'answer': 'Joe Biden',
            'difficulty': 3,
            'category': 4
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

    # test post a new question to database
    def test_add_user_question(self):
        """Test if user add a question it will be added successfully """
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[ 'success' ], True)
        self.assertTrue(data[ 'created' ])
        self.assertTrue(len(data[ 'questions' ]))
        self.assertTrue(data[ 'total_questions' ])

    # test error while posting a new question to database with missing data
    def test_error_add_user_question(self):
        """Test if user if error will occur on user submit wrong data """
        res = self.client().post('/questions', json=self.new_question_2)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data[ 'success' ], False)
        self.assertEqual(data[ 'message' ],
                         'Unprocessable!!! : The request was well-formed but was unable to be followed')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
