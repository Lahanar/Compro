import ipywidgets as widgets
from IPython.display import display, clear_output

def run_checker(user_code, exercise_num):
    # The master data list
    score = [65, 12, 88, 45, 76, 3, 94, 51, 29, 60, 82, 18, 41, 99, 34, 55, 7, 85, 62, 20, 48, 73, 15, 90, 57]
    
    try:
        # Create a local environment and give them the 'score' list
        local_env = {'score': score.copy()}
        exec(user_code, {}, local_env)
        
        # Test Case logic
        if exercise_num == 1:
            # Easy: Get 1st and last score
            if local_env.get('first') == 65 and local_env.get('last') == 57:
                return "✅ Correct! You accessed the first and last elements."
            return "❌ Incorrect. Hint: Use score[0] and score[-1]."

        elif exercise_num == 2:
            # Easy: Count students
            if local_env.get('count') == 25:
                return "✅ Correct! len(score) is 25."
            return "❌ Hint: Use the len() function and save it to 'count'."

        elif exercise_num == 3:
            # Easy: Slicing
            if local_env.get('subset') == [12, 88, 45]:
                return "✅ Correct! You successfully sliced index 1 to 4."
            return "❌ Hint: subset = score[1:4]"

        elif exercise_num == 4:
            # Medium: Total Sum using loop
            if local_env.get('total') == 1289:
                return "✅ Correct! Total sum is 1289."
            return "❌ Incorrect total. Did you loop through the list?"

        elif exercise_num == 5:
            # Medium: Count passing scores (>= 50)
            if local_env.get('pass_count') == 14:
                return "✅ Correct! 14 students passed."
            return "❌ Incorrect count. Remember to check if score >= 50."

        elif exercise_num == 6:
            # Medium: Create a list of failed scores only
            if local_env.get('failed_list') == [12, 45, 3, 29, 18, 41, 34, 7, 20, 48, 15]:
                return "✅ Correct! failed_list created."
            return "❌ Hint: Use .append() inside an if statement."

        elif exercise_num == 7:
            # Difficult: Find Max without max()
            if local_env.get('highest') == 99:
                return "✅ Correct! The highest score is 99."
            return "❌ Hint: Start with highest = 0 and update it inside a loop."

        elif exercise_num == 8:
            # Difficult: Dictionary frequency
            # (Check if they created a dict where keys are grades)
            ans = local_env.get('result')
            if isinstance(ans, dict) and ans.get(99) == 1:
                return "✅ Correct! Dictionary built successfully."
            return "❌ Check your dictionary logic."

        elif exercise_num == 9:
            # Difficult: Indexed string
            if local_env.get('report') and "Student #1: 65" in local_env['report']:
                return "✅ Correct! report string generated."
            return "❌ Hint: Use enumerate() or a counter to get the index."

    except Exception as e:
        return f"⚠️ Syntax Error: {e}"

def create_ui(exercise_num, default_code):
    code_input = widgets.Textarea(value=default_code, layout={'height': '140px', 'width': '90%'})
    btn = widgets.Button(description="Check My Code", button_style='primary')
    out = widgets.Output()
    
    def on_click(b):
        with out:
            clear_output()
            print("Checking...")
            result = run_checker(code_input.value, exercise_num)
            print(result)
            
    btn.on_click(on_click)
    display(code_input, btn, out)
