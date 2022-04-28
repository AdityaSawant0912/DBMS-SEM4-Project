# Python 3.10.1
# Aditya Sawant

from tkinter import *
from tkinter import messagebox
import pymysql
from manager import managerHomePage
from employee import employeeHomePage
import hashlib

# Utility Funtions
def showPassword(passwordText, show):

    if show == '•':
        passwordText.config(show="")
    else:
        passwordText.config(show="•")

def getHash(str):
    return hashlib.sha256(str.encode()).hexdigest()


# Database Functions
def getCursor():
    db = pymysql.connect(host="localhost", user="sakec",
                         passwd="sakec123", db="dbmslab")
    cursor = db.cursor()
    return db, cursor

def dbOne(sql):
    db, cursor = getCursor()
    cursor.execute(sql)
    data = cursor.fetchone() 
    db.commit()
    return data

def ifUserExists(user_name, userType):
    db, cursor = getCursor()
    cursor.execute(f"""SELECT * FROM {userType} WHERE {userType}_name = "{user_name}"; """)
    data = cursor.fetchone()
    db.commit()
    # data = None
    if data == None:
        return False
    else:
        return True

def getPassword(user_name, userType):
    db, cursor = getCursor()
    cursor.execute(f"""SELECT {userType}_password FROM {userType} WHERE {userType}_name = "{user_name}"; """)
    data = cursor.fetchone()
    db.commit()
    return data[0]


def login(user_name, password, userType):
    if(user_name == '' or password == ''):
        return False
    if ifUserExists(user_name, userType):
        if getHash(password) == getPassword(user_name, userType):
            messagebox.showinfo("Success", "Login successful.")
            return True
        else:
            messagebox.showerror("Error", "Incorrect password.")
            return False
    else:
        messagebox.showerror("Error", "User does not exist.")
        return False

def doEmployeeLogin(root, user_name, password):
    if(login(user_name, password, "employee")):
        employeeHomePage(root)

def doManagerLogin(root, user_name, password):
    if(login(user_name, password, "manager")):
        managerHomePage(root)

def managerLoginPage(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("500x400+700+250")
    root.title("Banking System | Manager Login Page")
    root.config(bg = "pink")
    
    usernameTextVar = StringVar()
    passwordTextVar = StringVar()
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: homePage(root))
    
    title = Label(root, text = "Login Page", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    usernameLable = Label(root, text = "Username", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    usernameText = Entry(root,textvariable= usernameTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    
    passwordLable = Label(root, text = "Password", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    passwordText = Entry(root,textvariable= passwordTextVar ,font = ("Dosis", 15), bg = "lightblue", fg = "black", show="•",  width=20)
    
    passwordShow = Button(root, text = "Show", relief=FLAT, font = ("Arial", 9), bg = "lightblue", command= lambda: showPassword(passwordText, passwordText.cget('show')))
    
    loginBtn = Button(root, text = "Login", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=2, width= 10, command = lambda : doManagerLogin(root, usernameText.get(), passwordText.get()))
    
    home.place(x = 10, y = 10)
    title.place(x = 160, y = 35)
    usernameLable.place(x = 133, y = 110)
    usernameText.place(x = 133, y = 140)
    passwordLable.place(x = 133, y = 190)
    passwordText.place(x = 133, y = 220)
    passwordShow.place(x =320 + 133 - 66, y = 220)
    loginBtn.place(x = 190, y = 290)
    root.mainloop()

def employeeLoginPage(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("500x400+700+250")
    root.title("Banking System | Employee Login Page")
    root.config(bg = "pink")
    
    usernameTextVar = StringVar()
    passwordTextVar = StringVar()
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: homePage(root))
    
    title = Label(root, text = "Login Page", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    usernameLable = Label(root, text = "Username", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    usernameText = Entry(root,textvariable= usernameTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    
    passwordLable = Label(root, text = "Password", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    passwordText = Entry(root,textvariable= passwordTextVar ,font = ("Dosis", 15), bg = "lightblue", fg = "black", show="•",  width=20)
    
    passwordShow = Button(root, text = "Show", relief=FLAT, font = ("Arial", 9), bg = "lightblue", command= lambda: showPassword(passwordText, passwordText.cget('show')))
    
    loginBtn = Button(root, text = "Login", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=2, width= 10, command = lambda : doEmployeeLogin(root, usernameText.get(), passwordText.get()))
    
    home.place(x = 10, y = 10)
    title.place(x = 160, y = 35)
    usernameLable.place(x = 133, y = 110)
    usernameText.place(x = 133, y = 140)
    passwordLable.place(x = 133, y = 190)
    passwordText.place(x = 133, y = 220)
    passwordShow.place(x =320 + 133 - 66, y = 220)
    loginBtn.place(x = 190, y = 290)
    root.mainloop()

def homePage(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("500x400+700+250")
    root.title("Banking System | Home Page")
    root.config(bg = "pink")
    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    manager = Button(root, text = "Manager Login", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)

    employee = Button(root, text = "Employee Login", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)
    
    manager.configure(command = lambda: managerLoginPage(root))
    employee.configure(command = lambda: employeeLoginPage(root))
    
    title.place(x = 130, y = 66)
    manager.place(x = 66, y = 166+18)
    employee.place(x = 266, y = 166+18)
    
    root.mainloop()


if __name__ == '__main__':
    homePage(None)