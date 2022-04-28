from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from util import *
import pymysql
import pandas as pd

# Database Functions
def getCursor():
    db = pymysql.connect(host="localhost", user="sakec",
                         passwd="sakec123", db="dbmslab")
    cursor = db.cursor()
    return db, cursor


def getAccData():
    db, cursor = getCursor()
    cursor.execute("SELECT * FROM loan")
    data = cursor.fetchall()
    db.commit()
    return data

def goBack(root, stat):
    if root == None:
        root.destroy()
    if stat == "emp":
        callEmployee(root)
    elif stat == "man":
        callManager(root)

def showLoans(root, stat):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("800x700+700+250")
    root.title("Banking System | All Loans")
    root.config(bg = "pink")
    
    frame_Table = Frame(root)
    frame_Table.place(x = 20, y = 150, width = 760, height = 530)
    frame_Table.configure(relief='groove')
    frame_Table.configure(borderwidth="2")
    frame_Table.configure(relief="groove")
    
    scroll_x = Scrollbar(frame_Table, orient=HORIZONTAL)
    scroll_y = Scrollbar(frame_Table, orient=VERTICAL)
    
    accTable = ttk.Treeview(frame_Table, columns=("loan_id", "loan_type", "amount","intrest", "start_date", "amount_paid", "acc_no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_x.configure(command=accTable.xview)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.configure(command=accTable.yview)
    accTable.heading("loan_id", text="Loan Id")
    accTable.heading("loan_type", text="Loan Type")
    accTable.heading("intrest", text="Loan Intrest")
    accTable.heading("amount", text="Loan Amount")
    accTable.heading("start_date", text="Start Date")
    accTable.heading("amount_paid", text="Amount Paid")
    accTable.heading("acc_no", text="Account Number")
    accTable['show'] = 'headings'
    accTable.column("loan_id", width=100)
    accTable.column("loan_type", width=100)
    accTable.column("intrest", width=100)
    accTable.column("amount", width=100)
    accTable.column("start_date", width=100)
    accTable.column("amount_paid", width=100)
    accTable.column("acc_no", width=100)
    
    
    
    title = Label(root, text = "Banking System", font = ("Arial", 25, "bold"), bg = "pink", fg = "#3675d9")
    home = Button(root, text = "Home", font = ("Arial", 13), bg = "lightblue",height=2, width= 10, command= lambda: goBack(root, stat))
    title.place(x = 170, y = 66)
    home.place(x = 10, y = 10)
    accTable.pack(fill=BOTH, expand=1)
    data = getAccData()
    if len(data) > 0:
        accTable.delete(*accTable.get_children())
        for row in data:
            accTable.insert('', END, values=row)

    root.mainloop()



if __name__ == '__main__':
    showLoans(None, None)