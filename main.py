# main.py
import sys
import os
# Add current directory so that flow.py can be imported
sys.path.append(os.path.dirname(__file__))

from flow import create_qa_flow

def main():
    shared = {}
    flow = create_qa_flow()
    flow.run(shared)
    print("🎯 Final Answer:", shared.get("AnswerNode"))

if __name__ == "__main__":
    main()