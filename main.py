def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    
    # Convert to Celsius first
    if from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "F":
        return round((celsius * 9 / 5) + 32, 2)
    elif to_unit == "K":
        return round(celsius + 273.15, 2)
    else:
        return round(celsius, 2)


# Demo
print(convert_temperature(100, "C", "F"))  # 212.0
print(convert_temperature(32, "F", "C"))   # 0.0
print(convert_temperature(300, "K", "C"))  # 26.85


#Kandace
t=5
w=3
print(w)
