
import random

cab_types = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}


while True:
    print("\n========================================")
    print("         CAB BOOKING CHATBOT")
    print("========================================")
    print("1. Book Ride")
    print("2. Exit")
    print("========================================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        # Step 1: Select cab type
        while True:
            print("\nSelect Your Cab Type")
            print("1. Auto  - Rs.12/km")
            print("2. Sedan - Rs.18/km")
            print("3. SUV   - Rs.25/km")
            print("4. Return to Main Menu")

            cab_choice = input("Enter your choice: ").strip()

            if cab_choice in ("1", "2", "3"):
                cab_type, rate = cab_types[int(cab_choice)]
                break

            elif cab_choice == "4":
                cab_type = None
                break

            else:
                print("Invalid cab choice! Please try again.")

        if cab_type is None:
            continue

        # Step 2: Select route
        while True:
            print("\nAvailable Routes")
            print("1. Pune Station to Shivajinagar - 5 km")
            print("2. Swargate to Kothrud - 8 km")
            print("3. Hinjawadi to Wakad - 10 km")
            print("4. Return to Main Menu")

            route_choice = input("Enter route number: ").strip()

            if route_choice in ("1", "2", "3"):
                source, destination, distance = routes[
                    int(route_choice)
                ]
                break

            elif route_choice == "4":
                source = None
                break

            else:
                print("Invalid route choice! Please try again.")

        if source is None:
            continue

        # Step 3: Calculate fare
        fare = distance * rate

        # Step 4: Display booking summary
        print("\n========================================")
        print("             BOOKING SUMMARY")
        print("========================================")
        print(f"Cab Type       : {cab_type}")
        print(f"Source         : {source}")
        print(f"Destination    : {destination}")
        print(f"Distance       : {distance} km")
        print(f"Rate           : Rs.{rate}/km")
        print(f"Total Fare     : Rs.{fare}")
        print("========================================")

        # Step 5: Confirm or cancel booking
        while True:
            print("\nBooking Confirmation")
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")

            confirm_choice = input(
                "Enter your choice: "
            ).strip()

            if confirm_choice == "1":
                # Generate OTP only after confirmation
                otp = random.randint(0, 9999)
                otp = f"{otp:04d}"

                print("\n========================================")
                print("       OTP SHARED SUCCESSFULLY")
                print("========================================")
                print(f"Your Ride OTP is: {otp}")
                print("Your booking is confirmed!")
                print("IMPORTANT: Ride cancellation is not")
                print("allowed after the OTP has been shared.")
                print("========================================")

                # OTP is shared; finish this booking
                break

            elif confirm_choice == "2":
                print("\nRide cancelled successfully.")
                print("No OTP has been generated or shared.")
                break

            else:
                print("Invalid choice! Please enter 1 or 2.")

        # Return to the main menu after booking
        continue


    elif choice == "2":
        print("\nThank you for using Cab Booking Chatbot!")
        print("Have a safe journey. Goodbye!")
        break

    
    else:
        print("\nInvalid menu choice! Please enter 1 or 2.")
