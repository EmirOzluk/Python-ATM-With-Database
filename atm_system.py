import json
import random

# DATABASE SYSTEM: Load existing data when the program starts
try:
    with open("bank_database.json", "r", encoding="utf-8") as file:
        cards = json.load(file)
except FileNotFoundError:
    cards = {}

# DATABASE SYSTEM: Function to save current data permanently to the storage
def save_data():
    with open("bank_database.json", "w", encoding="utf-8") as file:
        json.dump(cards, file, ensure_ascii=False, indent=4)

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def create_card():
    while True:
        print("\nWelcome to the Card Creation System. Please type 'CONFIRM' to start the process.")
        confirmation = input("Type CONFIRM to start the process: ")
        if confirmation == "CONFIRM":
            pin = int(input("Please set a !numerical! PIN for your card: "))
            confirm_pin = int(input("Please confirm your PIN: "))
            if pin == confirm_pin:
                print("Your PIN has been successfully created. Now, please enter your personal details.")
                while True:
                    random_iban = "".join(random.choices(digits, k=8))
                    if random_iban not in cards:
                        iban = random_iban
                        break
                id_number = int(input("Enter your ID Number (TC): "))
                cvv = "".join(random.choices(digits, k=3))
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                birth_date = input("Enter your birth date: ")
                support_code = "".join(random.choices(digits, k=5))
                
                print("Your card has been successfully created!")
                print(f"""
                ============================================================
                |    VIRTUAL CARD VIEW (DO NOT SHARE FOR YOUR SECURITY)    |
                ============================================================
                |                                                          |
                | NAME: {first_name}           IBAN: {iban}                |
                | SURNAME: {last_name}        PIN: {pin}                  |
                | ID NO: {id_number}          CVV: {cvv}                  |
                | BIRTHDATE: {birth_date}     Balance: 0                  |
                | Support Code: {support_code}  REPUBLIC OF TURKEY-K0938    |
                =============================================================""")
                
                cards[iban] = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "id_number": id_number,
                    "birth_date": birth_date,
                    "support_code": support_code,
                    "iban": iban,
                    "pin": pin,
                    "cvv": cvv,
                    "balance": 0,
                }
                save_data() # Save the newly created card to the database file
                break
            else:
                print("PINs do not match. Please enter it correctly.")
        else:
            print("Since you typed something other than CONFIRM, the system is shutting down...")
            break

# ATM SYSTEM HISTORY TRACKERS
history_deposit = []
history_withdraw = []
history_transfer = []
history_balance_check = 0
history_pin_change = []
history_support_call = 0
history_logs_check = 0
history_card_creation = 0
history_card_info_check = 0

