import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()


# ====================================
#  Fixtures
# ====================================



# ====================================
#  Category Enpoint Tests
# ====================================

def test_all_categories():
    pass

def test_all_categories_none_found():
    pass

def test_get_questions_for_category():
    pass

def test_no_questions_found_for_category():
    pass

# ====================================
#  Question Endpoint Tests
# ====================================

def test_all_questions():
    pass

def test_all_questions_none_found():
    pass

def test_create_new_question():
    pass

def test_create_new_question_invalid_category():
    pass

def test_create_new_question_invalid_difficulty():
    pass

def test_delete_question():
    pass

def test_delete_question_invalid_id():
    pass

def test_search_for_question():
    pass

def test_search_for_question_empty_search_term():
    pass

def test_search_for_question_no_results():
    pass


# ====================================
#  Quiz Endpoint Tests
# ====================================

def test_play_quiz_category_chosen():
    pass

def test_play_quiz_no_category_chosen():
    pass

def test_play_quiz_invalid_category():
    pass

def test_play_quiz_no_questions_remaining():
    pass
