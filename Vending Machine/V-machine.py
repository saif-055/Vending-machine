# Defining a list of dictionaries representing each product in the vending machine
products = [
    {'Item Code': '01', 'Item Name': 'Water', 'Item Price': 1, 'Item Stock': 3},
    {'Item Code': '02', 'Item Name': 'Pepsi', 'Item Price': 3, 'Item Stock': 6},
    {'Item Code': '03', 'Item Name': 'Redbull', 'Item Price': 6.5, 'Item Stock': 1},
    {'Item Code': '04', 'Item Name': 'Fanta', 'Item Price': 2.5, 'Item Stock': 8},
    {'Item Code': '05', 'Item Name': 'Croissant', 'Item Price': 2.5, 'Item Stock': 6},
    {'Item Code': '06', 'Item Name': 'Cheetos', 'Item Price': 3.5, 'Item Stock': 6},
    {'Item Code': '07', 'Item Name': 'Kit-Kat', 'Item Price': 1.5, 'Item Stock': 3},
    {'Item Code': '08', 'Item Name': 'Milkyway', 'Item Price': 3, 'Item Stock': 0},
    {'Item Code': '09', 'Item Name': 'Mars', 'Item Price': 3, 'Item Stock': 4},
    {'Item Code': '10', 'Item Name': 'Galaxy', 'Item Price': 3, 'Item Stock': 9},
    {'Item Code': '11', 'Item Name': 'Skittles', 'Item Price': 3, 'Item Stock': 2},
    {'Item Code': '12', 'Item Name': 'Snickers', 'Item Price': 3.5, 'Item Stock': 2}
]

# Initializing the user's wallet and a list to store transaction history
wallet = 0
transaction_history = []

print('----------WELCOME TO MY VENDING MACHINE-----------')

# A continuous loop for the vending machine operations
while True:
    # Displaying the list of available products along with their details
    print("\nAvailable Products:")
    for item in products:
        print(f"{item['Item Code']} - {item['Item Name']}, Price: {item['Item Price']}, Stock: {item['Item Stock']}")

    # Asking the user to input the amount of money they want to add
    try:
        money_amount = float(input("\nEnter the amount of money (0 to exit): "))

        # If the user enters 0, exit the vending machine
        if money_amount == 0:
            break

        # Adding the entered money to the user's wallet
        wallet += money_amount

        # Asking the user to input the product code they want to purchase
        product_code = input("Enter the product code: ")

        # Searching for the selected item in the products list
        selected_item = next((item for item in products if item['Item Code'] == product_code), None)

        if selected_item:
            # Checking if the selected item is in stock
            if selected_item['Item Stock'] > 0:
                # Checking if the user has enough money to purchase the item
                if wallet >= selected_item['Item Price']:
                    # Calculating the change and dispensing the item
                    change = wallet - selected_item['Item Price']
                    print(f"\nDispensing {selected_item['Item Name']}")
                    print("Your change is", change)

                    # Updating the item stock and recording the transaction
                    selected_item['Item Stock'] -= 1
                    transaction_history.append({
                        'Item Name': selected_item['Item Name'],
                        'Amount Spent': selected_item['Item Price'],
                        'Change Given': change
                    })
                    wallet = change
                    print(f"Updated Wallet Balance: {wallet}\n")

                    # Asking if the user wants to make another purchase
                    additional_purchase = input("Do you want to make another purchase? (yes/no): ").lower()
                    if additional_purchase != 'yes':
                        break  # Exits the loop if the user doesn't want to make another purchase
                else:
                    # Informing the user if their wallet has insufficient funds
                    remaining_amount = selected_item['Item Price'] - wallet
                    print(f"Cash insufficient. Amount pending: {remaining_amount}")
            else:
                # Informing the user if the selected item is out of stock
                print("The item is out of stock.")
        else:
            # Printing invalid code when it does not find a matching product
            print("Invalid product code. Please enter a valid code.")

    except ValueError:
        # If an invalid input is provided, ask again
        print("Invalid input. Please enter a valid numeric value.")

# Displaying the transaction history at the end
print("\n-------- TRANSACTION HISTORY --------")
for transaction in transaction_history:
    print(f"Item: {transaction['Item Name']}, Amount Spent: {transaction['Amount Spent']}, Change Given: {transaction['Change Given']}")

# Displaying the final wallet balance
print(f"\nFinal Wallet Balance: {wallet}")

# Thanking the user for using the vending machine
print("!!! Thank you for using my vending machine. Have a great day !!!")
