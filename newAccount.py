from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from util import *
import pymysql
from random import randint

# Database Functions
def getCursor():
    db = pymysql.connect(host="localhost", user="sakec",
                         passwd="sakec123", db="dbmslab")
    cursor = db.cursor()
    return db, cursor

def accExists(accNo):
    db, cursor = getCursor()
    cursor.execute(f"""SELECT * FROM account WHERE acc_no = "{accNo}"; """)
    data = cursor.fetchone()
    db.commit()
    if data == None:
        return False
    else:
        return True

def submitData(root, accno, accType, accIntr, custName, custAdd, custPh, accBranch=1, accBal=0):
    print(accno, accType, accIntr, custName, custAdd, custPh, accBranch, accBal)
    try:
        custPh = int(custPh)
    except(Exception):
        messagebox.showerror("Error", "Phone number must be a number")
        return
    db, cursor = getCursor()
    print(accno, accType, accIntr)
    try:
        cursor.execute(f"""INSERT INTO account VALUES("{accno}", "{accType}", "{accIntr}", "{accBal}", "{accBranch}");""")
        cursor.execute(f"""INSERT INTO customer (`name`, `address`, `ph_no`) VALUES("{custName}", "{custAdd}", "{custPh}");""")
    except():
        messagebox.showerror("Error", "Database Error")
        return
    finally:
        db.commit()
        messagebox.showinfo("Success", "Account Added Successfully")
        callManager(root)
    

def getAccNo():
    # return 10 digit random no.
    nos = ['0','1','2','3','4','5','6','7','8','9']
    accNo = []
    accNo.append(nos[randint(1,9)])
    for i in range(4): 
        accNo.append(nos[randint(0,9)])
        
    if accExists(''.join(accNo)):
        getAccNo()
    else:
        return ''.join(accNo)

def newAccount(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("800x500+500+250")
    root.title("Banking System | Create New Account")
    root.config(bg = "pink")
    
    accNoTextVar = IntVar()
    accNoTextVar.set(int(getAccNo()))
    
    accTypeTextVar = StringVar()
    accIntrTextVar = IntVar()
    accIntrTextVar.set(7)
    
    
    custNameTextVar = StringVar()
    custAddTextVar = StringVar()
    custPhTextVar = StringVar()
    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: callManager(root))
    
    # Account Details
    
    accNoLable = Label(root, text = "Account Number", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accNoText = Entry(root,textvariable= accNoTextVar,  font = ("Dosis", 15), bg = "lightblue", state='readonly', fg = "black")
    
    accTypeLable = Label(root, text = "Account Type", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accTypeText = Combobox(root,textvariable= accTypeTextVar,  font = ("Dosis", 15), state='readonly', values=['Savings', 'Current'])
    
    accIntrLable = Label(root, text = "Account Intrest", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accIntrText = Entry(root,textvariable= accIntrTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black") 
    
    # Customer Details
    
    custNameLable = Label(root, text = "Customer Name", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    custNameText = Entry(root,textvariable= custNameTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    
    custAddresLable = Label(root, text = "Customer Address", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    custAddresText = Entry(root,textvariable= custAddTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    
    custPhLable = Label(root, text = "Customer Phone Number", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    custPhText = Entry(root,textvariable= custPhTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    

    submitBtn = Button(root, text = "Create Account", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=2, width= 20)
    submitBtn.configure(command = lambda: submitData(root,accNoTextVar.get(), accTypeTextVar.get(), accIntrTextVar.get(), custNameTextVar.get(), custAddTextVar.get(), custPhTextVar.get()))
    
    title.place(x = 280, y = 66)
    home.place(x = 10, y = 10)
    accNoLable.place(x = 133, y = 130)
    accNoText.place(x = 133, y = 160)
    accTypeLable.place(x = 133, y = 210)
    accTypeText.place(x = 133, y = 240)
    accIntrLable.place(x = 133, y = 290)
    accIntrText.place(x = 133, y = 320)
    
    custNameLable.place(x = 443, y = 130)
    custNameText.place(x = 443, y = 160)
    custAddresLable.place(x = 443, y = 210)
    custAddresText.place(x = 443, y = 240)
    custPhLable.place(x = 443, y = 290)
    custPhText.place(x = 443, y = 320)

    
    submitBtn.place(x = 280, y = 400)
    
    root.mainloop()



if __name__ == '__main__':
    newAccount(None)