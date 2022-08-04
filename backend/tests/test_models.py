import pytest

from backend.flaskr.models import Category, Question


@pytest.fixture()
def new_question():
    return {
        "question": "What is the capital of Angola?",
        "answer": "Luanda",
        "category_id": 2,
        "difficulty": 3,
    }


def test_new_question(new_question):
    question = Question(**new_question)

    assert question.question == new_question["question"]
    assert question.answer == new_question["answer"]
    assert question.category_id == new_question["category_id"]
    assert question.difficulty == new_question["difficulty"]


def test_new_category():
    category = Category(type="Physics")

    assert category.type == "Physics"
