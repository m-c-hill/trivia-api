# Trivyah (Trivia App)

The Trivyah project is a simple trivia game where users can test their knowledge by answering questions for a range of topics including Science, Geography, Sports and Art.

The project involved designing, writing and implementing the backend REST API and its accompanying test suite to provide the data consumed by the provided React frontend.

See below a brief demonstration of the Trivyah application:

https://user-images.githubusercontent.com/74383191/182891342-edab5f01-d883-4a22-9231-5f0fb7113bdc.mp4

Requirements for the functionality of the API were as follows. Users must be able to:

- View all categories
- View questions, including the question category, difficulty rating and answer
- Delete questions
- Filter questions by catgegory
- Search for questions based on a text query string
- Add their own questions to the game by submitting the question, answer, difficulty and category
- Play the quiz game, which will provide a random selection of questions from either the entire question bank or a category of the player's choice

The project was created as the final project for the API Development and Documentation module of [Udacity's Full Stack Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).

## Getting Started

### Installing Dependencies

#### Frontend Dependencies

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, download and install Node from [https://nodejs.com/en/download](https://nodejs.org/en/download/)

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run: `npm install`

#### Backend Dependencies

1. Developers are expected to have Python3 and pip installed
2. Create a new virtual environment `python3 -m venv venv` and activate: `source venv/bin/activate`
3. Install all dependencies: `pip install -r requirements.txt`

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file. From the `backend` directory, run:

```bash
psql trivia < trivia.psql
```

### Running the Server

From the `backend` directory, run the following:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Running the Frontend

The frontend app was built using create-react-app. In order to run the app in development mode, in the `frontend` directory run:

```bash
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

### Testing

[Pytest](https://docs.pytest.org/en/7.1.x/contents.html) was used as the testing framework for the endpoint tests in this project.

Install Pytest in your virtual environment using pip:

```bash
pip install pytest
```

To deploy the tests, run:

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
pytest
```

Note: the `dropdb` can be omitted when running the tests for the first time.

## API Reference

### Getting Started

- **Base URL**: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
- **Authentication**: This version does not require authentication or API keys.

### Endpoints

#### Categories

**GET /categories**

- Returns a complete list of categories.

- Example: `curl http://127.0.0.1:5000/categories`

```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categories": 6
}
```

**GET /categories/${category_id}/quesitons**

- Returns all questions under a specific category.

- Example: `curl http://127.0.0.1:5000/categories/1/questions`

```
{
    "category": {
        "id": 1,
        "type": "Science"
    },
    "questions": [
        {
            "answer": "The Liver",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 3
}
```

#### Questions

**GET /questions**

- Returns questions, paginated in groups of 10, and the total number of questions currently being stored in the application database.

- Example: `curl http://127.0.0.1:5000/questions`

```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "category:": {
        "id": 0,
        "type": "All"
    },
    "questions": [
        {
            "answer": "Apollo 13",
            "category": {
                "id": 5,
                "type": "Entertainment"
            },
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": {
                "id": 5,
                "type": "Entertainment"
            },
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": {
                "id": 4,
                "type": "History"
            },
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": {
                "id": 5,
                "type": "Entertainment"
            },
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": {
                "id": 4,
                "type": "History"
            },
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": {
                "id": 6,
                "type": "Sports"
            },
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": {
                "id": 6,
                "type": "Sports"
            },
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": {
                "id": 4,
                "type": "History"
            },
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": {
                "id": 3,
                "type": "Geography"
            },
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": {
                "id": 3,
                "type": "Geography"
            },
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 19
}
```

**GET /questions/${question_id}**

- Returns a specific question by ID.

- Example: `curl http://127.0.0.1:5000/questions/15`

```
{
    "question": {
        "answer": "Agra",
        "category": {
            "id": 3,
            "type": "Geography"
        },
        "difficulty": 2,
        "id": 15,
        "question": "The Taj Mahal is located in which Indian city?"
    },
    "success": true,
    "total_questions": 19
}
```

**POST /questions**

- Sends a post request to create a new question by providing question text, answer, difficulty and category in the request body.
- If successful, a JSON object with the newly created question is returned, as well as paginated questions.
- Example: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Who wrote Kafka On The Shore?", "category_id": 2, "difficulty": 3, "answer": "Haruki Murakami"}'`

```
{
    "created": 33,
    "questions": [
        {
            "answer": "Agra",
            "category": {
                "id": 3,
                "type": "Geography"
            },
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "The Liver",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "Scarab",
            "category": {
                "id": 4,
                "type": "History"
            },
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
            "answer": "Haruki Murakami",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 3,
            "id": 33,
            "question": "Who wrote Kafka On The Shore?"
        }
    ],
    "success": true
}
```

**DELETE /questions/${question_id}**

- Deletes a question with corresponding question id provided in the

- Example: `curl http://127.0.0.1:5000/questions/33 -X DELETE`

```
{
    "deleted": 33,
    "questions": [
        {
            "answer": "Agra",
            "category": {
                "id": 3,
                "type": "Geography"
            },
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": {
                "id": 2,
                "type": "Art"
            },
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "The Liver",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": {
                "id": 1,
                "type": "Science"
            },
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "Scarab",
            "category": {
                "id": 4,
                "type": "History"
            },
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "total_questions": 19
}
```

#### Search

**POST /search**

Returns search results with paginataed questions matching a provivded search term in JSON request parameters.

Example: `curl http://127.0.0.1:5000/search -X POST -H "Content-Type: application/json" -d '{"search_term": "country"}'

```
{
    "questions": [
        {
            "answer": "Uruguay",
            "category": {
                "id": 6,
                "type": "Sports"
            },
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        }
    ],
    "search_term": "country",
    "success": true,
    "total_results": 1
}
```

#### Quiz

**POST /quiz**

Allows users to play the game by returning a random, unplayed question. It uses request parameters of `previous_question_ids` and `category` to return questions that have not yet been played and are in the player's chosen category.

Example: `curl http://127.0.0.1:5000/quiz -X POST -H "Content-Type: application/json" -d '{"previous_question_ids": [2, 5, 14], "category": {"id": 3, "type": "Geography"}}'`

```
{
    "category_id": 3,
    "previous_question_ids": [
        2,
        5,
        14,
        15
    ],
    "question": {
        "answer": "Agra",
        "category": {
            "id": 3,
            "type": "Geography"
        },
        "difficulty": 2,
        "id": 15,
        "question": "The Taj Mahal is located in which Indian city?"
    },
    "success": true,
    "total_questions_in_category": 3
}
```

### Error Handling

Errors are returned as JSON in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The API returns three types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