while True:
    print("\nWelcome to Emir ATM. System is launching...🤖\nPress 1 to Deposit Money\nPress 2 to Withdraw Money\nPress 3 to Transfer Money (Remittance)\nPress 4 to Check Balance\nPress 5 to Change PIN\nPress 6 to Contact Customer Representative\nPress 7 to Query Transaction History\nPress 8 to Create a New Card\nPress 9 to View Card Information\nPress 0 to Exit System. Have a nice day :)")
    selected_option = int(input("Please enter a choice (0-9): "))
    
    if selected_option < 0 or selected_option > 9:
        print("Invalid choice. Please press one of the given numbers.")
        
    elif selected_option == 1:
        iban_input = input("Please enter your IBAN: ")
        if iban_input in cards:
            user_data = cards[iban_input]
            amount = int(input("Enter the amount to deposit: "))
            user_data['balance'] += amount
            save_data() # Save the updated balance to file
            print("Transaction complete.")
            history_deposit.append(amount)
        else:
            print("No account found with this IBAN.")
            
    elif selected_option == 2:
        iban_input = input("Please enter your IBAN: ")
        if iban_input in cards:
            user_data = cards[iban_input]
            amount = int(input("Enter the amount to withdraw: "))
            if amount > user_data['balance']:
                print("The amount to withdraw cannot exceed your current balance.")
            else:
                user_data['balance'] -= amount
                save_data() # Save the updated balance to file
                history_withdraw.append(amount)
                print("Transaction successfully completed.")
        else:
            print("No account found with this IBAN.")
            
    elif selected_option == 3:
        sender_iban = input("Enter your IBAN: ")
        if sender_iban in cards:
            sender_card = cards[sender_iban]
            print(f"\nWelcome {sender_card['first_name']}, Current Balance: {sender_card['balance']}")
            receiver_iban = input("Enter the IBAN you want to transfer money to: ")
            if receiver_iban in cards:
                receiver_card = cards[receiver_iban]
                if sender_card == receiver_card:
                    print("You cannot transfer money to your own account.")
                else:
                    transfer_amount = int(input("Enter the transfer amount: "))
                    if sender_card['balance'] >= transfer_amount:
                        sender_card['balance'] -= transfer_amount
                        receiver_card['balance'] += transfer_amount
                        save_data() # Save both account updates to file
                        print(f"Transaction successful. {transfer_amount} has been successfully sent to {receiver_card['first_name']}.")
                        print(f"Your remaining balance is {sender_card['balance']}.")
                        history_transfer.append(transfer_amount)
                    else:
                        print("Transfer amount cannot exceed your balance.")
            else:
                print("No account found with the receiver's IBAN.")
        else:
            print("No account found with your IBAN.")
            
    elif selected_option == 4:
        iban_input = input("Please enter your IBAN: ")
        if iban_input in cards:
            print(f"\nYour card balance is: {cards[iban_input]['balance']}")
            history_balance_check += 1
        else:
            print("No account found with this IBAN.")
            
    elif selected_option == 5:
        iban_input = input("Enter your IBAN: ")
        if iban_input in cards:
            user_data = cards[iban_input]
            print("\nLogin Successful!")
            current_pin = int(input("Please enter your current PIN: "))
            if current_pin == user_data['pin']:
                new_pin = int(input("Enter your new PIN: "))
                
                # Check if this PIN is already used by another card in the system
                pin_exists = False
                for card_id in cards:
                    if cards[card_id]['pin'] == new_pin:
                        pin_exists = True
                        break
                        
                if pin_exists:
                    print("This PIN is currently being used by another account in the system. Please choose another PIN.")
                else:
                    user_data['pin'] = new_pin
                    save_data() # Save the new PIN to file
                    print("\nYour PIN has been successfully changed.")
                    history_pin_change.append(new_pin)
            else:
                print("\nYour current PIN was entered incorrectly.")
        else:
            print("Your IBAN does not exist in our system.")
            
    elif selected_option == 6:
        iban_input = input("Please enter your IBAN: ")
        if iban_input in cards:
            user_data = cards[iban_input]
            input_support_code = input("Enter your customer representative code: ")
            if input_support_code == user_data['support_code']:
                print("Connecting to your representative...")
                history_support_call += 1
            else:
                print("Representative code is incorrect.")
        else:
            print("Please make sure you entered the correct IBAN.")
            
    elif selected_option == 7:
        history_logs_check += 1
        print("\nCompiling your transaction history so far ⚙️.\nDeposit history:", history_deposit, "\nWithdraw history:", history_withdraw, "\nTransfer history:", history_transfer, "\nBalance check count:", history_balance_check, "\nPIN change history:", history_pin_change, "\nSupport call count:", history_support_call, "\nHistory query count:", history_logs_check, "\nCard creation count:", history_card_creation, "\nCard info check count:", history_card_info_check, "\nThis data represents the session log of this ATM. Have a good day.")
        
    elif selected_option == 8:
        print("\nStarting card creation process...")
        create_card()
        history_card_creation += 1
        
    elif selected_option == 9:
        iban_input = input("Please enter your IBAN: ")
        if iban_input in cards:
            user_data = cards[iban_input]
            print("Compiling card details...")
            print(f"""
            ===================================================================
            |       VIRTUAL CARD VIEW (DO NOT SHARE FOR YOUR SECURITY)         |
            ===================================================================
            |                                                                 |
            | NAME: {user_data['first_name']}         IBAN: {iban_input}                   |
            | SURNAME: {user_data['last_name']}      PIN: {user_data['pin']}              |
            | ID NO: {user_data['id_number']}         CVV: {user_data['cvv']}              |
            | BIRTHDATE: {user_data['birth_date']}   Balance: {user_data['balance']}      |
            | Support Code: {user_data['support_code']}   REPUBLIC OF TURKEY-K0938        |
            ===================================================================""")
            print("\nCard information successfully displayed.")
            history_card_info_check += 1
        else:
            print("Your IBAN could not be found.")
            
    elif selected_option == 0:
        print("\n\nSYSTEM IS SHUTTING DOWN⚙️⚙️")
        break
