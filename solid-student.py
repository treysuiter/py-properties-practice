# class Product():

#     @property  # The getter
#     def price(self):
#         try:
#             return self.__price  # Note there are 2 underscores here
#         except AttributeError:
#             return 0

#     @price.setter  # The setter
#     def price(self, new_price):
#         if type(new_price) is float:
#             self.__price = new_price
#         else:
#             raise TypeError(
#                 'Please provide a floating point value for the price')

# Practice: Solid Student
# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.
# Practice: Convert Student Object to a String


class Student():

    @property
    def firstName(self):
        try:
            return self.__firstName
        except AttributeError:
            return "No First Name Entered"

    @firstName.setter
    def firstName(self, firstName):
        if type(firstName) is str:
            self.__firstName = firstName
        else:
            print("Please input first name as a string value.")

    @property
    def lastName(self):
        try:
            return self.__lastName
        except AttributeError:
            return "No Last Name Entered"

    @lastName.setter
    def lastName(self, lastName):
        if type(lastName) is str:
            self.__lastName = lastName
        else:
            print("Please input first name as a string value.")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return "No Age Entered"

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            print("Please enter an integer for value of age.")

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return "No Cohort Entered"

    @cohort.setter
    def cohort(self, cohort):
        if type(cohort) is int:
            self.__cohort = cohort
        else:
            print("Please enter an integer for value of cohort.")

    @property
    def fullName(self):
        try:
            return(f"{self.__firstName} {self.__lastName}")
        except AttributeError:
            return "Full Name Not Entered"
   


fred = Student()
fred.firstName = "fred"
fred.lastName = "smith"
fred_fullName = fred.fullName
print(fred_fullName)
