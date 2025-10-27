import traceback


def run_code_with_arrow(code: str):
    try:
        exec(code, {})
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        last = tb[-1]
        filename, lineno, func, text = last

        # Split code into lines for display
        lines = code.strip().split("\n")

        # Determine the range (5 before and after the error line)
        start = max(lineno - 6, 0)
        end = min(lineno + 5, len(lines))

        # Display context with line numbers and an arrow marker
        for i in range(start, end):
            prefix = "---> " if i == lineno - 1 else "     "
            print(f"{prefix}{i + 1:>4}: {lines[i]}")

        # Show complete traceback information
        print("\n" + traceback.format_exc())


# Example code
code_snippet = """
def divide(a, b):
    return a / b

def compute():
    val1 = 5
    val2 = 0  # division by zero
    result = divide(val1, val2)
    print(result)

def executor():
    for i in range(3):
        compute()

executor()
"""

run_code_with_arrow(code_snippet)
