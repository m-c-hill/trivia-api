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


# TEST: At this point, when you start the application
# you should see questions and categories generated,
# ten questions per page and pagination at the bottom of the screen for three pages.
# Clicking on the page numbers should update the questions.

# TEST: When you submit a question on the "Add" tab,
# the form will clear and the question will appear at the end of the last page
# of the questions list in the "List" tab.

# TEST: Search by any phrase. The questions list will update to include
# only question that include that string within their question.
# Try using the word "title" to start.

# TEST: In the "List" tab / main screen, clicking on one of the
# categories in the left column will cause only questions of that
# category to be shown.

# TEST: In the "Play" tab, after a user selects "All" or a category,
# one question at a time is displayed, the user is allowed to answer
# and shown whether they were correct or not.
