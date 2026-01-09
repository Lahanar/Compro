import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import sys
import io

def run_grader(_):
    # Get code from the text area
    student_code = code_input.value
    
    # Define our test cases (Inputs)
    test_inputs = [1, 5, 10.5]
    expected_outputs = ["3.14", "78.54", "346.36"]
    
    with output_area:
        clear_output()
        print(f"{'Input (Radius)':<15} | {'Your Output (Result)':<20} | {'Status'}")
        print("-" * 55)
        
        all_passed = True
        for radius_val, expected in zip(test_inputs, expected_outputs):
            # Setup the environment with the current radius
            local_env = {"radius": radius_val, "math": math}
            
            try:
                # Redirect stdout to catch any print statements if needed
                exec(student_code, {}, local_env)
                
                # We expect the student to store the string in a variable named 'result'
                user_result = str(local_env.get("result", "Variable 'result' not found"))
                
                status = "✅ Pass" if user_result == expected else f"❌ Fail (Expected {expected})"
                if user_result != expected: all_passed = False
                
                print(f"{radius_val:<15} | {user_result:<20} | {status}")
                
            except Exception as e:
                print(f"{radius_val:<15} | Error: {type(e).__name__} | ❌ Error")
                all_passed = False

        if all_passed:
            print("\n🎉 Excellent! All test cases passed.")

# UI Components
code_input = widgets.Textarea(
    placeholder='Type your code here...',
    description='Code:',
    layout={'height': '200px', 'width': '90%'}
)

check_button = widgets.Button(
    description='Check My Code',
    button_style='success',
    tooltip='Click to test your code'
)

output_area = widgets.Output()

check_button.on_click(run_grader)

# Display the UI
print("Problem: Use 'math.pi' and the variable 'radius' to calculate the area.")
print("Store the final formatted string in a variable named 'result' (2 decimal places).")
display(code_input, check_button, output_area)
