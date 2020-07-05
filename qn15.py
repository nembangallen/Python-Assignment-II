"""
15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""


class Customer:

    def __init__(self, name, mob_num, acc_num, acc_type, balance):
        self.name = name
        self.mob_num = mob_num
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.balance = balance

    def deposit_balnc(self, amount):
        self.balance = self.balance + amount

    def withdraw_balnc(self, amount):
        if (self.balance < amount):
            print('You don\'t have sufficient balance.')
        else:
            self.balance = self.balance - amount


customer1 = Customer('John Doe', '9802671522', '78677007812', 'Saving', 30000)
print('Account name: ' + customer1.name)
print('Account Number: '+customer1.acc_num)
print('Account Type: '+customer1.acc_type)
print('Mobile: '+customer1.mob_num)
print('Available Balance: '+str(customer1.balance))
customer1.deposit_balnc(10000)
print('After deposit: ' + str(customer1.balance))
customer1.withdraw_balnc(50000)
