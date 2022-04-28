# Python 3.10.1
# Aditya Sawant

from tkinter import *
from tkinter import messagebox
from util import *
import pymysql

def callNewAcc(root):
    from newAccount import newAccount
    newAccount(root)

def callNewLoan(root):
    from newLoan import newLoan
    newLoan(root)

def callShowAcc(root, stat):
    from showAccounts import showAccounts
    showAccounts(root, stat)

def callShowLoan(root, stat):
    from showLoans import showLoans
    showLoans(root, stat)
    
def managerHomePage(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("500x500+700+250")
    root.title("Banking System | Manager Home Page")
    root.config(bg = "pink")
    
    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: callHome(root))
    
    newAcc = Button(root, text = "Create Account", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)

    newLoan = Button(root, text = "New Loan", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)
    
    showAcc = Button(root, text = "Show Accounts", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)

    showLoan = Button(root, text = "Show Loans", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=4, width= 15)
    
    newAcc.configure(command = lambda: callNewAcc(root))
    newLoan.configure(command = lambda: callNewLoan(root))
    showAcc.configure(command = lambda: callShowAcc(root, "man"))
    showLoan.configure(command = lambda: callShowLoan(root, "man"))
    
    title.place(x = 130, y = 66)
    home.place(x = 10, y = 10)
    newAcc.place(x = 66, y = 166+18)
    newLoan.place(x = 266, y = 166+18)
    showAcc.place(x = 66, y = 266+48)
    showLoan.place(x = 266, y = 266+48)
    
    root.mainloop()



if __name__ == '__main__':
    managerHomePage(None)