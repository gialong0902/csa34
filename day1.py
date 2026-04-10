#1: Giới thiệu nhân viên
# class Employee:
#     def __init__(self, tenNv, vtlv):
#         self.tenNv = tenNv
#         self.vtlv = vtlv
    
#     def say_hi(self):
#         print("Hi, my name is", str(self.tenNv) + ".")
    
#     def tell_position(self):
#         print("I am a", str(self.vtlv))

# john = Employee("John", "Software Engineer.")
# john.say_hi()
# john.tell_position()

#2: Hình học
# class Rectangle:
#     def __init__(self, cd, cr):
#         self.cd = cd
#         self.cr = cr
    
#     def Perimeter(self):
#         cv = (self.cd + self.cr)*2
#         print("=> Perimeter:", cv)
#     def Area(self):
#         dt = self.cd * self.cr
#         print("=> Area:", dt)
    

# class Circle:
#     def __init__(self, r):
#         self.r = r
    
#     def perimeter(self):
#         cv = self.r*2*3.14
#         print("=> Perimeter:", cv)
#     def area(self):
#         dt = self.r**2*3.14
#         print("=> Area:", dt)

# text = input("Shape (rectangle|circle):")
# if text == "rectangle":
#     height = int(input("Height: "))
#     width = int(input("Width: "))

#     a = Rectangle(height, width)
#     a.Perimeter()
#     a.Area()
# elif text == "circle":
#     radius = int(input("Radius: "))

#     b = Circle(radius)
#     b.perimeter()
#     b.area()
# else:
#     print("=> Invalid!")

#3 Ngày tháng
# from datetime import datetime 
 
# now = datetime.now() 

# class CustomDate:
#     def __init__(self, date, time):
#         self.date = date
#         self.time = time

#     def get_date(self):
#         self.date = now.strftime("%d/%m/%Y")
#         print(self.date)
    
#     def get_time(self):
#         self.time = now.strftime("%H:%M:%S")
#         print(self.time)
# a = CustomDate("", "")
# a.get_date()
# a.get_time()

#4 DateHandler
# from datetime import datetime

# class DateHandler:
#     def __init__(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date
    
#     def format_date(self, date):
#         return date.strftime("%d/%m/%Y")
    
#     def get_days_between(self, start_date, end_date):
#         gap = self.end_date - self.start_date
#         return gap.days

# start_date = datetime(2021, 1, 1) 
# end_date = datetime(2022, 1, 1) 

# a = DateHandler(start_date, end_date)
 
# print("Start:", a.format_date(start_date)) 
# print("End:", a.format_date(end_date)) 
# print("Days between:", a.get_days_between(start_date, end_date)) 
