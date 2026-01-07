import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import io
import contextlib

def run_checker(user_code, exercise_num):
    # Base data for collection questions
    score_list = [65, 12, 88, 45, 76, 3, 94, 51, 29, 60, 82, 18, 41, 99, 34, 55, 7, 85, 62, 20, 48, 73, 15, 90, 57]
    
    try:
        # Initial environment setup
        local_env = {'score': score_list.copy(), 'math': math}
        
        # 1. First Run: Execute for visible output (Student sees this)
        exec(user_code, {}, local_env)
        
        # 2. Hidden Validation Logic
        if exercise_num == 1: # Area of Circle (Easy)
            # Test with radius 2.2
            t_rad = 2.2
            test_env = {'math': math, 'radius': t_rad}
            with contextlib.redirect_stdout(io.StringIO()):
                exec(user_code, {}, test_env)
            expected = f"{math.pi * (t_rad**2):.2f}"
            if test_env.get('result') == expected: return f"✅ Correct! Works for radius {t_rad}."
            return f"❌ Incorrect. For radius {t_rad}, expected '{expected}', but got '{test_env.get('result')}'."

        elif exercise_num == 2: # List Insert/Append (Easy)
            s = local_env.get('score')
            if s and s[0] == 100 and s[-1] == 999: return "✅ Correct! 100 at start, 999 at end."
            return "❌ Incorrect. Hint: use score.insert(0, 100) and score.append(999)."

        elif exercise_num == 3: # Dictionary (Easy)
            d = local_env.get('student')
            if isinstance(d, dict) and d.get('id') == 101: return "✅ Correct! Student dict created."
            return "❌ Incorrect. Make sure 'id' is 101."

        elif exercise_num == 4: # F-String Format (Easy)
            if local_env.get('msg') == "Student has 65 points.": return "✅ Correct formatting!"
            return "❌ Incorrect. Use f-string with variable 'score[0]'."

        elif exercise_num == 5: # If-Else Even/Odd (Medium)
            # Test with hidden number 13
            t_n = 13
            test_env = {'n': t_n}
            with contextlib.redirect_stdout(io.StringIO()):
                exec(user_code, {}, test_env)
            if test_env.get('status') == "Odd": return "✅ Correct logic for even/odd!"
            return "❌ Failed. Logic did not identify 13 as 'Odd'."

        elif exercise_num == 6: # Membership (Medium)
            if local_env.get('found') is True: return "✅ Correct! 99 is in list."
            return "❌ Hint: use '99 in score'."

        elif exercise_num == 7: # While Loop Break (Medium)
            if local_env.get('last_num') == 5: return "✅ Correct! Loop broke at 5."
            return "❌ Loop should stop when number is 5."

        elif exercise_num == 8: # List Sorting (Medium)
            if local_env.get('score') == sorted(score_list, reverse=True): return "✅ Correct sort!"
            return "❌ Hint: Use score.sort(reverse=True)."

        elif exercise_num == 9: # For Loop Sum Evens (Hard)
            if local_env.get('even_sum') == 510: return "✅ Correct! Total is 510."
            return "❌ Incorrect sum for even numbers."

        elif exercise_num == 10: # Nested Loop (Hard)
            if local_env.get('total_stars') == 15: return "✅ Correct nested logic!"
            return "❌ Pattern logic incorrect."

        elif exercise_num == 11: # Find Max (Hard)
            if local_env.get('highest') == 99: return "✅ Correct! 99 found."
            return "❌ Do not use max(). Use a loop."

        elif exercise_num == 12: # Continue Skip (Hard)
            # Sum score skipping 3
            if local_env.get('clean_sum') == 1286: return "✅ Correct! 3 was skipped."
            return "❌ Hint: if s == 3: continue."

        return "❌ Variable names not found."
    except Exception as e:
        return f"⚠️ Syntax Error: {e}"

def create_ui(exercise_num, default_code):
    code_input = widgets.Textarea(value=default_code, layout={'height': '180px', 'width': '95%'})
    btn = widgets.Button(description="Check Code", button_style='primary')
    out = widgets.Output()
    def on_click(b):
        with out:
            clear_output()
            print("--- Code Output ---")
            # This exec is just for the student to see their own print/error
            try: exec(code_input.value, {'math':math, 'score':[65, 12, 88, 45, 76, 3, 94, 51, 29, 60, 82, 18, 41, 99, 34, 55, 7, 85, 62, 20, 48, 73, 15, 90, 57]}, {})
            except Exception as e: print(f"Error: {e}")
            print("\n--- Checker ---")
            print(run_checker(code_input.value, exercise_num))
    btn.on_click(on_click)
    display(code_input, btn, out)
