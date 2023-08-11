from OOPS_day3_4 import SIB
class bank:

    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show you your account open status ")

    def deposit(self):
        print("this will show your deposited amount")

    def test(self):
        print("this is a test method from bank class")
class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happened to icici through hdfc")

    def test(self):
        print("this is a test method from HDFC_bank class")

class ineuron_bank:
    def account_status_icici(self):
        print("print an account status in icici")
class icici(bank,HDFC_bank,ineuron_bank,SIB):
    pass



i = icici()
i.deposit()
i.account_opening()
i.transaction()
i.hdfc_to_icici()
i.test()
i.account_status_icici()
i.transactions_list()
