import os
import sys

# Add Stack directory for model import
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Add DSA directory for test_helper import
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from model import Stack
from test_helper import run_tests

def baseball_game(l:list):
    s = Stack()
    for i in l:
        if i == "+":
            s.push(s.peek()+s.peek_n(-2))
        elif i == "D":
            s.push(s.peek()*2)
        elif i == "C":
            s.pop()
        else:
            s.push(int(i))
        print(s.get())
    return sum(s.get())
    

if __name__ == "__main__":
    print(baseball_game(['100', '200', 'C', 'D', '+']))
    # run_tests(baseball_game)