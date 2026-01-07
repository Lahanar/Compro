import ipywidgets as widgets
from IPython.display import display, clear_output

def run_checker(user_code, exercise_num):
    """General function to execute student code and run specific tests."""
    try:
        local_env = {}
        exec(user_code, {}, local_env)
        
        # Test Logic for each question
        if exercise_num == 1: # Get Last Score
            func = local_env['get_last_score']
            if func([91, 22, 59]) == 59 and func([10, 20]) == 20:
                return "✅ Correct! Last element retrieved."
            return "❌ Incorrect. Did you use index [-1]?"

        elif exercise_num == 2: # Count Students
            func = local_env['count_students']
            if func([1, 2, 3, 4]) == 4:
                return "✅ Correct! len() used properly."
            return "❌ Incorrect count."

        elif exercise_num == 3: # Sum Range
            func = local_env['sum_range']
            if func([10, 20, 30, 40, 50]) == 90: # 20+30+40
                return "✅ Correct! Slice [1:4] summed."
            return "❌ Incorrect sum."

        elif exercise_num == 4: # Failing Grade
            func = local_env['count_failing']
            if func([91, 22, 59, 40]) == 2:
                return "✅ Correct! Loop and 'if' worked."
            return "❌ Incorrect count."

        elif exercise_num == 5: # Dict Search
            func = local_env['get_student_score']
            data = {"A": 50}
            if func(data, "A") == 50 and func(data, "B") == "Not Found":
                return "✅ Correct! Dictionary handling is good."
            return "❌ Name not found logic failed."

        elif exercise_num == 6: # Even Index
            func = local_env['get_even_index_items']
            if func([10, 20, 30, 40]) == [10, 30]:
                return "✅ Correct! Enumerate filter worked."
            return "❌ Incorrect list returned."

        elif exercise_num == 7: # Stats
            func = local_env['get_stats']
            if func({"A": 10, "B": 90}) == (90, 10):
                return "✅ Correct! Max/Min found."
            return "❌ Stats logic error."

        elif exercise_num == 8: # BMI
            func = local_env['calc_bmis']
            # [name, w, h] -> w/h^2
            res = func([["Test", 70, 1.75]])
            if abs(res[0] - 22.85) < 0.1:
                return "✅ Correct! BMI calculation accurate."
            return "❌ Calculation error."

        elif exercise_num == 9: # Categorize
            func = local_env['categorize']
            res = func([90, 40])
            if res.get("Pass") == [90] and res.get("Fail") == [40]:
                return "✅ Masterful! Dictionary of lists complete."
            return "❌ Categorization failed."

    except Exception as e:
        return f"⚠️ Error: {e}"

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
