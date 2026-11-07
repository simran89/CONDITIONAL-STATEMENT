pin = "1234"

balance = 5000

user_pin = input("Enter your ATM PIN: ")

if user_pin == pin:

    print("Login Successful!")

    while True:

        print("\n--- ATM MENU ---")

        print("1. Check Balance")

        print("2. Withdraw Money")

        print("3. Deposit Money")

        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("Your balance is:", balance)

        elif choice == "2":

            amount = float(input("Enter amount: "))

            if amount > 0 and amount <= balance:

                balance -= amount

                print("Please collect your cash.")

                print("Remaining balance:", balance)

            else:

                print("Invalid amount or insufficient balance.")

        elif choice == "3":

            amount = float(input("Enter deposit amount: "))

            if amount > 0:

                balance += amount

                print("Money deposited successfully!")

                print("Updated balance:", balance)

            else:

                print("Enter a valid amount.")

        elif choice == "4":

            print("Thank you for using ATM!")

            break

        else:

            print("Invalid choice!")

else:

    print("Incorrect PIN!")