# Bank Account

A simple Python project for ACS 1111 that simulates a bank account using object-oriented programming.

The project defines a BankAccount class with attributes for the account holder's full name, account number, balance, and an optional account type. It also implements common banking operations such as deposit, withdraw (with overdraft fee), balance inquiry, interest calculation, and printing account statements.

## Assignment Mapping

This project satisfies the Bank Account assignment requirements by:

- Defining a `BankAccount` class in `bank_account.py`.
- Using attributes: `full_name`, `account_number` (8-digit, unique per run), and `balance` (starting at 0 by default).
- Implementing methods: `deposit`, `withdraw`, `get_balance`, `add_interest`, and `print_statement`.
- Creating three different BankAccount examples, including the required "Mitchell" account with account number `03141592` and the specified sequence of actions.

## Files

- `bank_account.py` - Main Python script that defines the BankAccount class and demonstrates its usage with several example accounts.

## How to Run

1. Make sure you have Python 3 installed.
2. In a terminal, navigate to this project folder.
3. Run the program:

   ```bash
   python bank_account.py
   ```

You should see example output for multiple accounts, including deposits, withdrawals, interest being added, and account statements.
