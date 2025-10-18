# src/question_b/speed.py

CONVERSION_RATIO = 0.621371  # kilometers → miles

def get_miles_per_hour(kilometers: float, minutes: float):
    """
    Convert distance/time to miles per hour.

    - kilometers: distance in kilometers (must be ≥ 0)
    - minutes: time in minutes (must be > 0)

    Returns:
        mph as a float, or the string 'Invalid arguments'
        if either input is invalid.
    """
    # 1️⃣ Input validation
    if not isinstance(kilometers, (int, float)) or not isinstance(minutes, (int, float)):
        return "Invalid arguments"
    if kilometers < 0 or minutes <= 0:
        return "Invalid arguments"

    # 2️⃣ Compute miles and hours
    miles = kilometers * CONVERSION_RATIO
    hours = minutes / 60.0
    mph = miles / hours
    return mph
#write functions here, don't add input('') statements here!