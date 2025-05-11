from datetime import datetime
def calculate_days_between():
    """
Prompts the user to input two dates in the 'YYYY-MM-DD' format and computes the number of days separating them.

Example:
    Enter the start date (YYYY-MM-DD): 2025-05-01
    Enter the end date (YYYY-MM-DD): 2025-05-04
    Difference in days: 3

If the input does not match the required date format, an error message is displayed.
"""
    try:
        start = input("Enter the start date (YYYY-MM-DD): ")
        end = input("Enter the end date (YYYY-MM-DD): ")
        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")
        difference = abs((d2 - d1).days)
        print("Difference in days:", difference)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

calculate_days_between()
