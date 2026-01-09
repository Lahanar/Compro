import ipywidgets as widgets
from IPython.display import display, clear_output
import math

def run_coderunner():
    # --- Configuration ---
    test_cases = [1, 5, 12.2]
    
    # UI Components
    instruction = widgets.HTML("<b>Task:</b> Use <code>math.pi</code> and the variable <code>radius</code>. Store the result in a variable named <code>result</code> formatted to 2 decimal places.")
    code_input = widgets.Textarea(
        value='# Write your code here\nimport math\nradius = \narea = \nresult = f""',
        layout={'height': '150px', 'width': '90%'}
    )
    check_btn = widgets.Button(description='Run & Check', button_style='primary')
    out = widgets.Output()

    def on_click(_):
        with out:
            clear_output()
            student_code = code_input.value
            
            # Validation: Ensure they use the required tools
            if "math.pi" not in student_code:
                print("❌ Hint: You must use 'math.pi' for precision.")
                return
            if "f\"" not in student_code and "f'" not in student_code:
                print("❌ Hint: Please use an f-string for formatting.")
                return

            print(f"{'Input (radius)':<15} | {'Your result':<15} | {'Status'}")
            print("-" * 45)

            passed_all = True
            for r in test_cases:
                # Calculate expected result internally
                expected = f"{math.pi * (r**2):.2f}"
                
                # Setup local environment
                local_env = {'radius': r}
                try:
                    exec(student_code, {"math": math}, local_env)
                    user_res = str(local_env.get('result', 'N/A'))
                    
                    if user_res == expected:
                        status = "✅ Correct"
                    else:
                        status = f"❌ Wrong (Expected {expected})"
                        passed_all = False
                    
                    print(f"{r:<15} | {user_res:<15} | {status}")
                except Exception as e:
                    print(f"{r:<15} | Error: {str(e)[:15]}... | ❌ Error")
                    passed_all = False
            
            if passed_all:
                print("\n🎉 Perfect! You've mastered f-strings and math.pi.")

    check_btn.on_click(on_click)
    display(instruction, code_input, check_btn, out)

# Automatically trigger the UI when the script is imported/run
if __name__ == "__main__":
    run_coderunner()
