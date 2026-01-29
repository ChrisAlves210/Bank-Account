import random


class BankAccount:
    """A simple bank account model with basic operations."""

    # Class-level set to track used account numbers (for uniqueness in this run)
    _used_account_numbers = set()

    def __init__(self, full_name: str, account_number: str | None = None, initial_balance: float = 0.0,
                 account_type: str = "checking"):
        self.full_name = full_name
        self.account_type = account_type.lower()

        if account_number is None:
            self.account_number = self._generate_account_number()
        else:
            # Store as zero-padded 8-character string
            self.account_number = str(account_number).zfill(8)
            BankAccount._used_account_numbers.add(self.account_number)

        self.balance = float(initial_balance)

    @classmethod
    def _generate_account_number(cls) -> str:
        """Generate a unique 8-digit account number as a string."""
        while True:
            number = f"{random.randint(0, 99999999):08d}"
            if number not in cls._used_account_numbers:
                cls._used_account_numbers.add(number)
                return number

    @property
    def monthly_interest_rate(self) -> float:
        """Return the monthly interest rate based on account type."""
        # Base requirement: 1% annually → approx 0.00083 monthly
        base_rate = 0.00083
        # Stretch: savings account gets higher interest (≈1% per month)
        if self.account_type == "savings":
            return 0.01
        return base_rate

    def deposit(self, amount: float) -> None:
        """Deposit money into the account and print the result."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account, handling overdrafts."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            # Overdraft fee of $10
            self.balance -= 10
            print(f"Overdraft fee charged. New balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

    def get_balance(self) -> float:
        """Print and return the current balance."""
        print(f"{self.full_name}, your current balance is: ${self.balance:.2f}")
        return self.balance

    def add_interest(self) -> None:
        """Add monthly interest to the balance.

        Uses the formula: interest = balance * 0.00083 for checking accounts,
        and a higher rate for savings accounts.
        """
        interest = self.balance * self.monthly_interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f} new balance: ${self.balance:.2f}")

    def print_statement(self) -> None:
        """Print a simple account statement with masked account number."""
        masked_number = "****" + self.account_number[-4:]
        print(self.full_name)
        print(f"Account No.: {masked_number}")
        print(f"Balance: ${self.balance:.2f}")
        print("-")


if __name__ == "__main__":
    # Example 1: Checking account with randomly generated account number
    account1 = BankAccount(full_name="Alice Johnson")
    account1.deposit(250.00)
    account1.withdraw(50.00)
    account1.add_interest()
    account1.print_statement()

    # Example 2: Savings account with random account number
    account2 = BankAccount(full_name="Bob Smith", account_type="savings")
    account2.deposit(1000.00)
    account2.add_interest()
    account2.get_balance()
    account2.withdraw(1200.00)  # This will trigger overdraft
    account2.print_statement()

    # Example 3: Required "Mitchell" example with specific account number 03141592
    mitchell_account = BankAccount(full_name="Mitchell", account_number="03141592")

    # Deposit $400,000 into Mitchell's account
    mitchell_account.deposit(400_000.00)

    # Print a statement
    mitchell_account.print_statement()

    # Add interest to the account
    mitchell_account.add_interest()

    # Print a statement
    mitchell_account.print_statement()

    # Make a withdrawal of $150
    mitchell_account.withdraw(150.00)

    # Print a statement
    mitchell_account.print_statement()
