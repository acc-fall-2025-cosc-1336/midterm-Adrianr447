# src/question_b/main.py
import sys, os

# Allow this file to run directly in Codespaces
if __package__ is None:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from src.question_b.speed import get_miles_per_hour

def main():
    try:
        kilometers = float(input("Enter kilometers: ").strip())
        minutes = float(input("Enter minutes: ").strip())
    except ValueError:
        print("Invalid input.")
        return

    result = get_miles_per_hour(kilometers, minutes)
    print(result)

if __name__ == "__main__":
    main()
#add import