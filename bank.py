class BankAccount:
    bank_balance = 0
    loan_feature_enabled = True
    total_loan_amount = 0
    accounts = {}

    def __init__(self, account_number, name, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to account {recipient_account.account_number}")
        else:
            print("Insufficient balance!")

    def take_loan(self):
        if self.loan_feature_enabled and self.balance > 0:
            loan_amount = 2 * self.balance
            self.balance += loan_amount
            self.total_loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        else:
            print("Loan feature is disabled or you don't have sufficient balance!")

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


class BankAdmin:
    def create_account(self, account_number, name, initial_deposit):
        if account_number in BankAccount.accounts:
            print("Account number already exists!")
            return None

        account = BankAccount(account_number, name, initial_deposit)
        BankAccount.accounts[account_number] = account
        return account

    def check_bank_balance(self):
        return BankAccount.bank_balance

    def check_total_loan_amount(self):
        return BankAccount.total_loan_amount

    def enable_loan_feature(self):
        BankAccount.loan_feature_enabled = True
        print("Loan feature is enabled.")

    def disable_loan_feature(self):
        BankAccount.loan_feature_enabled = False
        print("Loan feature is disabled.")


# Example usage:
admin = BankAdmin()

# Create user accounts
user1 = admin.create_account(10001, "Raisa", 7000)
user2 = admin.create_account(10002, "Totul", 9000)

# Deposit and withdraw money for user1
user1.deposit(2000)
user1.withdraw(1000)

# Transfer money from user1 to user2
user1.transfer(500, user2)

# Check balance for user1
print(user1.check_balance()) 

# Take a loan for user1
user1.take_loan()

# Check transaction history for user1
print(user1.get_transaction_history())

# Deposit and withdraw money for user2
user2.deposit(3000)
user2.withdraw(1000)

# Transfer money from user2 to user1
user2.transfer(300, user1)

# Check balance for user2
print(user2.check_balance())  # Output: 2900

# Take a loan for user2
user2.take_loan()

# Check transaction history for user2
print(user2.get_transaction_history())

# Admin actions
print(admin.check_bank_balance())
print(admin.check_total_loan_amount())
admin.disable_loan_feature()