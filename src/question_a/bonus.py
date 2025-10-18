def get_bonus_pay_amount(sales: float):
    """
    Return bonus based on sales:
      0–499      -> 5%
      500–999    -> 6%
      1000–1499  -> 7%
      1500–1999  -> 8%

    Return "Invalid arguments" if sales is not numeric or outside 0..1999.
    """
    # 1) Validate the input first (defensive programming)
    if not isinstance(sales, (int, float)):
        return "Invalid arguments"
    if sales < 0 or sales > 1999:
        return "Invalid arguments"

    # 2) Decide the rate using ordered conditions (note the <= makes ranges inclusive)
    if sales <= 499:
        rate = 0.05
    elif sales <= 999:
        rate = 0.06
    elif sales <= 1499:
        rate = 0.07
    else:
        rate = 0.08

    # 3) Compute and return the raw numeric amount
    return sales * rate
