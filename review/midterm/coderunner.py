# checker.py
import sys
import io

def check_work(student_code):
    test_cases = [1, 5, 0, 2.5]
    expected_outputs = ["3.14", "78.54", "0.00", "19.63"]
    
    passed = 0
    print("--- Running Tests ---")

    for radius_val, expected in zip(test_cases, expected_outputs):
        # We create a dictionary to act as the 'environment' for the code
        # We inject the radius into this environment
        local_vars = {"radius": radius_val}
        
        try:
            # Execute the student's code within that environment
            exec(student_code, {}, local_vars)
            
            # Check the variable 'result' that the student was asked to create
            user_result = local_vars.get("result")
            
            if user_result == expected:
                print(f"✅ Test Passed: Radius {radius_val} produced {expected}")
                passed += 1
            else:
                print(f"❌ Test Failed: For radius {radius_val}, expected '{expected}', but got '{user_result}'")
                
        except Exception as e:
            print(f"💥 Error running your code for radius {radius_val}: {e}")

    print(f"\nScore: {passed}/{len(test_cases)}")
