from random import randint
from typing import List

from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from backend.flaskr.models import Category, Question, db, setup_db

QUESTIONS_PER_PAGE = 10


def paginate_questions(request: request, questions: List[Question]):
    """
    Return paginated list of questions from users requested page number.
    """
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_questions = [question.format() for question in questions]

    return formatted_questions[start:end]


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={"*": {"origins": "*"}})  # "*/api/*"
    db.create_all()
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        """
        When a request is received, run this method to add additional CORS headers to the response.
        """
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    # ====================================
    #  Category endpoints
    # ====================================

    @app.route("/categories")
    def retrieve_all_categories():
        categories = Category.query.order_by(Category.id).all()
        formatted_categories = {category.id: category.type for category in categories}

        if len(formatted_categories) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "categories": formatted_categories,
                "total_categories": len(formatted_categories),
            }
        )

    @app.route("/categories/<int:category_id>/questions")
    def questions_in_category(category_id):
        category = Category.query.filter_by(id=category_id).one_or_none()
        if category is None:
            abort(404)

        questions = Question.query.filter_by(category_id=category_id).all()
        if not questions:
            abort(404)

        formatted_questions = [question.format() for question in questions]

        return jsonify(
            {
                "success": True,
                "category": category.format(),
                "questions": formatted_questions,
                "total_questions": len(formatted_questions),
            }
        )

    # ====================================
    #  Question endpoints
    # ====================================

    @app.route("/questions")
    def retrieve_all_questions():
        questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, questions)
        categories = Category.query.order_by(Category.type).all()

        if len(current_questions) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(questions),
                "categories": {category.id: category.type for category in categories},
                "current_category:": None,
            }
        )

    @app.route("/questions/<int:question_id>")
    def retrieve_question_by_id(question_id):
        question = Question.query.filter_by(id=question_id).one_or_none()

        if question is None:
            abort(404)

        return jsonify(
            {
                "success": True,
                "question": question.format(),
                "total_questions": len(Question.query.all()),
            }
        )

    @app.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()
        if body.get("difficulty") < 1 or body.get("difficulty") > 4:
            # Difficulty must be in range 1-4
            abort(422)

        try:
            question = Question(
                question=body.get("question"),
                answer=body.get("answer"),
                category_id=body.get("category_id"),
                difficulty=body.get("difficulty"),
            )

            question.insert()

            all_questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, all_questions)

            return (
                jsonify(
                    {
                        "success": True,
                        "created": question.id,
                        "questions": current_questions,
                    }
                ),
                201,
            )

        except:
            abort(422)

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        question = Question.query.filter_by(id=question_id).one_or_none()
        if question is None:
            abort(404)

        try:
            question.delete()

            all_questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, all_questions)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "total_questions": len(all_questions),
                }
            )

        except:
            abort(422)

    # ====================================
    #  Search endpoint
    # ====================================

    @app.route("/search", methods=["POST"])
    def search_questions():
        try:
            search_term = request.get_json().get("search_term", "")
        except AttributeError:
            search_term = ""

        search_results = Question.query.filter(
            Question.question.ilike(f"%{search_term}%")
        ).all()
        questions = [question.format() for question in search_results]

        return jsonify(
            {
                "success": True,
                "search_term": search_term,
                "questions": questions,
                "total_results": len(questions),
            }
        )

    # ====================================
    #  Play quiz endpoint
    # ====================================

    @app.route("/quiz", methods=["POST"])
    def quiz():
        body = request.get_json()
        category_id = body.get("category")["id"]
        previous_question_ids = body.get("previous_question_ids", [])

        try:
            if category_id == 0:
                all_questions = Question.query.all()
            else:
                all_questions = Question.query.filter_by(category_id=category_id).all()

            all_question_ids = [question.id for question in all_questions]
            remaining_question_ids = [
                id for id in all_question_ids if id not in previous_question_ids
            ]

            random_index = randint(0, len(remaining_question_ids) - 1)
            chosen_question_id = remaining_question_ids[random_index]
            previous_question_ids.append(chosen_question_id)
            chosen_question = Question.query.filter_by(id=chosen_question_id).first()

            return jsonify(
                {
                    "success": True,
                    "previous_question_ids": previous_question_ids,
                    "question": chosen_question.format(),
                    "category_id": category_id,
                }
            )

        except:
            abort(404)

    # ====================================
    #  Error handlers
    # ====================================

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Not found"}), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    return app
