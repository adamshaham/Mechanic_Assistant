def add_maintenance_log(maintenance_logs):
    print("\nLet's add a maintenance log for your car.")

    # Capture maintenance details
    car_name = input("Enter the name of your car (e.g., 'Toyota Camry'): ")
    service_date = input("Enter the date of the service (e.g., '2024-08-12'): ")
    service_mileage = input("Enter the mileage at the time of service (in miles): ")

    print("\nWhat type of service was performed?")
    print("1. Oil Change")
    print("2. Tire Rotation")
    print("3. Brake Service")
    print("4. Transmission Service")
    print("5. Battery Replacement")
    print("6. Other")
    service_type_option = input("Choose an option (1-6): ")

    # Map the user's input to service type descriptions
    service_type_dict = {
        "1": "Oil Change",
        "2": "Tire Rotation",
        "3": "Brake Service",
        "4": "Transmission Service",
        "5": "Battery Replacement",
        "6": "Other"
    }

    # Capture the corresponding service type
    service_type = service_type_dict.get(service_type_option, "Unknown")

    # Store the maintenance log
    maintenance_log = {
        "car_name": car_name,
        "service_date": service_date,
        "service_mileage": service_mileage,
        "service_type": service_type
    }
    maintenance_logs.append(maintenance_log)

    # Display captured log
    print("\nMaintenance log added successfully!")
    print(f"Car Name: {car_name}")
    print(f"Service Date: {service_date}")
    print(f"Service Mileage: {service_mileage} miles")
    print(f"Service Type: {service_type}")

    return maintenance_logs


# Example usage
if __name__ == "__main__":
    maintenance_logs = []

    while True:
        add_maintenance_log(maintenance_logs)

        another = input("\nWould you like to add another maintenance log? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("\nAll Maintenance Logs:")
    for log in maintenance_logs:
        print(log)
