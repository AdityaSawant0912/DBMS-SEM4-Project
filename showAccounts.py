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
    cursor.execute("SELECT * FROM account")
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

def showAccounts(root, stat):
    if root != None:
        root.destroy()
    root = Tk()
    root.geometry("600x700+700+250")
    root.title("Banking System | All Accounts")
    root.config(bg = "pink")
    
    frame_Table = Frame(root)
    frame_Table.place(x = 20, y = 150, width = 560, height = 530)
    frame_Table.configure(relief='groove')
    frame_Table.configure(borderwidth="2")
    frame_Table.configure(relief="groove")
    
    scroll_x = Scrollbar(frame_Table, orient=HORIZONTAL)
    scroll_y = Scrollbar(frame_Table, orient=VERTICAL)
    
    accTable = ttk.Treeview(frame_Table, columns=("acc_no", "acc_type", "intrest", "balance", "branch_id"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_x.configure(command=accTable.xview)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.configure(command=accTable.yview)
    accTable.heading("acc_no", text="Account Number")
    accTable.heading("acc_type", text="Account Type")
    accTable.heading("intrest", text="Account Intrest")
    accTable.heading("balance", text="Account Balance")
    accTable.heading("branch_id", text="Branch Id")
    accTable['show'] = 'headings'
    accTable.column("acc_no", width=100)
    accTable.column("acc_type", width=100)
    accTable.column("intrest", width=100)
    accTable.column("balance", width=100)
    accTable.column("branch_id", width=100)
    
    
    
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
    showAccounts(None, None)