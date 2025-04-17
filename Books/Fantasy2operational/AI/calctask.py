# Here's a simple implementation of the calculator described:

# I would say an AI failed (some 3B model)

import re

def calc(expression):
    # Replace all whitespace characters with a single space
    cleaned_expression = expression.replace(' ', '').replace('\t', '')

    # Split the cleaned expression into its components (numbers and operations)
    components = re.findall(r'-?\d+\.?\d*', cleaned_expression)

    # Initialize variables to hold the numbers and operations as they are parsed from the expression
    nums, ops = [], []

    # Iterate over each component in the expression
    for i, component in enumerate(components):
        try:
            # Try parsing the component as a number
            number = float(component)
        except ValueError:
            # If parsing as a number fails, it must be an operation
            if i == 0 or components[i-1] in "+*":
                ops.append(component)
            else:
                raise ValueError(f"Invalid expression at position {i}")

        # Add the parsed number or operation to its respective list
        if i < len(components):
            nums.append(number) if isinstance(number, (int, float)) else None

    # Initialize variables to hold the final result of the expression and a flag to indicate whether an error has occurred during parsing
    result = 0
    error_occurred = False

    # Iterate over each number in the expression
    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            # If this is the last number in the expression, its value becomes the final result of the expression
            result += num
        else:
            # If this is not the last number in the expression, its value must be an operation
            op = num

            if op == "+":
                result += nums[i+1] if i < len(nums) - 1 else 0
            elif op == "-":
                result -= nums[i+1] if i < len(nums) - 1 else 0
            elif op == "*":
                result *= nums[i+1] if i < len(nums) - 1 else 1
            elif op == "/":
                if nums[i+1] != 0:
                    result /= nums[i+1] if i < len(nums) - 1 else 1
                else:
                    raise ZeroDivisionError("Cannot divide by zero")

    # Return the final result of the expression
    return result

# This implementation uses regular expressions to parse the input string into its
# components (numbers and operations). It then iterates over these components,
# executing the appropriate operation in order. Finally, it returns the final result
# of the expression.

# Note that this implementation assumes that the input string is well-formed and does
# not contain any syntax errors. If the input string may contain syntax errors, you
# should add error handling code to handle these cases appropriately.

print(calc("1 + 3"))