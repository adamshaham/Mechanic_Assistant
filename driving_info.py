def get_car_information():
    print("Let's capture some details about your car.")

    # Capture car details
    car_year = input("Enter the year of your car (e.g., 2015): ")
    car_make = input("Enter the make of your car (e.g., Toyota): ")
    car_model = input("Enter the model of your car (e.g., Camry): ")
    car_mileage = input("Enter the mileage of your car (in miles): ")

    # Capture driving habits
    print("\nHow would you describe your driving habits?")
    print("1. Fast and aggressive")
    print("2. Moderate and balanced")
    print("3. Slow and cautious")
    driving_habits = input("Choose an option (1, 2, or 3): ")

    # Map the user's input to driving habit descriptions
    driving_habits_dict = {
        "1": "Fast and aggressive",
        "2": "Moderate and balanced",
        "3": "Slow and cautious"
    }

    # Capture the corresponding driving habit
    driving_habit_description = driving_habits_dict.get(driving_habits, "Unknown")

    # Display captured information
    print("\nThank you! Here is the information you provided:")
    print(f"Year: {car_year}")
    print(f"Make: {car_make}")
    print(f"Model: {car_model}")
    print(f"Mileage: {car_mileage} miles")
    print(f"Driving Habits: {driving_habit_description}")

    # Return the information as a dictionary
    return {
        "year": car_year,
        "make": car_make,
        "model": car_model,
        "mileage": car_mileage,
        "driving_habits": driving_habit_description
    }


# Example usage
if __name__ == "__main__":
    car_info = get_car_information()
    print("\nCaptured Car Information:", car_info)
