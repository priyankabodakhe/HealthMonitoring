import time

class Water:
    def water_intake_reminder(self):
        """Reminds the user to drink water"""
        print("Water Intake Reminder")
        target = int(input("Enter your daily water intake target (in liters): "))
        current = 0
        while current < target:
            print(f"Current intake: {current}L. Please drink more water!")
            time.sleep(2)  # Simulate a reminder every 2 seconds (instead of 5 minutes)
            current += 0.50  # Assuming user drinks 0.5L every reminder

        print(f"Congratulations! You've met your water intake target of {target}L today!")
