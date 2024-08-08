class ATM:
    def __init__(self, bills) -> None:
        self.bills = bills
        self.max_login = 3
        self.login_attempts = 0
        self.logged_in = False

    def login(self, pin):
        if pin == "123456":
            self.logged_in = True
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_login:
                self.lock_account()
            return False

    def lock_account(self):
        self.logged_in = False
        print("Account locked due to too many failed login attempts.")

    def check_money(self):
        total_money = sum(denomination * count for denomination, count in self.bills.items())
        return total_money

    def withdraw(self, amount):
        if amount > self.check_money():
            return "Insufficient funds"
        
        bills_copy = self.bills.copy()
        for denomination in sorted(bills_copy.keys(), reverse=True):
            while amount >= denomination and bills_copy[denomination] > 0:
                amount -= denomination
                bills_copy[denomination] -= 1
        
        if amount > 0:
            return "Unable to dispense the exact amount"
        
        self.bills = bills_copy
        return "Withdrawal successful"

    def display_menu(self):
        while True:
            print("Check money press 1")
            print("Withdraw money press 2")
            print("Exit press 3")
            mode = int(input("Enter your choice: "))

            if mode == 1:
                print(f"Total money available: {self.check_money()}")
            elif mode == 2:
                amount = int(input("Enter amount to withdraw: "))
                print(self.withdraw(amount))
                print(f'Total money balance: {self.check_money()}')
            elif mode == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

atm = ATM({
    1000: 1,
    500: 7,
    100: 5
})

while not atm.logged_in:
    pin = input("Enter your PIN: ")
    if not atm.login(pin):
        if atm.login_attempts >= atm.max_login:
            break
        else:
            print("Login Failed. Try again.")

if atm.logged_in:
    atm.display_menu()
