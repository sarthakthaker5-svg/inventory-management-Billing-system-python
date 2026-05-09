from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x800+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #title
        lbl_title=Label(self.root,text="Inventory Management System",font=("algerian",35,"bold"),bg="green",fg="white",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1360,height=60)

        img=Image.open("Image/Logo.png")
        img=img.resize((100,60),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg,bg="green")
        lbl_img.place(x=0,y=0,width=100,height=60)

        #button
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("arial",15,"bold"),bg="red",cursor="hand2").place(x=1200,y=10,height=30,width=150)

        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Inevntory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("arial",15),bg="blue",fg="white")
        self.lbl_clock.place(x=0,y=60,relwidth=1,height=25)

        #left menu
        img_1=Image.open("Image/Menu.png")
        img_1=img_1.resize((197,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_1)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=90,width=200,height=575)

        lbl_img_1=Label(self.root,image=self.photoimg,bg="white")
        lbl_img_1.place(x=2,y=91,width=197,height=200)

        lbl_menu=Label(LeftMenu,font=('arialblack',20,'bold'),bg="red",fg="black",text="Menu",bd=4)
        lbl_menu.place(x=1,y=200,width=200,height=52.6)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=253.5,width=198,height=52.6)
        btn_supplier=Button(LeftMenu,text="Suppliers",command=self.supplier,font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=307,width=198,height=52)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=360.5,width=198,height=52)
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=414,width=198,height=52)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=467.5,width=198,height=52)
        btn_exit=Button(LeftMenu,text="Exit",font=("arial",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=1,y=521,width=198,height=52)
        
        #Content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="brown",fg="white",font=("Bahnschrift Semi Bold",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_Supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="gray",fg="white",font=("Bahnschrift Semi Bold",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_Category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="pink",fg="white",font=("Bahnschrift Semi Bold",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_Sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="green",fg="white",font=("Bahnschrift Semi Bold",20,"bold"))
        self.lbl_Sales.place(x=300,y=300,height=150,width=300)
        
        self.lbl_Product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("Bahnschrift Semi Bold",20,"bold"))
        self.lbl_Product.place(x=650,y=300,height=150,width=300)
        
        #last varu box
        lbl_footer=Label(self.root,text="IMS -Inventory Management System\n 22bsit148, 21bsit085, 22bsit115",font=("arial",15),bg="blue",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f'Total Product\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_Supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_Category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')

            self.lbl_Sales.config(text=f'Total Sales\n[{str(len(os.listdir('bill')))}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d:%m:%Y")
            self.lbl_clock.config(text=f"Welcome to Inevntory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
