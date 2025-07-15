# flow.py
import sys
import os

# Add the directory that contains the 'pocketflow' module
sys.path.append(os.path.join(os.path.dirname(__file__), 'pocketflow'))
from pocketflow import Flow
# or use absolute path
from nodes import (GetQuestionNode, AnswerNode)


def create_qa_flow():
    get_question = GetQuestionNode()
    answer = AnswerNode()

    class ManualFlow(Flow):
        def run(self, shared):
            question = get_question._run(shared)
            answer.set_params({"_input": question})  # ← MUST use "_input"
            shared["AnswerNode"] = answer._run(shared)

    return ManualFlow()

# def create_qa_flow():
#     get_question = GetQuestionNode()
#     answer = AnswerNode()
#     get_question >> answer  # This connects the output of GetQuestionNode to AnswerNode
#     return Flow(start=get_question)