from flask import Blueprint, jsonify, abort, request, make_response, json
from api.models.questions import Question, my_questions
from api.controllers.validators import is_valid

appblueprint = Blueprint('api',__name__)

@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to StackOverflow</h1>"

@appblueprint.route('/questions', methods = ['GET'])
def getQuestions():
    return jsonify({"Questions":my_questions.questionList})
