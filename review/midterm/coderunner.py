import ipywidgets as widgets
from IPython.display import display, clear_output
import math

def run_grader():
    # Problem Definitions
    problems = {
        "1. Circle Area": {
            "hint": "Use math.pi and radius.\nStore in 'result' (2 dec).", 
            "tests": [{"radius": 2}], "target": "result", 
            "expected": lambda d: f"{math.pi * d['radius']**2:.2f}"
        },
        "2. List Ops": {
            "hint": "score.insert(0, 5) then score.append(30).\nStore in 'result'.", 
            "tests": [{"score": [10, 20]}], "target": "result", 
            "expected": lambda d: [5, 10, 20, 30]
        },
        "3. Dictionary": {
            "hint": "Create dict 'student'.\nUse keys 'name' and 'age'.", 
            "tests": [{}], "target": "student", 
            "expected": lambda d: {"name": "John", "age": 20}
        },
        "4. Conversion": {
            "hint": "Convert s='10' to integer.\nStore in variable 'x_int'.", 
            "tests": [{"s": "10"}], "target": "x_int", 
            "expected": lambda d: 10
        },
        "5. Even/Odd": {
            "hint": "If num is even, result='Even'.\nElse result='Odd'.", 
            "tests": [{"num": 4}, {"num": 7}], "target": "result", 
            "expected": lambda d: "Even" if d['num'] % 2 == 0 else "Odd"
        },
        "6. In Operator": {
            "hint": "Check if 99 is in list 'score'.\nStore boolean in 'found'.", 
            "tests": [{"score": [1, 99, 3]}], "target": "found", 
            "expected": lambda d: 99 in d['score']
        },
        "7. While Break": {
            "hint": "Loop i from 0, break when i == 5.\nStore i in 'result'.", 
            "tests": [{}], "target": "result", 
            "expected": lambda d: 5
        },
        "8. Sort List": {
            "hint": "Sort 'score' descending.\nStore in 'result'.", 
            "tests": [{"score": [1, 5, 2]}], "target": "result", 
            "expected": lambda d: [5, 2, 1]
        },
        "9. Sum Evens": {
            "hint": "Sum even numbers in 'nums'.\nStore in 'total'.", 
            "tests": [{"nums": [1, 2, 3, 4]}], "target": "total", 
            "expected": lambda d: 6
        },
        "10. Star Triangle": {
            "hint": "Create 3-line triangle.\nStore in 'stars'.",
            "tests": [{}], "target": "stars", 
            "expected": lambda d: "*\n**\n***"
        },
        "11. BMI": {
            "hint": "BMI = w/h^2 from data={'w':70, 'h':1.7}.\nStore in 'bmi' (1 dec).", 
            "tests": [{"data": {"w": 70, "h": 1.75}}], "target": "bmi", 
            "expected": lambda d: f"{d['data']['w'] / d['data']['h']**2:.1f}"
        },
        "12. Continue": {
            "hint": "Sum nums [1,2,3], skip 2.\nStore in 'total'.", 
            "tests": [{"nums": [1, 2, 3]}], "target": "total", 
            "expected": lambda d: 4
        }
    } # This closing brace ends the problems dictionary
    
    # UI setup
    selector = widgets.Dropdown(options=list(problems.keys()), description='Problem:')
    instruction = widgets.HTML(value=f"<b>Goal:</b> {problems[selector.value]['hint']}")
    code_input = widgets.Textarea(placeholder='Write code here...', layout={'height': '180px', 'width': '95%'})
    btn = widgets.Button(description='Run & Check', button_style='success')
    out = widgets.Output()

    def update_ui(change):
        instruction.value = f"<b>Goal:</b> {problems[change.new]['hint']}"
        out.clear_output()
    selector.observe(update_ui, names='value')

    def check_code(_):
        with out:
            clear_output()
            p = problems[selector.value]
            student_code = code_input.value
            print(f"Testing: {selector.value}\n" + "-"*30)
            
            for test in p["tests"]:
                local_env = {**test, "math": math}
                try:
                    exec(student_code, {"math": math}, local_env)
                    actual = local_env.get(p["target"])
                    expected = p["expected"](test)
                    
                    if str(actual) == str(expected):
                        print(f"✅ Input {test or 'None'} -> Got: {actual} (Pass)")
                    else:
                        print(f"❌ Input {test or 'None'} -> Expected: {expected}, Got: {actual}")
                except Exception as e:
                    print(f"💥 Error: {e}")
    
    btn.on_click(check_code)
    display(selector, instruction, code_input, btn, out)

if __name__ == "__main__":
    run_grader()
