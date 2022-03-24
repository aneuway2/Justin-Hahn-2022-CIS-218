"""
Week 5 lab
Justin Hahn
"""

degrees_celcius = float(
    input("Enter the degrees in celcius")
)

temp_dict = {
    0: "0 degrees celcius is the freezing point of water",
    100: "100 degrees celcius is the boiling point of water",
    "snow": "the weather today is below freezing so theres a chance of snow",
    "rain": "the weather today is above freezing so theres a chance of rain",
    }

if temp_dict.get(degrees_celcius):
    print(temp_dict.get)
elif degrees_celcius >= 0:
    print(temp_dict.get("rain"))
else:
    print(temp_dict.get("snow"))

def celcius_to_fahrenheit(degrees_celcius=0):
    """
    apx. 0 celcius = 32 fahrenheit
    """
    fahrenheit_temp = (degrees_celcius * 1.8) + 32
    print(f"{fahrenheit_temp}")
    return fahrenheit_temp

def test_celcius_to_fahrenheit():
    assert celcius_to_fahrenheit(0) == 32
    assert celcius_to_fahrenheit(100) == 212
    assert celcius_to_fahrenheit(8) == 46.4
    assert celcius_to_fahrenheit(4) == 39.2

celcius_to_fahrenheit(degrees_celcius)
test_celcius_to_fahrenheit()
