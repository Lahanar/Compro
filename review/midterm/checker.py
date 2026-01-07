# checker.py
# ----------------------------------------
# CodeRunner-style checker for Colab
# ----------------------------------------

def check(qid, student_func):
    try:
        tests[qid](student_func)
        print(f"✅ {qid}: All tests passed!")
    except AssertionError as e:
        print(f"❌ {qid}: {e}")
    except Exception as e:
        print(f"❌ {qid}: Runtime error -> {e}")


# -------------------------
# TEST CASES
# -------------------------

def q1_test(fn):
    assert fn(3, 4) == 7
    assert fn(-1, 1) == 0

def q2_test(fn):
    assert fn("Alice", 20) == "Alice is 20 years old"

def q3_test(fn):
    assert fn([1, 2, 3]) == 6
    assert fn([]) == 0

def q4_test(fn):
    assert fn(5) == [0, 1, 2, 3, 4]

def q5_test(fn):
    assert fn({"a": 1, "b": 2}) == 3

def q6_test(fn):
    assert fn(75) == "Pass"
    assert fn(40) == "Fail"

def q7_test(fn):
    assert fn(10) == 55

def q8_test(fn):
    assert fn([[1, 2], [3, 4]]) == 10

def q9_test(fn):
    assert fn([1, 2, 2, 3]) == [1, 2, 3]

def q10_test(fn):
    assert fn(3) == [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def q11_test(fn):
    assert fn({"a": 10, "b": 20}) == 30

def q12_test(fn):
    assert fn([1, 2, 3, 4]) == [1, 3]


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
