# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
temp_c = 37
print(f"{temp_c}°C is equal to {celsius_to_fahrenheit(temp_c)}°F")
