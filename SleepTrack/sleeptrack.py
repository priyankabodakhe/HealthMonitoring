class SleepTrack:
    def sleep_tracker(self):
        """Tracks sleep duration"""
        print("Sleep Tracker")
        sleep_hours = float(input("Enter the number of hours you slept last night: "))

        if sleep_hours < 7:
            print("You did not get enough sleep. Aim for 7-9 hours.")
        elif 7 <= sleep_hours <= 9:
            print("You got a healthy amount of sleep.")
        else:
            print("You slept too much. Consider adjusting your sleep schedule.")
