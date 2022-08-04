# Trivyah (Trivia App)

## Overview

- Introduction and

https://user-images.githubusercontent.com/74383191/182891342-edab5f01-d883-4a22-9231-5f0fb7113bdc.mp4

## App Features

#### View Questions

#### Question Categories

#### Search for Questions

#### Submit New Questions

#### Gameplay

## Structure

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server.

> View the [Backend README](./backend/README.md) for more details and API Documentation.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.
