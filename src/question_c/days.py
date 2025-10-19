# src/question_c/days.py

def get_day_of_week(day: int) -> str:
    """
    1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
    5 = Friday, 6 = Saturday, 7 = Sunday.
    Return "Invalid number" for out-of-range or non-int input.
    """
    if not isinstance(day, int):
        return "Invalid number"

    mapping = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return mapping.get(day, "Invalid number")
#write functions here, don't add input('') statements here!