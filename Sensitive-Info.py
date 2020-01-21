class Patient:

    def __init__(self, ssn, dob, acct_num, first_name, last_name, address):

        self.__ssn = ssn
        self.__dob = dob
        self.__acct_num = acct_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return "Cannot set SSN"

    @property
    def dob(self):
        return self.__dob

    @property
    def acct_num(self):
        return self.__acct_num

    @property
    def first_name(self):
        return "Nothing"

    @property
    def last_name(self):
        return "Nothing"

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            print("Please enter a string value for address")
       


fred = Patient("111-22-3333", "08-01-2001", "998877", "Fred", "Flip", "999 Elm St.")

# fred.ssn = "999-99-9999"
# fred.dob = "08-01-2002"
# print(fred.ssn)
# print(fred.dob)
# print(fred.first_name)
# print(fred.last_name)
# print(fred.full_name)

print(fred.address)

fred.address = "111 Pine St."

print(fred.address)