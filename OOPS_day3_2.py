class bank:

    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show you your account open status ")

    def deposit(self):
        print("this will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction happened to icici through hdfc")

class icici(HDFC_bank):
    pass

i = icici()
print(i.deposit())
print(i.hdfc_to_icici())
print(i.transaction())
print(i.account_opening())
