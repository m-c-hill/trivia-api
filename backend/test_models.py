from models import Question, Category


def test_new_question():
    question = Question(
        question="What is the capital of Angola?",
        answer="Luanda",
        category_id=2,
        difficulty=3,
    )

    assert question.question == "What is the capital of Angola?"
    assert question.answer == "Luanda"
    assert question.category_id == 2
    assert question.difficulty == 3


def test_new_category():
    category = Category(type="Physics")

    assert category.type == "Physics"
