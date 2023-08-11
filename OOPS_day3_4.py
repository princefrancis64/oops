class SIB:
    def transactions_list(self):
        print("this shows the transaction list from SIB bank")


class ineuron:
    def student(self):
        print("print the details of all the students")

    def acheivers(self):
        print("print the list of all the acheivers")

    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):
    def student(self):  #method over riding
        print("these are the filtered student list")

iv = ineuron_vision()
iv.student()