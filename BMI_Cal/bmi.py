class BMI:
    
    def calculate_bmi(weight, height):
        """Calculate and return BMI"""
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return bmi, "Underweight"
        elif 18.5 <= bmi < 24.9:
            return bmi, "Normal weight"
        elif 25 <= bmi < 29.9:
            return bmi, "Overweight"
        else:
            return bmi, "Obesity"

    def bmi_calculator(self):
        """Handles BMI calculation"""
        print("BMI Calculator")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        bmi, category = self.calculate_bmi(weight, height)
        print(f"Your BMI is {bmi:.2f}, which falls under the category: {category}")
