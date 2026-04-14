# from day_1 import Vehicle

# Kế thừa có thể chứa toàn bộ thuộc tính và chức năng của class cha

# class Employee:
#     def __init__(self, age, position):
#         self.age = age
#         self.position = position

# class Car(Vehicle, Employee):
#     def __init__(self, name, color, type, wheels, slots, speed, age, position, fuel, price):
#         Vehicle.__init__(self, name, color, type, wheels, slots, speed)
#         Employee.__init__(self, age, position)

#         self.fuel = fuel
#         self.price = price

#     def information(self):
#         print("Fuel:", str(self.fuel))
#         print("Price:", str(self.price))
#         super().information()
    
#     #___str___: In ra object ở dạng string
#     def __str__(self):
#         return f"Name: {self.name}"

#     def __add__(self, object):
#         return self.age + object.age
# car1 = Car("Ferrari","red","super-car",4, 4,4,10, "leader", 1000, 3000)
# car2 = Car("BMW","black","luxury-car",5, 3, 200,30, "leader", 2000, 1500)
# print(car1 + car2)
# print(car)
# car.information()

#hw
#1 hcn
# class Rectangle:
#     def __init__(self, cd, cr):
#         self.cd = cd
#         self.cr = cr

#     def __str__(self):
#         return f"Rectangle object with height = {self.cd} and width = {self.cr}"

# rect = Rectangle(2, 1) 
# print(rect)

#2 Mathlist
# class MathList:
#     def __init__(self, values):
#         self.values = values
    
#     def __str__(self):
#         return str(self.values)

#     #Hàm dùng để thêm gtri vào list nl
#     def __add__(self, other):
#         for i in range(len(self.values)):
#             self.values[i] = self.values[i] + other
#         return self


#     def __sub__(self, other):
#         for i in range(len(self.values)):
#             self.values[i] = self.values[i] - other
#         return self

# mL = MathList([1, 2, 3, 4, 5])
# print(mL)
# mL += 2
# print(mL)

#3 Hv và hlp
# class Square:
#     def __init__(self, values):
#         self.values = values
    
#     #hàm dùng để viết int ra str
#     def __str__(self):
#         return str(self.values)
    
#     def cal_area(self):
#         self.values *= self.values
#         return self
    
# sq = Square(2)
# print("Square area: ", sq.cal_area())

# class Cube:
#     def __init__(self, values):
#         self.values = values

#     #hàm dùng để viết int ra str
#     def __str__(self):
#         return str(self.values)
    
#     def cal_area(self):
#         return ((self.values)**2)*6
    
#     def cal_volume(self):
#         return self.values**3

# cube = Cube(2)
# print("Cube area: ", cube.cal_area())
# print("Cube volume: ", cube.cal_volume())

#4 Tài khoản/ ý 2 chưa xong
# class User:
#     def __init__(self, tk, mk):
#         self.tk = tk
#         self.mk = mk
    
#     def welcome(self):
#         print(f"Welcome {self.tk}")
    
#     def check_password(self, password):
#         if self.mk == password:
#             return True
#         else:
#             return False

# user = User('mindx', '12345') 
# user.welcome() 
# print(user.check_password('1234')) 

# from datetime import datetime

# now = datetime.now()

    
# class SubscribedUser(User):
#     def __init__(self, tk, mk, date):
#         super().__init__(tk, mk)
#         SubscribedUser.__init__(self,tk, mk, date)
#         self.date = date

# s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1)) 
# s_user.welcome() 
