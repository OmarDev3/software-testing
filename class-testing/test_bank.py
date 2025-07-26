import pytest
from bank_class import BankAccount
from datetime import datetime

#1. Account Creation Tests
#Test 1	Create an account with a valid initial balance
def test_create_account_with_valid_balance():
    account3 = BankAccount("Omar",100)
    assert account3.check_balance() == 100

#Test 2	Attempt to create an account with a negative balance (should raise ValueError)
def test_create_account_with_invalid_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        account4=BankAccount("Ahmed",-50)

#Test 3	Ensure the account holder's name is stored correctly
def test_check_holder_name_correct():
    account5=BankAccount("Ali",500)
    assert account5.account_holder == "Ali"


#2. Deposit Tests
#Test 1	Deposit a valid amount successfully
def test_desposit_valid_amount():
    account6 = BankAccount("Mohammed",100)
    account6.deposit(100)
    assert account6.check_balance() == 200

#Test 2	Attempt to deposit zero (should raise ValueError)
def test_desposite_zero():
    account7 = BankAccount("Talal",100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account7.deposit(0)

#Test 3	Attempt to deposit a negative amount (should raise ValueError)
def test_desposite_negative_amount():
    account8 = BankAccount("Fasial", 500)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account8.deposit(-100)


#3. Withdrawal Tests
#Test 1	Withdraw an amount successfully
def test_withdraw_valid_amount():
    account9 = BankAccount("Abdulla", 200)
    account9.withdraw(100)
    assert account9.check_balance() == 100

#Test 2	Attempt to withdraw more than available balance (should raise ValueError)
def test_withdraw_more_available_balance():
    account10= BankAccount("Ebrahim", 500)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account10.withdraw(700)

#Test 3	Attempt to withdraw zero or negative amount (should raise ValueError)
def test_withdraw_zero_or_negative_amount():
    account11 = BankAccount("Hamad",200)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account11.withdraw(-100)


#4. Transfer Tests
#Test 1	Transfer an amount successfully
def test_transfer_valid_amount():
    account12 = BankAccount("Hessa",800)
    account13 = BankAccount("Maryam",10)
    account12.transfer(account13,20)

    assert account12.check_balance() == 780

#Test 2	Attempt to transfer more than available balance (should raise ValueError)
def test_transfer_more_availavle_balance():
    with pytest.raises(ValueError, match="Insufficient funds"):
        account14 = BankAccount("Haya",20)
        account15 = BankAccount("Layla",40)
        account14.transfer(account15,40)

#Test 3	Attempt to transfer to a non-BankAccount object (should raise TypeError)
def test_transfer_non_bankAccount():
    with pytest.raises(TypeError, match="Recipient must be a BankAccount instance"):
        account16 = BankAccount("Lamya",20)
        account17 = ""
        account16.transfer(account17,40)


#5. Transaction History Tests
#Test 1	Ensure transactions are recorded correctly
def test_check_transactions():
    account18 = BankAccount("Amina",300)
    account18.deposit(20)
    account18.withdraw(10)

    transactions=account18.get_transaction_history()

    assert transactions[0]['type'] == "Account Created"
    assert transactions[1]['type'] == "Deposit"
    assert transactions[2]['type'] == "Withdrawal"

#Test 2	Verify transaction history contains correct details
def test_check_transation_history():
    account19 = BankAccount("Jassim",500)
    account19.deposit(200)
    account19.deposit(30)

    transactions=account19.get_transaction_history()
    assert transactions[1]['amount'] == 200

#Test 3	Ensure transaction timestamps are present
def test_check_transaction_timestamps_present():
    account24 = BankAccount("Yasser", 200)
    account24.deposit(100)
    transactions = account24.get_transaction_history()
    assert len(transactions) > 0
    for transaction in transactions:
        assert "timestamp" in transaction
        assert isinstance(transaction["timestamp"], datetime)