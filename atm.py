class Atm:
    balance = 750


    def __init__(self,pin):
        self.pin = pin

        

    def withdrawal(self):
        amount = eval(input("Enter amount: "))
        self.balance = self.balance - amount
        print("The amount withdrawn  is ", amount, "\nYour new balance is ", d.balance)
        print("Transaction successful.")


    def deposit(self):
        amount = eval(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Your deposited amount is ", amount, "\n Your new balance is ", d.balance)
        print("Transaction successful.")

    def Atmpin(self):
        pin = input("Enter pin to proceed: ")
        if len(pin) == 4:
            return
        else:
            print("Enter correct pin")
                     
    def getBalance(self):
        self.balance = self.balance
        choose = eval(input("Choose account. \n1:Savings \n2: current \nEnter: "))
        if choose == 1:
            print(self.balance)
        else:
            print("service not available")

    def transfer(self):
        amount = eval(input ("Enter amount to transfer: "))
        self.balance = self.balance - amount
        d1.balance = d1.balance + amount 
        print("Verify amount to transfer:", amount)
        enter = input("Press enter to proceed")
        print("Transaction successful")

    def AtmProcess(self):
        print("Hello welcome to Ecobank \n Atm services.")
        print("Quick reminder \nCards expiring from March 2020 will be renewed for use due to the COVID -19")
        d.Atmpin()
        choice = eval(input("Choose Service \n1: Deposit \n2: Witdrawal: \n3 Check balance \n4:Transfer \nEnter: "))
        if choice == 1:
             d.deposit()
        elif choice ==2:
            d.withdrawal()
        elif choice == 3:
            d.getBalance()
        elif choice ==4:
            d.transfer()

        else:
            print("you have entered a wrong number.")


d = Atm(2323)
d1 = Atm(3434)

d.AtmProcess()

