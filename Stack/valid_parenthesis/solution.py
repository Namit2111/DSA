import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from model import Stack
from test_helper import run_tests


def validate_parenthesis(st: str) -> bool:
    inverse={
        ')':'(',
        '}':'{',
        ']':'['
    }
    s = Stack()
    for i in st:
        if i in ['(','[','{']:
            s.push(i)
        if i in [')','}',']']:
            if s.is_empty():
                return False
            element = s.peek()
            if element == inverse[i]:
                s.pop()
    if s.is_empty():
        return True
    else:
        return False
    


if __name__ == "__main__":
    # print(validate_parenthesis("()"))
    run_tests(validate_parenthesis)
