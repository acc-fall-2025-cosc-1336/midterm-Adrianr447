#write functions here, don't add input('') statements here!

def get_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit:
      F = (9/5) * C + 32

    Returns float. Raises ValueError if celsius is not numeric.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("celsius must be a number")
    return (9.0 / 5.0) * celsius + 32.0