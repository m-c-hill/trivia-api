import os
from unicodedata import category
import unittest
from numpy import insert
import pytest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from test_data import dummy_questions, dummy_categories


# =======================================
#  Fixtures - Test Client and Dummy Data
# =======================================


@pytest.fixture()
def client():
    app = create_app()
    database_path = "postgres://postgres:password@localhost:5432/trivia_test"
    db = setup_db(app, database_path)
    insert_dummy_data()
    yield app.test_client()
    db.drop_all()


def insert_dummy_data() -> None:
    """Helper function to insert dummy records into the test database"""
    for category in dummy_categories:
        new_category = Category(**category)
        new_category.insert()

    for question in dummy_questions:
        new_question = Question(**question)
        new_question.insert()


# =============================
#  Fixtures - Expected Results
# =============================


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


@pytest.fixture()
def all_questions():
    return


@pytest.fixture()
def all_questions_in_science_category():
    return [
        {
            "answer": "The Liver",
            "category": {"id": 1, "type": "Science"},
            "difficulty": 4,
            "id": 16,
            "question": "What is the heaviest organ in the human body?",
        },
        {
            "answer": "Alexander Fleming",
            "category": {"id": 1, "type": "Science"},
            "difficulty": 3,
            "id": 17,
            "question": "Who discovered penicillin?",
        },
    ]


@pytest.fixture()
def error_not_found():
    return {"error": 404, "message": "Not found", "success": False}


@pytest.fixture()
def play_quiz_response():
    return {
        "category_id": 1,
        "previous_question_ids": [17, 16],
        "question": {
            "answer": "The Liver",
            "category": {"id": 1, "type": "Science"},
            "difficulty": 4,
            "id": 16,
            "question": "What is the heaviest organ in the human body?",
        },
        "success": True,
    }


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


def test_all_categories_none_found(client, error_not_found):
    Question.query.delete()
    Category.query.delete()
    response = client.get("/categories")
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


def test_get_questions_for_category(client, all_questions_in_science_category):
    response = client.get("/categories/1/questions")
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["questions"] == all_questions_in_science_category
    assert body["total_questions"] == len(all_questions_in_science_category)
    assert body["category"] == {"id": 1, "type": "Science"}


def test_no_questions_found_for_category(client, error_not_found):
    Question.query.filter_by(category_id=1).delete()
    response = client.get("/categories/1/questions")
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


# ====================================
#  Question Endpoint Tests
# ====================================

@pytest.mark.skip(reason="Test needs to be written")
def test_all_questions(client, all_questions_page_one):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_all_questions_pagination(client, all_questions_page_two):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_all_questions_none_found(client, error_not_found):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_create_new_question(client, new_question_created_response):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_create_new_question_invalid_category(client, error_unprocessable):
    assert True


@pytest.mark.skip(reason="Feature not yet implemented")
def test_create_new_question_invalid_difficulty(client, error_unprocessable):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_delete_question(client, question_deleted_response):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_delete_question_invalid_id(client, error_unprocessable):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_search_for_question(client, search_results):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_search_for_question_empty_search_term(
    client, search_results_empty_search_term
):
    assert True

@pytest.mark.skip(reason="Test needs to be written")
def test_search_for_question_no_results(client):
    assert True


# ====================================
#  Quiz Endpoint Tests
# ====================================


def test_play_quiz_category_chosen(client, play_quiz_response):
    response = client.post(
        "/quiz", json={"category_id": 1, "previous_question_ids": [17]}
    )
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["category_id"] == 1
    assert body["previous_question_ids"] == play_quiz_response["previous_question_ids"]
    assert body["question"] == play_quiz_response["question"]


def test_play_quiz_invalid_category(client, error_not_found):
    response = client.post(
        "/quiz", json={"category_id": 7, "previous_question_ids": [17]}
    )
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


def test_play_quiz_no_questions_remaining(client, error_not_found):
    response = client.post(
        "/quiz", json={"category_id": 1, "previous_question_ids": [16, 17]}
    )
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]
