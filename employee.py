# Python 3.10.1
# Aditya Sawant

from tkinter import *
from tkinter import messagebox
import pymysql
from util import callHome

def callShowAcc(root, stat):
    from showAccounts import showAccounts
    showAccounts(root, stat)

def callShowLoan(root, stat):
    from showLoans import showLoans
    showLoans(root, stat)

def employeeHomePage(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("500x400+700+250")
    root.title("Banking System | Employee Home Page")
    root.config(bg = "pink")
    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: callHome(root))
    
    manager = Button(root, text = "Show Accounts", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)

    employee = Button(root, text = "Show Loans", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)
    
    manager.configure(command = lambda: callShowAcc(root, "emp"))
    employee.configure(command = lambda: callShowLoan(root, "emp"))
    
    title.place(x = 130, y = 66)
    home.place(x = 10, y = 10)
    manager.place(x = 66, y = 166+18)
    employee.place(x = 266, y = 166+18)
    
    root.mainloop()


if __name__ == '__main__':
    employeeHomePage(None)