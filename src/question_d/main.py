from src.question_d.temps import get_fahrenheit

def main():
    print("Celsius  Fahrenheit")
    for c in range(0, 21):          # 0..20 inclusive
        f = get_fahrenheit(c)
        print(f"{c:>7}  {f:>10.2f}")

if __name__ == "__main__":
    main()