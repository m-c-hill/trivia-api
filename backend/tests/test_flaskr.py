import pytest

from backend.flaskr import create_app
from backend.flaskr.models import Category, Question, setup_db
from backend.tests.data.test_data import (
    all_questions,
    dummy_categories,
    dummy_questions,
)

# =======================================
#  Fixtures - Test Client and Dummy Data
# =======================================


@pytest.fixture()
def client():
    app = create_app()
    database_path = "postgres://postgres:password@localhost:5432/trivia_test"  # TODO
    db = setup_db(app, database_path)
    insert_dummy_data()  # Populate database with test data
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
def all_questions_page_one():
    return all_questions[0:10]


@pytest.fixture()
def all_questions_page_two():
    return all_questions[10:]


@pytest.fixture()
def all_questions_in_science_category():
    return [
        question
        for question in all_questions
        if question["category"]["type"] == "Science"
    ]


@pytest.fixture()
def question_one():
    return all_questions[0]


@pytest.fixture()
def new_question():
    return {
        "question": "Who is the author of Norwegian Wood?",
        "answer": "Haruki Murakami",
        "category_id": 2,
        "difficulty": 2,
    }


@pytest.fixture()
def new_question_response():
    return {
        "answer": "Haruki Murakami",
        "category": {"id": 2, "type": "Art"},
        "difficulty": 2,
        "id": 19,
        "question": "Who is the author of Norwegian Wood?",
    }


@pytest.fixture()
def search_results():
    return {
        "answer": "Uruguay",
        "category": {"id": 6, "type": "Sports"},
        "difficulty": 4,
        "id": 7,
        "question": "Which country won the first ever soccer World Cup in 1930?",
    }


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


@pytest.fixture()
def error_not_found():
    return {"error": 404, "message": "Not found", "success": False}


# ====================================
#  Category Endpoint Tests
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


def test_all_questions(client, all_questions_page_one):
    response = client.get("/questions")
    body = response.get_json()

    assert response.status_code == 200
    assert body["questions"] == all_questions_page_one
    assert body["success"] == True
    assert body["total_questions"] == len(all_questions)


def test_all_questions_pagination(client, all_questions_page_two):
    response = client.get("/questions", query_string={"page": 2})
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["questions"] == all_questions_page_two
    assert body["total_questions"] == len(all_questions)


def test_all_questions_none_found(client, error_not_found):
    Question.query.delete()
    response = client.get("/questions")
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


def test_get_question_by_id(client, question_one):
    response = client.get(f"/questions/1")
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["question"] == question_one
    assert body["total_questions"] == len(all_questions)


def test_create_new_question(client, new_question, new_question_response):
    response = client.post("/questions", json=new_question)
    body = response.get_json()

    new_question_id = body["created"]
    assert response.status_code == 201

    response = client.get(f"/questions/{new_question_id}")
    body = response.get_json()

    assert body["success"] == True
    assert body["question"] == new_question_response
    assert body["total_questions"] == len(all_questions) + 1


def test_delete_question(client, error_not_found):
    response = client.delete("/questions/1")
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["deleted"] == 1
    assert body["total_questions"] == len(all_questions) - 1

    response = client.get(f"/questions/1")
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


def test_delete_question_invalid_id(client, error_not_found):
    response = client.delete("/questions/100")
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


# ====================================
#  Search Endpoint Tests
# ====================================


def test_search_for_question(client, search_results):
    search_term = "country"
    response = client.post("/search", json={"search_term": search_term})
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["questions"] == [search_results]
    assert body["total_results"] == 1
    assert body["search_term"] == search_term


def test_search_for_question_empty_search_term(client):
    response = client.post("/search")
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["questions"] == all_questions
    assert body["total_results"] == 18
    assert body["search_term"] == ""


def test_search_for_question_no_results(client):
    search_term = "zelda"
    response = client.post("/search", json={"search_term": search_term})
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["questions"] == []
    assert body["total_results"] == 0
    assert body["search_term"] == "zelda"


# ====================================
#  Quiz Endpoint Tests
# ====================================


def test_play_quiz_category_chosen(client, play_quiz_response):
    response = client.post(
        "/quiz",
        json={"category": {"type": "science", "id": 1}, "previous_question_ids": [17]},
    )
    body = response.get_json()

    assert response.status_code == 200
    assert body["success"] == True
    assert body["category_id"] == 1
    assert body["previous_question_ids"] == play_quiz_response["previous_question_ids"]
    assert body["question"] == play_quiz_response["question"]


def test_play_quiz_invalid_category(client, error_not_found):
    response = client.post(
        "/quiz",
        json={"category": {"type": "physics", "id": 7}, "previous_question_ids": [17]},
    )
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]


def test_play_quiz_no_questions_remaining(client, error_not_found):
    response = client.post(
        "/quiz",
        json={
            "category": {"type": "science", "id": 1},
            "previous_question_ids": [16, 17],
        },
    )
    body = response.get_json()

    assert response.status_code == 404
    assert body["error"] == 404
    assert body["success"] == False
    assert body["message"] == error_not_found["message"]
