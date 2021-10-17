class Atm(object):
    def __init__(self,card,pin):
        self.card = card
        self.pin = pin


    def cashWithdrawl(self,amount):
        newAmount = 50000 - amount
        print("you have withdrawn amount " + str(amount)+ " euros. your remaining balance is " + str(newAmount))
   
    def balanceEnquiry(self):
        print("your balance is 50000")

atm = Atm("credit",1234)
atm.cashWithdrawl(500)
atm.balanceEnquiry()
