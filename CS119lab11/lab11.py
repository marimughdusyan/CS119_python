# Mari Mughdusyan
# CS119 programming in Python
# Chapter 11 lab
# Employee and ProductionWorker Classes

class Employee:
    # Attributes of the super class
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    # set and get attributes
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number


# subclass of the superclass Employee
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        Employee.__init__(self, name, id_number)
        # attributes of subclass
        self._shift_number = shift_number
        self._pay_rate = pay_rate

    # set and get attributes of the subclass
    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def get_shift_number(self):
        return self._shift_number

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate

    def get_pay_rate(self):
        return self._pay_rate

def main():
    # user input attributes
    name = input("Enter your name: ")
    id = int(input("Enter your ID: "))
    shift_num = int(input("Enter shift number: "))
    # check if shift number is correct 1,2 or 3
    while shift_num > 3 or shift_num < 1:
        shift_num = int(input("Please enter shift number 1,2 or 3: "))
    pay_rate = float(input("Enter pay rate: "))

    # create an object with input values
    productionWorker1 = ProductionWorker(name,id, shift_num, pay_rate)

    # Display the attributes of the object
    print("\nEMPLOYEE INFORMATION")
    print("====================\n")

    print(f"Name: {productionWorker1.get_name()}")
    print(f"ID Number: {productionWorker1.get_id_number()}")
    print(f"Pay Rate: {productionWorker1.get_pay_rate()}")
    print(f"Sift Number: {productionWorker1.get_shift_number()}")

# call main function
if __name__ == "__main__":
    main()


# output example

# Enter your name: Mari
# Enter your ID: 1234
# Enter shift number: 5
# Please enter shift number 1,2 or 3: 3
# Enter pay rate: 3.3
#
# EMPLOYEE INFORMATION
# ====================
#
# Name: Mari
# ID Number: 1234
# Pay Rate: 3.3
# Sift Number: 3