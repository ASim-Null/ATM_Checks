balance = 100
pin_valid = 000
pin = int(input("Please insert pin: "))

def check_pin():
    count = 0
    while count < 3:
            if pin == pin_valid:
                print("Pin Code Valid")
                print("Access Granted")
                break
            else:
                count += 1
                print(input("Invalid Pin, Try Again: "))
                if count == 2:
                    print("Pin limit reached")
                    exit()

check_pin()

#Simulate Cash Withdrawal
withdrawal_amount = float(int(input("How much would you like to withdraw?: £")))
up_balance = 0

def new_balance():
    try:
        if withdrawal_amount > balance:
            raise Exception
        up_balance = balance - withdrawal_amount
        print(f"Withdrawal succesful. Balance is now £{up_balance}")
    except:
        print("Withdrawal limit exceeds balance.")
    else:
        print("Thank you for using This Fake Bank!")

new_balance()
