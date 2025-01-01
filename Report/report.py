import datetime

class Report:
    def generate_report(self):
        """Generates a health report summary"""
        print("\nGenerating Health Report...")
        current_date = datetime.datetime.now()

        print(f"     Date: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("     Health Summary:")
        print("     BMI: 23.5 (Normal weight)")
        print("     Total Calories: 1500 kcal")
        print("     Exercise: 30 minutes (Running)")
        print("     Water Intake: 2L")
        print("     Stress Level: Moderate")
        print("     Sleep: 7 hours")

        print("Report generated successfully!")
