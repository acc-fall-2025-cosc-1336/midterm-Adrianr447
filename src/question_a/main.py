from src.question_a.bonus import get_bonus_pay_amount

def main():
    try:
        sales = float(input("Enter sales amount (0–1999): "))
        result = get_bonus_pay_amount(sales)
        print(result)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
#add import