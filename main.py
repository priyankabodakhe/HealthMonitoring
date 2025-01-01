# main.py
from LoginPage.login import Login
from BMI_Cal.bmi import BMI
from CaloriesTrack.calories import Calories
from HeartRate.heartrate import HeartRate
from Report.report import Report
from SleepTrack.sleeptrack import SleepTrack
from StressLevel.stresslevel import StressLevel
from Water.water import Water

def display_menu():
    """Displays the main menu of the Health Monitoring System"""
    print("\nHealth Monitoring System")
    print("1. User Registration/Login")
    print("2. BMI Calculator")
    print("3. Water Intake Reminder")
    print("4. Calorie Tracker")
    print("5. Heart Rate Analyzer")
    print("6. Stress Level Detector")
    print("7. Sleep Tracker")
    print("8. Generate Health Report")
    print("0. Exit")

def main():
    print("***Welcome to Health Monitoring System***")
    login = Login()
    bmi = BMI()
    water = Water()
    calories = Calories()
    heartrate = HeartRate()
    stresslevel = StressLevel()
    sleeptrack = SleepTrack()
    report = Report()

    while True:
        print("\n  1. Register")
        print("  2. Login")
        print("  0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            if login.register():
                print("You can now log in.")
        elif choice == '2':
            if login.log():
                while True:
                    display_menu()
                    sub_choice = input("Choose an option: ")

                    if sub_choice == '1':
                        print("You are already logged in.")
                    elif sub_choice == '2':
                        bmi.bmi_calculator()
                    elif sub_choice == '3':
                        water.water_intake_reminder()
                    elif sub_choice == '4':
                        calories.calorie_tracker()
                    elif sub_choice == '5':
                        heartrate.heart_rate_analyzer()
                    elif sub_choice == '6':
                        stresslevel.stress_level_detector()
                    elif sub_choice == '7':
                        sleeptrack.sleep_tracker()
                    elif sub_choice == '8':
                        report.generate_report()
                    elif sub_choice == '0':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
