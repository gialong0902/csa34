import sqlite3

conn = sqlite3.connect("C:\\Users\\longt\\Downloads\\csa\\Buoi_3\\homework.db")
print(conn)

cursor = conn.cursor()

data = [
    {"id": 4, "name": "Alice"},
    {"id": 5, "name": "Bob"},
    {"id": 6, "name": "Charlie"},
    {"id": 7, "name": "David"},
    {"id": 8, "name": "Emma"}
]

values = ""


for i in range(len(data)): # chạy liên tục từ 0 -> len(data)
    if i < len(data) - 1: # kiểm tra nếu lặp chạy đến = len(data) -1 thì print else để xóa ","
        values = values + f"({data[i]["id"]}, '{data[i]["name"]}')" + ","
    else:
        values = values + f"({data[i]["id"]}, '{data[i]["name"]}')"

# print(values)

# for i in range(0, len(data)):
#     print(data[i]["id"], data[i]["name"])


# cursor.execute("""
#     Create table users(
#         id number,
#         name varchar(255)
               
#     )
# """)



# cursor.execute("""Insert into users (id, name)
#             values
#             (1, 'Gia Long'),
#             (2, 'Tung Anh')
               
#         """)

# cursor.execute(f"""Insert into users (id, name) values {values}""")

# Lấy ra dữ liệu trong 
cursor.execute("Select * from users")
output = cursor.fetchall()
# print(output)
# for val in output:
#     print(val)

# usernameInput = input("Enter username you want to to add password: ")

# for val in output:
#     if val[1] == usernameInput:
#         passwordInput = input(f"Enter password for users {usernameInput}")
#         # cursor.execute(f"Insert into users (password) values ('{passwordInput}')")
#         cursor.execute(f"Update users set password = '{passwordInput}' where name = '{usernameInput}'")
#     else:
#         print("Username is not existed")


conn.commit()


# Thêm 1 cột password
# Dùng input để định nghĩa password cho 1 user có name nằm trong bảng

# a = input("Nhập vào 1 tên user: ")
# cursor.execute("Select * from users")
# output = cursor.fetchall()
# print(output)
#hàm cursor dùng để chạy lệnh sql

#HW làm đăng nhập đăng ký
def register():
    name = input("Enter username: ")

    password = input("Enter password: ")

    #ktra username tồn tại chx
    cursor.execute(
        "SELECT * FROM users WHERE name = ?",
        (name,)
    )

    user = cursor.fetchone()

    if user is not None:
        print("Username alr exists")
    else:
        cursor.execute(
            "INSERT INTO users(name,password) VALUES(?,?)",
            (name,password)
        )

    conn.commit()
    print("Register successful!")

def login():
    name = input("Enter username: ")

    password = input("Enter password: ")
    cursor.execute(
        "SELECT * FROM users WHERE name = ? AND password = ?",
        #Lấy vào cột user và pass
        (name, password)
    )
    #lấy gtri đầu của dãy
    user = cursor.fetchone()

    if user is not None:
        print("Login Succesful!")
    else:
        print("Wrong username or password")
#MENU


while True:
    print("===Menu===")
    print("1. register")
    print("2. login")
    print("3. Exit")
    
    choice = int(input(""))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        break
    else:
        print("There's no option for that!")
        print("Please choose again.")
    continue

conn.close()