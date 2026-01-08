import json
import os
import inspect


def run_tests(solution_func, test_file_path=None):
    """
    Run test cases from a JSON file against a solution function.

    Args:
        solution_func: Your solution function to test
        test_file_path: Path to test_case.json file

    JSON format:
        {
            "test_cases": [
                {"input": ..., "expected": ...},
                {"input": [...], "expected": ...}  # for multiple args
            ]
        }
    """
    # Auto-detect test_case.json from caller's directory
    if test_file_path is None:
        caller_file = inspect.stack()[1].filename
        test_file_path = os.path.join(os.path.dirname(caller_file), "test_case.json")

    with open(test_file_path, "r") as f:
        data = json.load(f)

    test_cases = data["test_cases"]
    passed = 0

    print("Running tests...\n")
    print("-" * 60)

    for i, tc in enumerate(test_cases, 1):
        input_val = tc["input"]
        expected = tc["expected"]

        # Handle single arg or multiple args
        if isinstance(input_val, list):
            result = solution_func(*input_val)
        else:
            result = solution_func(input_val)

        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:    {input_val}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()

    print("-" * 60)
    print(f"Results: {passed}/{len(test_cases)} passed")

    if passed == len(test_cases):
        print("All tests passed!")
