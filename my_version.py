import math
import random

class Account:
    def __init__(self, account_number: int, customer_name: str, customer_address: str, balance: float):
        self._account_number = account_number
        self._balance = balance
        self._customer_name = customer_name
        self._customer_address = customer_address

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_info(self):
        print(f"Account {self._account_number} by {self._customer_name} ({self._customer_address}),"
              f" balance {self._balance}")

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: int, customer_name: str, customer_address: str, initial_balance: float) -> Account:
        account = Account(account_number, customer_name, customer_address, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: int) -> Account:
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")

class GenerateNumber:
    def generate(self) -> int:
        return math.floor(random.random() * 1000000)

class Customer:

    generate_account_number = GenerateNumber()

    def __init__(self, name: str, address: str, bank: Bank):
        self.name = name
        self.address = address
        self.bank = bank

    def open_account(self, initial_balance: float) -> Account:
        account_number = self.generate_account_number.generate()
        account = self.bank.create_account(account_number, self.name, self.address, initial_balance)
        return account

def banking_scenario():
      bank = Bank()
      customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
      customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)

      # Alice opens an account and deposits some money
      alice_account = customer1.open_account(initial_balance=500.0)
      alice_account.deposit(100.0)
      print(f"Alice's balance: {alice_account.get_balance()}")  # Alice's balance: 600.0

      # Bob opens an account and deposits some money
      bob_account = customer2.open_account(initial_balance=1000.0)
      bob_account.deposit(500.0)
      print(f"Bob's balance: {bob_account.get_balance()}")  # Bob's balance: 1500.0

      # Alice withdraws some money from her account
      alice_account.withdraw(300.0)
      print(f"Alice's balance: {alice_account.get_balance()}")  # Alice's balance: 300.0

      # Alice tries to withdraw more money than she has in her account
      try:
            alice_account.withdraw(500.0)
      except ValueError as e:
            print(e)  # Insufficient funds

      # Bank retrieves Alice's account using the account number
      retrieved_account = bank.get_account(alice_account.get_account_number())
      print(retrieved_account.get_info())   # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0

banking_scenario()