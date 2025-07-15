# main.py
import sys
import os

# Add the directory that contains the 'pocketflow' module
sys.path.append(os.path.join(os.path.dirname(__file__), 'pocketflow'))
from pocketflow import Node
from utils.call_llm import call_llm
def node_property(func):
    func._is_node_property = True
    return func
# class GetQuestionNode(Node):
#     def exec(self, _):
#         question = input("Enter your question: ").strip()
#         if not question:
#             raise ValueError("❌ You must enter a question.")
#         print(f"📝 Question asked to Gemini: {question!r}")
#         return question

class GetQuestionNode(Node):
    def exec(self, _):
        question = input("Enter your question: ").strip()
        print(f"📝 Question asked to Gemini: {question!r}")
        return question

class AnswerNode(Node):
    def exec(self, _input):  # ← MUST be named _input
        print(f"🤖 Gemini received question: {_input!r}")
        return call_llm(_input)

# class AnswerNode(Node):
#     def exec(self, question):
#         print(f"🤖 Gemini received question: {question!r}")
#         return call_llm(question)

