class Calories:
    def calorie_tracker(self):
        """Tracks calories consumed"""
        print("Calorie Tracker")
        total_calories = 0
        while True:
            food = input("Enter the food item (or type 'done' to finish): ")
            if food.lower() == 'done':
                break
            calories = int(input(f"Enter the calories for {food}: "))
            total_calories += calories

        print(f"Total Calories Consumed: {total_calories}")
