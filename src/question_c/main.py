# src/question_c/main.py
from src.question_c.days import get_day_of_week

def main():
    while True:
        raw = input("Enter a number 1–7 (q to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            break
        try:
            n = int(raw)
        except ValueError:
            print("Invalid number")
            continue
        print(get_day_of_week(n))

if __name__ == "__main__":
    main()
#add import