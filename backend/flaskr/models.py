import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

# TODO: Add enum to limit question difficulty to be 1-4


# Database configuration
postgres_user = os.environ.get("POSTGRES_USER", "postgres")
postgres_pw = os.environ.get("POSTGRES_PW", "password")
database_name = "trivia"
database_path = (
    f"postgres://{postgres_user}:{postgres_pw}@localhost:5432/{database_name}"
)
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    return db


class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    difficulty = Column(Integer)

    def __init__(self, question, answer, category_id, difficulty):
        self.question = question
        self.answer = answer
        self.category_id = category_id
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "category": self._get_category(),
            "difficulty": self.difficulty,
        }

    def _get_category(self):
        category = Category.query.filter_by(id=self.category_id).one()
        return category.format()


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    questions = db.relationship("Question", backref="questions", lazy=True)

    def __init__(self, type):
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        return {"id": self.id, "type": self.type}
