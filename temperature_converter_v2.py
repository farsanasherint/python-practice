# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius temperature to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
if __name__ == "__main__":
    temp_c = 25
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is equal to {temp_f}°F")
