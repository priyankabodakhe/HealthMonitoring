class StressLevel:
    def stress_level_detector(self):
        """Detects stress level"""
        print("Stress Level Detector")
        score = int(input("On a scale of 1 to 10, how stressed are you today? "))

        if score <= 3:
            print("You are feeling relaxed.")
        elif 4 <= score <= 7:
            print("You are moderately stressed. Take some time to relax.")
        else:
            print("You are very stressed. Consider speaking to a counselor or doing a relaxing activity.")
