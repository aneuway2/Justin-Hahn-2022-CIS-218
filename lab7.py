def calculate_bmi(height, weight):
    return round((weight / (height * height) * 703), 1)


def test_calculate_bmi():
    # put in height, inches and BMI here
    assert calculate_bmi(71, 125) == 17.4
    assert calculate_bmi(71, 130) == 18.1
    assert calculate_bmi(67, 130) == 20.4
    assert calculate_bmi(67, 145) == 22.7
    assert calculate_bmi(67, 159) == 24.9
    assert calculate_bmi(67, 160) == 25.1
    assert calculate_bmi(67, 165) == 25.8
    assert calculate_bmi(67, 170) == 26.6
    assert calculate_bmi(67, 191) == 29.9
    assert calculate_bmi(67, 195) == 30.5
    assert calculate_bmi(67, 190) == 29.8
    assert calculate_bmi(67, 200) == 31.3
    print("all checks OK")


def bmi_to_cat(bmi):
    if bmi < 16:
        return "severley underweight"
    elif bmi >= 16 and bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "healthy"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    elif bmi >= 30:
        return "severley overweight"


def test_bmi_to_cat():
    # put bmi in here
    assert bmi_to_cat(15.9) == "severley underweight"
    assert bmi_to_cat(16) == "underweight"
    assert bmi_to_cat(18.5) == "healthy"
    assert bmi_to_cat(25) == "overweight"
    assert bmi_to_cat(30) == "severley overweight"
    print("all checks OK")


def main():
    height = float(input("Input your height in inches: "))
    weight = float(input("Input your weight in pounds: "))
    bmi = calculate_bmi(height, weight)
    cat = bmi_to_cat(bmi)
    print("Your body mass index is", bmi, "Which is considered", cat)


if __name__ == "__main__":
    main()
