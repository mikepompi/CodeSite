# =============================================================================
# TESTER
# =============================================================================

from template_exercises import *    # Change to the appropriate module

# Import any other necessary libraries
import numpy as np
import random

# =============================================================================
# DATA GENERATOR FUNCTIONS
# These functions should end with _t



# =============================================================================
# INPUTS

functions = []  # user function names
functions_t = []   # tester function names
args_num = []   # number of arguments per par
test_cases = [
    
    ]
results = []

# =============================================================================
# GENERATE RESULTS

for i in range(len(functions_t)):
    func = functions_t[i]
    results.append([])
    if args_num[i] == 1:
        for args in test_cases[i]:
            results[i].append(func(args))
    else:
        for args in test_cases[i]:
            results[i].append(func(*args))
print("Successfully generated all the test cases.")

# =============================================================================
# TESTER

score = 0
max_score = 0

print("Starting to test your solutions.")

for i in range(len(functions)):
    max_score += len(test_cases[i])
    func = functions[i]
    valid = 0
    submitted = 0
    for case in range(len(test_cases[i])):
        score += 1
        if args_num[i] == 1:
            res = func(test_cases[i][case])
        else:
            res = func(*test_cases[i][case])
        if results[i][case] is not None and res is None:
            submitted += 1
        elif results[i][case] is not None and res is not None: 
            if results[i][case] != res:
                score -= 1
                valid += 1
                print("Wrong result\nExpected {}\nReceived {}".format(results[i][case], res))
    if submitted > 0:
        print("Part {} hasn't been submitted".format(i+1))
    elif valid == 0:        
        print("Part {} has valid solutions".format(i+1))

if score == 0:
    score_str = "0"
    score = 0
else:
    score_str = str(round(score/max_score*100, 1))
    score = int(score/max_score*100)
print("Your have finished {} % of this exercise".format(score_str))

