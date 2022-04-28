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

def submitData(root, accno, loanType, loanAmt, loanIntr, loanPaid=0):
    from datetime import date
    loanStart = date.today().strftime("%d-%m-%Y")
    print(accno, loanType, loanAmt,loanStart, loanIntr, loanPaid)
    if(not accExists(accno)):
        messagebox.showinfo("Error", "Account Number does not exist")
        return
    db, cursor = getCursor()
    try:
        cursor.execute(f"""INSERT INTO loan (`loan_type`, `amount`, `intrest`, `start_date`, `amount_paid`, `acc_no`) VALUES("{loanType}", "{loanAmt}", "{loanIntr}", "{loanStart}", "{loanPaid}", "{accno}");""")
    except():
        messagebox.showerror("Error", "Database Error")
        return
    finally:
        db.commit()
        messagebox.showinfo("Success", "Loan Added Successfully")
        callManager(root)
        
    

def getAccNo():
    db, cursor = getCursor()
    cursor.execute(f"""SELECT acc_no FROM account; """)
    data = cursor.fetchall()
    db.commit()
    out = []
    for i in range(len(data)):
        out.append(data[i][0])
    return out

def newLoan(root):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("800x400+500+250")
    root.title("Banking System | Add New Loan")
    root.config(bg = "pink")
    
    accNoTextVar = IntVar()
    accNoTextVar.set(0)
    
    accTypeTextVar = StringVar()
    accIntrTextVar = IntVar()
    accIntrTextVar.set(7)
    custNameTextVar = IntVar()

    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: callManager(root))
    
    # Account Details
    
    accNoLable = Label(root, text = "Account Number", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accNoText = Combobox(root,textvariable= accNoTextVar,  font = ("Dosis", 15),  values= getAccNo())
    
    accTypeLable = Label(root, text = "Loan Type", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accTypeText = Combobox(root,textvariable= accTypeTextVar,  font = ("Dosis", 15), state='readonly', values= ["Home Loan", "Car Loan", "Education Loan", "Personal Loan"])
    
    accIntrLable = Label(root, text = "Loan Intrest", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    accIntrText = Entry(root,textvariable= accIntrTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black") 
    
    # Customer Details
    
    custNameLable = Label(root, text = "Loan Amount", font = ("Arial", 15), bg = "pink", fg = "#3675d9")
    custNameText = Entry(root,textvariable= custNameTextVar,  font = ("Dosis", 15), bg = "lightblue", fg = "black")
    
    

    submitBtn = Button(root, text = "Add Loan", relief=RIDGE, font = ("Arial", 15), bg = "lightblue",height=2, width= 20)
    submitBtn.configure(command = lambda: submitData(root, accNoTextVar.get(), accTypeTextVar.get(), custNameTextVar.get(), accIntrTextVar.get(),))
    
    title.place(x = 280, y = 66)
    home.place(x = 10, y = 10)
    accNoLable.place(x = 133, y = 130)
    accNoText.place(x = 133, y = 160)
    accTypeLable.place(x = 133, y = 210)
    accTypeText.place(x = 133, y = 240)
    accIntrLable.place(x = 443, y = 210)
    accIntrText.place(x = 443, y = 240)
    
    custNameLable.place(x = 443, y = 130)
    custNameText.place(x = 443, y = 160)

    
    submitBtn.place(x = 280, y = 310)
    
    root.mainloop()



if __name__ == '__main__':
    newLoan(None)