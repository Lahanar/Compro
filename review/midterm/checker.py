# checker.py
# ----------------------------------------
# CodeRunner-style checker (NO functions)
# ----------------------------------------

import copy

def check(qid, student_ns):
    try:
        tests[qid](student_ns)
        print(f"✅ {qid}: All tests passed!")
    except AssertionError as e:
        print(f"❌ {qid}: {e}")
    except Exception as e:
        print(f"❌ {qid}: Runtime error -> {e}")


# -------------------------
# TEST CASES
# -------------------------

def q1_test(ns):
    # Variables & operators
    assert ns["result"] == 7, "Expected result = 7"

def q2_test(ns):
    # f-string output
    assert ns["output"] == "Alice is 20 years old"

def q3_test(ns):
    # List iteration
    assert ns["total"] == 6

def q4_test(ns):
    # for + range
    assert ns["numbers"] == [0, 1, 2, 3, 4]

def q5_test(ns):
    # Dictionary iteration
    assert ns["sum_values"] == 3

def q6_test(ns):
    # if-else
    assert ns["grade"] == "Pass"

def q7_test(ns):
    # while loop
    assert ns["sum_n"] == 55

def q8_test(ns):
    # Nested list
    assert ns["nested_sum"] == 10

def q9_test(ns):
    # Set + uniqueness
    assert ns["unique_sorted"] == [1, 2, 3]

def q10_test(ns):
    # Nested loops
    expected = [(0,0),(0,1),(0,2),
                (1,0),(1,1),(1,2),
                (2,0),(2,1),(2,2)]
    assert ns["pairs"] == expected

def q11_test(ns):
    # Dictionary aggregation
    assert ns["total_sales"] == 30

def q12_test(ns):
    # continue
    assert ns["odd_numbers"] == [1, 3]


tests = {
    "Q1": q1_test,
    "Q2": q2_test,
    "Q3": q3_test,
    "Q4": q4_test,
    "Q5": q5_test,
    "Q6": q6_test,
    "Q7": q7_test,
    "Q8": q8_test,
    "Q9": q9_test,
    "Q10": q10_test,
    "Q11": q11_test,
    "Q12": q12_test,
}
