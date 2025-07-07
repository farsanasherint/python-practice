# bmi_calculator.py

def calculate_bmi(weight, height):
    """
    Calculate BMI given weight (kg) and height (m).
    """
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """
    Determine BMI category based on calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"


Great – let’s do **Script 3 today itself** to maintain your momentum. Here is the **full final script** for immediate upload:

---

### 🌟 **Script 3: BMI Calculator**

#### ✅ **File name**
`bmi_calculator.py`

---

#### 🔹 **Code content**

```python
# bmi_calculator.py

def calculate_bmi(weight, height):
    """
    Calculate BMI given weight (kg) and height (m).
    """
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """
    Determine BMI category based on calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Example usage
weight_kg = 60
height_m = 1.65

bmi = calculate_bmi(weight_kg, height_m)
category = bmi_category(bmi)

print(f"BMI is {bmi:.2f}, which is considered '{category}'.")
