import React, { Component } from "react";
import $ from "jquery";
import "../stylesheets/QuizView.css";

const defaultQuestionsPerPlay = 5;

class QuizView extends Component {
  constructor(props) {
    super();
    this.state = {
      quizCategory: null,
      previousQuestionIDs: [],
      showAnswer: false,
      categories: {},
      numCorrect: 0,
      currentQuestion: {},
      guess: "",
      forceEnd: false,
      questionsPerPlay: defaultQuestionsPerPlay, // Default set to 5
    };
  }

  componentDidMount() {
    $.ajax({
      url: `/categories`,
      type: "GET",
      success: (result) => {
        this.setState({ categories: result.categories });
        return;
      },
      error: (error) => {
        alert("Unable to load categories. Please try your request again");
        return;
      },
    });
  }

  selectCategory = ({ type, id = 0 }) => {
    this.setState(
      {
        quizCategory: { type, id },
      },
      this.getNextQuestion
    );
  };

  getQuestionsPerPlay = (category_id) => {
    $.ajax({
      url: `/categories/${category_id}/questions`,
      type: "GET",
      success: (result) => {
        this.setState({
          questionsPerPlay: Math.min(
            result.total_questions,
            defaultQuestionsPerPlay
          ),
        });
        return;
      },
      error: (error) => {
        alert("Unable to load categories. Please try your request again");
        return;
      },
    });
  };

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };

  getNextQuestion = () => {
    this.getQuestionsPerPlay(this.state.quizCategory.id);
    const previousQuestionIDs = [...this.state.previousQuestionIDs];

    if (this.state.currentQuestion.id) {
      previousQuestionIDs.push(this.state.currentQuestion.id);
    }

    if (this.isFinalQuestion()) {
      this.setState({ forceEnd: true });
      return;
    }

    $.ajax({
      url: "/quiz",
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      data: JSON.stringify({
        previous_question_ids: previousQuestionIDs,
        category: this.state.quizCategory,
      }),
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          showAnswer: false,
          previousQuestionIDs: previousQuestionIDs,
          currentQuestion: result.question,
          guess: "",
          forceEnd: result.question ? false : true,
          numOfQuestionsInCategory: result.previous_question_ids,
        });
        return;
      },
      error: (error) => {
        //alert("Unable to load question. Please try your request again");
        return;
      },
    });
  };

  submitGuess = (event) => {
    event.preventDefault();
    let evaluate = this.evaluateAnswer();
    this.setState({
      numCorrect: !evaluate ? this.state.numCorrect : this.state.numCorrect + 1,
      showAnswer: true,
    });
  };

  restartGame = () => {
    this.setState({
      quizCategory: null,
      previousQuestionIDs: [],
      showAnswer: false,
      numCorrect: 0,
      currentQuestion: {},
      guess: "",
      forceEnd: false,
    });
  };

  renderPrePlay() {
    return (
      <div className="quiz-play-holder">
        <div className="choose-header">Choose Category</div>
        <div className="category-holder">
          <div className="play-category" onClick={this.selectCategory}>
            ALL
          </div>
          {Object.keys(this.state.categories).map((id) => {
            return (
              <div
                key={id}
                value={id}
                className="play-category"
                onClick={() =>
                  this.selectCategory({ type: this.state.categories[id], id })
                }
              >
                {this.state.categories[id].toUpperCase()}
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  renderFinalScore() {
    return (
      <div className="quiz-play-holder">
        <div className="final-header">Final Score: {this.state.numCorrect}</div>
        <div className="play-again button" onClick={this.restartGame}>
          Play Again?
        </div>
      </div>
    );
  }

  evaluateAnswer = () => {
    const formatGuess = this.state.guess
      // eslint-disable-next-line
      .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "")
      .toLowerCase();
    const answerArray = this.state.currentQuestion.answer
      .toLowerCase()
      .split(" ");
    return answerArray.every((el) => formatGuess.includes(el));
  };

  isFinalQuestion = () => {
    return (
      this.state.questionsPerPlay === this.state.previousQuestionIDs.length + 1
    );
  };

  renderCorrectAnswer() {
    let evaluate = this.evaluateAnswer();
    let finalQuestion = this.isFinalQuestion();
    return (
      <div className="quiz-play-holder">
        <div className="quiz-counter">
          Question: {this.state.previousQuestionIDs.length + 1}/
          {this.state.questionsPerPlay}
        </div>
        <div className="quiz-question">
          {this.state.currentQuestion.question}
        </div>
        <div className={`${evaluate ? "correct" : "wrong"}`}>
          {evaluate ? "You were correct!" : "You were incorrect"}
        </div>
        <div className="quiz-answer">{this.state.currentQuestion.answer}</div>
        <div className="next-question button" onClick={this.getNextQuestion}>
          {" "}
          {finalQuestion ? "Get Results" : "Next Question"}
        </div>
      </div>
    );
  }

  renderPlay() {
    return this.state.previousQuestionIDs.length ===
      this.state.questionsPerPlay || this.state.forceEnd ? (
      this.renderFinalScore()
    ) : this.state.showAnswer ? (
      this.renderCorrectAnswer()
    ) : (
      <div className="quiz-play-holder">
        <div className="quiz-counter">
          Question: {this.state.previousQuestionIDs.length + 1}/
          {this.state.questionsPerPlay}
        </div>
        <div className="quiz-question">
          {this.state.currentQuestion.question}
        </div>
        <form onSubmit={this.submitGuess}>
          <input
            className="input-box"
            type="text"
            name="guess"
            onChange={this.handleChange}
          />
          <input
            className="submit-guess button"
            type="submit"
            value="Submit Answer"
          />
        </form>
      </div>
    );
  }

  render() {
    return this.state.quizCategory ? this.renderPlay() : this.renderPrePlay();
  }
}

export default QuizView;
