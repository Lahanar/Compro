import ipywidgets as widgets
from IPython.display import display, clear_output

def run_checker(user_code, exercise_num):
    try:
        # 1. Setup the data the student needs
        # We put the 'score' list in the global scope for them
        score = [65, 12, 88, 45, 76, 3, 94, 51, 29, 60, 82, 18, 41, 99, 34, 55, 7, 85, 62, 20, 48, 73, 15, 90, 57]
        
        # 2. Execute their code
        local_env = {'score': score} # Give them the score variable
        exec(user_code, {}, local_env)
        
        # 3. Test based on the variable they were supposed to create
        if exercise_num == 1:
            # Task: Get the 1st score and save it in a variable named 'ans'
            if 'ans' not in local_env: return "❌ Error: Please save your result in a variable named 'ans'"
            if local_env['ans'] == 65: return "✅ Correct! ans is 65."
            
        elif exercise_num == 2:
            # Task: Count students and save in 'total'
            if 'total' not in local_env: return "❌ Error: Use the variable name 'total'"
            if local_env['total'] == 25: return "✅ Correct! total is 25."
            
        # ... add other exercises similarly ...

        return "❌ Result is incorrect. Try again!"
    except Exception as e:
        return f"⚠️ Syntax Error: {e}"

def create_ui(exercise_num, default_code):
    """Creates the UI widgets for the student."""
    code_input = widgets.Textarea(value=default_code, layout={'height': '120px', 'width': '90%'})
    btn = widgets.Button(description="Check My Code", button_style='success')
    out = widgets.Output()
    
    def on_click(b):
        with out:
            clear_output()
            result = run_checker(code_input.value, exercise_num)
            print(result)
            
    btn.on_click(on_click)
    display(code_input, btn, out)
