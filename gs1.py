import stable_matching_helpers as helpers
import ast
import json
import sys

if __name__ == '__main__':


    with open (sys.argv[1],'r') as f:
        data = ast.literal_eval(f.read())
    print(data[0][0]['a1'])