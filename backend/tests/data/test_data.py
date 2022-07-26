# ===================================
#  Data to be inserted into database
# ===================================

dummy_categories = [
    {"type": "Science"},
    {"type": "Art"},
    {"type": "Geography"},
    {"type": "History"},
    {"type": "Entertainment"},
    {"type": "Sports"},
]

dummy_questions = [
    {
        "answer": "Apollo 13",
        "category_id": 5,
        "difficulty": 4,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
    },
    {
        "answer": "Tom Cruise",
        "category_id": 5,
        "difficulty": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
    },
    {
        "answer": "Maya Angelou",
        "category_id": 4,
        "difficulty": 2,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
    },
    {
        "answer": "Edward Scissorhands",
        "category_id": 5,
        "difficulty": 3,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
    },
    {
        "answer": "Muhammad Ali",
        "category_id": 4,
        "difficulty": 1,
        "question": "What boxer's original name is Cassius Clay?",
    },
    {
        "answer": "Brazil",
        "category_id": 6,
        "difficulty": 3,
        "question": "Which is the only team to play in every soccer World Cup tournament?",
    },
    {
        "answer": "Uruguay",
        "category_id": 6,
        "difficulty": 4,
        "question": "Which country won the first ever soccer World Cup in 1930?",
    },
    {
        "answer": "George Washington Carver",
        "category_id": 4,
        "difficulty": 2,
        "question": "Who invented Peanut Butter?",
    },
    {
        "answer": "Lake Victoria",
        "category_id": 3,
        "difficulty": 2,
        "question": "What is the largest lake in Africa?",
    },
    {
        "answer": "The Palace of Versailles",
        "category_id": 3,
        "difficulty": 3,
        "question": "In which royal palace would you find the Hall of Mirrors?",
    },
    {
        "answer": "Agra",
        "category_id": 3,
        "difficulty": 2,
        "question": "The Taj Mahal is located in which Indian city?",
    },
    {
        "answer": "Escher",
        "category_id": 2,
        "difficulty": 1,
        "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?",
    },
    {
        "answer": "Mona Lisa",
        "category_id": 2,
        "difficulty": 3,
        "question": "La Giaconda is better known as what?",
    },
    {
        "answer": "One",
        "category_id": 2,
        "difficulty": 4,
        "question": "How many paintings did Van Gogh sell in his lifetime?",
    },
    {
        "answer": "Jackson Pollock",
        "category_id": 2,
        "difficulty": 2,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
    },
    {
        "answer": "The Liver",
        "category_id": 1,
        "difficulty": 4,
        "question": "What is the heaviest organ in the human body?",
    },
    {
        "answer": "Alexander Fleming",
        "category_id": 1,
        "difficulty": 3,
        "question": "Who discovered penicillin?",
    },
    {
        "answer": "Edinburgh",
        "category_id": 3,
        "difficulty": 1,
        "question": "What is the capital of Scotland?",
    },
]


# ============================================
#  Expected endpoint responses for dummy data
# ============================================


all_questions = [
    {
        "answer": "Apollo 13",
        "category": {"id": 5, "type": "Entertainment"},
        "difficulty": 4,
        "id": 1,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
    },
    {
        "answer": "Tom Cruise",
        "category": {"id": 5, "type": "Entertainment"},
        "difficulty": 4,
        "id": 2,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
    },
    {
        "answer": "Maya Angelou",
        "category": {"id": 4, "type": "History"},
        "difficulty": 2,
        "id": 3,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
    },
    {
        "answer": "Edward Scissorhands",
        "category": {"id": 5, "type": "Entertainment"},
        "difficulty": 3,
        "id": 4,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
    },
    {
        "answer": "Muhammad Ali",
        "category": {"id": 4, "type": "History"},
        "difficulty": 1,
        "id": 5,
        "question": "What boxer's original name is Cassius Clay?",
    },
    {
        "answer": "Brazil",
        "category": {"id": 6, "type": "Sports"},
        "difficulty": 3,
        "id": 6,
        "question": "Which is the only team to play in every soccer World Cup tournament?",
    },
    {
        "answer": "Uruguay",
        "category": {"id": 6, "type": "Sports"},
        "difficulty": 4,
        "id": 7,
        "question": "Which country won the first ever soccer World Cup in 1930?",
    },
    {
        "answer": "George Washington Carver",
        "category": {"id": 4, "type": "History"},
        "difficulty": 2,
        "id": 8,
        "question": "Who invented Peanut Butter?",
    },
    {
        "answer": "Lake Victoria",
        "category": {"id": 3, "type": "Geography"},
        "difficulty": 2,
        "id": 9,
        "question": "What is the largest lake in Africa?",
    },
    {
        "answer": "The Palace of Versailles",
        "category": {"id": 3, "type": "Geography"},
        "difficulty": 3,
        "id": 10,
        "question": "In which royal palace would you find the Hall of Mirrors?",
    },
    {
        "answer": "Agra",
        "category": {"id": 3, "type": "Geography"},
        "difficulty": 2,
        "id": 11,
        "question": "The Taj Mahal is located in which Indian city?",
    },
    {
        "answer": "Escher",
        "category": {"id": 2, "type": "Art"},
        "difficulty": 1,
        "id": 12,
        "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?",
    },
    {
        "answer": "Mona Lisa",
        "category": {"id": 2, "type": "Art"},
        "difficulty": 3,
        "id": 13,
        "question": "La Giaconda is better known as what?",
    },
    {
        "answer": "One",
        "category": {"id": 2, "type": "Art"},
        "difficulty": 4,
        "id": 14,
        "question": "How many paintings did Van Gogh sell in his lifetime?",
    },
    {
        "answer": "Jackson Pollock",
        "category": {"id": 2, "type": "Art"},
        "difficulty": 2,
        "id": 15,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
    },
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
    {
        "answer": "Edinburgh",
        "category": {"id": 3, "type": "Geography"},
        "difficulty": 1,
        "id": 18,
        "question": "What is the capital of Scotland?",
    },
]
