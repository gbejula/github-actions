from bank_accounts import *

Ibukun = BankAccount(1000, "Ibukun")
David = BankAccount(2000, "David")

Ibukun.getBalance()
David.getBalance()

Ibukun.deposit(750)

Ibukun.withdraw(10000)
Ibukun.withdraw(50)

Ibukun.transfer(10000, David)
Ibukun.transfer(100, David)

Kunle = InterestRewardsAcct(1000, "Kunle")

Kunle.getBalance()

Kunle.deposit(100)

Kunle.transfer(100, Ibukun)

Bola = SavingsAccount(1000, "Bola")

Bola.getBalance()

Bola.deposit(100)

Bola.transfer(10000, David)
Bola.transfer(1000, David)