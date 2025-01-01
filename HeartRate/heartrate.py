class HeartRate:
    def heart_rate_analyzer(self):
        """Analyzes heart rate"""
        print("Heart Rate Analyzer")
        heart_rate = int(input("Enter your heart rate (beats per minute): "))

        if heart_rate < 60:
            print("Your heart rate is below normal (bradycardia).")
        elif 60 <= heart_rate <= 100:
            print("Your heart rate is normal.")
        else:
            print("Your heart rate is above normal (tachycardia).")
