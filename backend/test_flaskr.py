import os
import unittest
import pytest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from test_data import dummy_questions, dummy_categories


# ====================================
#  Fixtures
# ====================================


@pytest.fixture()
def client():
    app = create_app()
    database_path = "postgres://postgres:password@localhost:5432/trivia_test"
    db = setup_db(app, database_path)
    insert_dummy_data()
    yield app.test_client()
    db.drop_all()

@pytest.fixture()
def all_categories():
    return {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports",
    }


def insert_dummy_data() -> None:
    """Helper function to insert dummy records into the test database"""
    for category in dummy_categories:
        new_category = Category(**category)
        new_category.insert()

    for question in dummy_questions:
        new_question = Question(**question)
        new_question.insert()


# ====================================
#  Category Enpoint Tests
# ====================================


def test_all_categories(client, all_categories):
    response = client.get("/categories")
    body = response.get_json()
    assert response.status_code == 200
    assert body["categories"] == all_categories
    assert body["success"] == True
    assert body["total_categories"] == len(all_categories)


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
