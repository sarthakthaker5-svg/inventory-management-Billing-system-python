from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Billing and Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # Search Frame
        lbl_search = Label(self.root, text="Invoice No.",bg="white",font=("times new roman", 15))
        lbl_search.place(x=700, y=80)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=800, y=80,width=150)
        btn_search = Button(self.root, text="Search",command=self.search, font=("Bahnschrift Semi Bold", 15), bg="green", fg="white",cursor="hand2").place(x=960, y=79, width=120, height=30)

        # Title
        title = Label(self.root, text="Supplier Details", font=("Bahnschrift Semi Bold", 20,'bold'), bg="red", fg="white",
                      cursor="hand2",relief=RIDGE).place(x=50, y=10, width=1000,height=40)

        # Row1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("Bahnschrift Semi Bold", 15),
                          bg="lightyellow").place(x=180, y=80, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Name", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=180, y=120, width=180)
        
        # Row3
        lbl_contact=Label(self.root,text="Contact",font=("Bahnschrift Semi Bold",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Bahnschrift Semi Bold",15),bg="lightyellow").place(x=180,y=160,width=180)

        # Description
        lbl_desc = Label(self.root, text="Decription", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=200)
        self.txt_desc = Text(self.root, font=("Bahnschrift Semi Bold", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height=120)

        # Buttons
        btn_add = Button(self.root, text="Save", command=self.add, font=("Bahnschrift Semi Bold", 15), bg="blue",fg="white", cursor="hand2").place(x=180, y=370, width=110, height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Bahnschrift Semi Bold",15),bg="red",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Bahnschrift Semi Bold",15),bg="orange",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Bahnschrift Semi Bold",15),bg="yellow",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=400,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="NAME")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)

        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "" or self.var_name.get() == "" or self.var_contact.get() == "" or self.txt_desc.get('1.0', END).strip() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            if not self.var_sup_invoice.get() or not self.var_name.get() or not self.var_contact.get() or not self.txt_desc.get('1.0', END).strip():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Invoice already exists", parent=self.root)
                return
            if not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", "Contact number must be exactly 10 digits", parent=self.root)
                return
            cur.execute("INSERT INTO supplier (invoice, name, contact, desc) ""VALUES (?, ?, ?, ?)",(
                    int(self.var_sup_invoice.get()),
                    self.var_name.get(),
                    self.var_contact.get(),
                    self.txt_desc.get('1.0', END).strip(),
                )
            )
            con.commit()
            messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
        try:
            f = self.supplierTable.focus()
            content = self.supplierTable.item(f)
            row = content['values']
            if row:
                print("Retrieved Row:", row)  # Debugging line
                self.var_sup_invoice.set(row[0])
                self.var_name.set(row[1])
                self.var_contact.set(row[2])
                self.txt_desc.delete('1.0', END)
                self.txt_desc.insert(END, row[3])
            else:
                messagebox.showerror("Error", "No data selected", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving data: {str(e)}", parent=self.root)
    
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "" or self.var_name.get() == "" or self.var_contact.get() == "" or self.txt_desc.get('1.0', END).strip() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            if not self.var_sup_invoice.get().isdigit():
                messagebox.showerror("Error", "Invoice No. must be numeric", parent=self.root)
                return

            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid invoice", parent=self.root)
                return

            if not self.var_sup_invoice.get().isdigit():
                messagebox.showerror("Error", "Invoice No. must be numeric", parent=self.root)
                return
            try:
                cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?",(
                    self.var_name.get().strip(),
                    self.var_contact.get().strip(),
                    self.txt_desc.get('1.0', END).strip(),
                    self.var_sup_invoice.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                self.show()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"SQL Error: {str(e)}", parent=self.root)
                con.commit()
                messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "" or self.var_name.get() == "" or self.var_contact.get() == "" or self.txt_desc.get('1.0', END).strip() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            
            if not self.var_sup_invoice.get() or not self.var_name.get() or not self.var_contact.get() or not self.txt_desc.get('1.0', END).strip():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Invoice ID", parent=self.root)
                return
            op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
            if op:
                cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                con.commit()
                messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?",(self.var_searchtxt.get(),))               
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()

