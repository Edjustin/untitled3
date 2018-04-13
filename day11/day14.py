# class Person():
#     def __init__(self,  name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        #普通方法
#     def show_age(self):
#         print(self.age)
#
#     def show_sex(self):
#         print(self.sex)
#
# if __name__ == '__main__':
#     person = Person('周勇', 18, 'man')
#     print(person.name)

# class Employee():
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
#
#     def show(self):
#         print(self.name, self.id, self.salary)
#
# if __name__ == '__main__':
#     employee = Employee('周勇', 110, 30000)
#     shengxuan = Employee('程圣轩', 120, 31000)
#     employee.show()
#     shengxuan.show()

# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print(self.name + ":在说话")
#
#     def run(self):
#         print(self.name + ':带着小姨子跑路了')
#
#
# if __name__ == '__main__':
#     person = Person('小明')
#     print(person.name)
#     person.say()
#     person.run()


# class BankCard():
#     def __init__(self, account, balance):
#         self.account = account
#         self.balance = balance
#
#     def deposit(self):
#         if money > 0:
#         self.balance += deposit
#           else:
#               print ('请重新输入金额')
#         print(self.balance)
#
#     def withdrawal(self, money):
#         withdrawal = int(input('请输入取款金额:\n'))
#         if money > 0  self.balance >= money:
#             self.balance -= money
#         else:
#             print('请重新输入金额')
#
#     def transfer(self, bank_card, money):
#         if money > 0 and self.balance > 0 and self.balance >= money:
#             self.balance -= money
#             bank_card.balance += money
#         else:
#             print('余额不足')
#
#
# if __name__ == '__main__':
#     bankcard = BankCard('123456', 10000)
#       deposit = int(input('请输入存款金额:\n'))
#     bankcard.deposit()
#     bankcard.withdrawal()
#     bankcard.transfer()


# class Phone():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def show_info(self):
#         print('手机品牌:{brand}\n手机型号:{model}'.format(brand=self.brand, model=self.model))
#
#     def call(self):
#         print(self.brand + ':Hello,你好')
#
#
# if __name__ == '__main__':
#     phone = Phone('诺基亚', 'N86')
#     phone.show_info()
#     phone.call()


# class Student():
#     def __init__(self, name, age, schoolname):
#         self.name = name
#         self.age = age
#         self.schoolname = schoolname
#
#     def eat(self):
#         print(self.name + ':吃屎去吧你')
#
#     def study(self):
#         print(self.name + ':在书房安静的看书')
#
#
# if __name__ == '__main__':
#     student = Student('小明', 20, '哈弗')
#     student.eat()
#     student.study()


# class Road():
#     def __init__(self, roadname, roadlen):
#         self.roadname = roadname
#         self.roadlen = roadlen
#
#
# if __name__ == '__main__':
#     road = Road('软件园路', '1800千米')
#
#
# class Car():
#     def __init__(self, carname, speed):
#         self.carname = carname
#         self.speed = speed
#
#     def get_time(self,road_len):
#         time = road_len / self.speed
#         print(time)
#         return time
#
#
# if __name__ == '__main__':
#     road = Road('智慧园路', 9000)
#     car = Car('奥迪A6', 300)
#     i = car.get_time(road)
#     print(i)


from functools import reduce
li = [1, 2, 3, 4, 5, 6]
def fun(x, y):
    return x + y

value = reduce(lambda x, y: x + y, li)
print(value)


def func(x):
    return '杜佩' in x

li = ['1']
f = filter(func, li)
print(list(f))













