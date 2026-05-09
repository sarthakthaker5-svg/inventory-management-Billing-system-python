from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Billing and Stock Management System")
        self.root.config(bg="white")    
        self.root.focus_force()

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Bahnschrift Semi Bold", 12, "bold"),bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER,font=("times new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("Bahnschrift Semi Bold", 15), bg="green", fg="white",cursor="hand2").place(x=440, y=8, width=130, height=30)

        # Title
        title = Label(self.root, text="Employee Details", font=("Bahnschrift Semi Bold", 15), bg="orange", fg="white",
                      cursor="hand2",relief=RIDGE).place(x=50, y=100, width=1000)

        # Content
        lbl_empid = Label(self.root, text="Emp ID", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=350, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=850, y=150, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Name", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=350, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Bahnschrift Semi Bold", 15),bg="lightyellow").place(x=850, y=190, width=180)

        #Row3
        lbl_email=Label(self.root,text="Email",font=("Bahnschrift Semi Bold",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Pass",font=("Bahnschrift Semi Bold",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("Bahnschrift Semi Bold",15),bg="white").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("Bahnschrift Semi Bold",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("Bahnschrift Semi Bold",15),bg="lightyellow").place(x=500,y=230,width=180)
        self.cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin", "Employee"),state='readonly',justify=CENTER,font=("times new roman", 15))
        self.cmb_utype.place(x=850, y=230, width=180)
        self.cmb_utype.current(1)  # Default = Employee
        
        # Address and Salary
        lbl_address = Label(self.root, text="Address", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("Bahnschrift Semi Bold", 15), bg="white").place(x=500, y=270)
        self.txt_address = Text(self.root, font=("Bahnschrift Semi Bold", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        self.txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Bahnschrift Semi Bold", 15), bg="lightyellow")
        self.txt_salary.place(x=600, y=270, width=180)
        self.toggle_salary()
        self.cmb_utype.bind("<<ComboboxSelected>>", self.toggle_salary)
        # Buttons
        btn_add = Button(self.root, text="Save", command=self.add, font=("Bahnschrift Semi Bold", 15), bg="blue",fg="white", cursor="hand2").place(x=500, y=305, width=100, height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Bahnschrift Semi Bold",15),bg="red",fg="white",cursor="hand2").place(x=620,y=305,width=100,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Bahnschrift Semi Bold",15),bg="orange",fg="white",cursor="hand2").place(x=740,y=305,width=100,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Bahnschrift Semi Bold",15),bg="indigo",fg="white",cursor="hand2").place(x=860,y=305,width=100,height=28)

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="NAME")
        self.EmployeeTable.heading("email",text="EMAIL")
        self.EmployeeTable.heading("gender",text="GENDER")
        self.EmployeeTable.heading("contact",text="CONTACT")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="PASS")
        self.EmployeeTable.heading("utype",text="UTYPE")
        self.EmployeeTable.heading("address",text="ADDRESS")
        self.EmployeeTable.heading("salary",text="SALARY")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=200)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        if self.check_admin_exists():
            self.cmb_utype['values'] = ("Employee",)
            self.var_utype.set("Employee")

        self.show()
        
    def check_admin_exists(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM employee WHERE utype='Admin'")
            count = cur.fetchone()[0]
            return count > 0
        except:
            return False
        finally:
            con.close()
    def toggle_salary(self, event=None):
        if self.var_utype.get() == "Admin":
            self.txt_salary.config(state='disabled')
            self.var_salary.set("")  # clear salary
        else:
            self.txt_salary.config(state='normal')
        
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            if self.var_utype.get() == "Employee" and self.var_salary.get() == "":
                messagebox.showerror("Error", "Salary is required for Employee", parent=self.root)
                return
            if not self.var_emp_id.get().isdigit():
                messagebox.showerror("Error", "Employee ID must be numeric", parent=self.root)
                return
            if not self.var_name.get().replace(" ", "").isalpha():
                messagebox.showerror("Error", "Name must contain only alphabetic characters", parent=self.root)
                return
            if self.var_utype.get() == "Admin":
                salary = 0
            else:
                try:
                    salary = float(self.var_salary.get())
                except ValueError:
                    messagebox.showerror("Error", "Salary must be a numeric value", parent=self.root)
                    return
            dob_str = self.var_dob.get()
            try:
                dob = datetime.strptime(dob_str, "%d-%m-%Y")  
                today = datetime.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 18:
                    messagebox.showerror("Error", "Employee must be at least 18 years old", parent=self.root)
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid D.O.B format. Use DD-MM-YYYY", parent=self.root)
                return
            cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Employee ID already exists", parent=self.root)
                return
            if not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", "Contact number must be exactly 10 digits", parent=self.root)
                return
            doj_str = self.var_doj.get()
            try:
                doj = datetime.strptime(doj_str, "%d-%m-%Y")
                today = datetime.today()
                if doj > today:
                    messagebox.showerror("Error", "Date of Joining is Invalid", parent=self.root)
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid D.O.J format. Use DD-MM-YYYY", parent=self.root)
                return
            if self.var_gender.get() == "Select":
                messagebox.showerror("Error", "Gender selection is required", parent=self.root)
                return
            if self.var_utype.get() == "Admin" and self.check_admin_exists():
                messagebox.showerror("Error", "Admin already exists! Only one Admin allowed.", parent=self.root)
                return
            cur.execute("INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                int(self.var_emp_id.get()),
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_contact.get(),
                dob.strftime("%d-%m-%Y"),  # Store DOB in a consistent format
                self.var_doj.get(),
                self.var_pass.get(),
                self.var_utype.get(),
                self.txt_address.get('1.0', END).strip(),
                salary
                ))
            con.commit()
            messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
            self.show()
            if self.check_admin_exists():
                self.cmb_utype['values'] = ("Employee",)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']
        if not row:
            return
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])
        self.toggle_salary()
    
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "" or self.var_name.get() == "" or self.var_salary.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            if not self.var_emp_id.get().isdigit():
                messagebox.showerror("Error", "Employee ID must be numeric", parent=self.root)
                return
            try:
                salary = float(self.var_salary.get())
            except ValueError:
                messagebox.showerror("Error", "Salary must be a numeric value", parent=self.root)
                return
            dob_str = self.var_dob.get()
            try:
                dob = datetime.strptime(dob_str, "%d-%m-%Y")  
                today = datetime.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 18:
                    messagebox.showerror("Error", "Employee must be at least 18 years old", parent=self.root)
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid D.O.B format. Use DD-MM-YYYY", parent=self.root)
                return
            cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                return
            if not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", "Contact number must be exactly 10 digits", parent=self.root)
                return
            doj_str = self.var_doj.get()
            try:
                doj = datetime.strptime(doj_str, "%d-%m-%Y")
                today = datetime.today()
                if doj > today:
                    messagebox.showerror("Error", "Date of Joining is Invalid", parent=self.root)
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid D.O.J format. Use DD-MM-YYYY", parent=self.root)
                return
            if self.var_gender.get() == "Select":
                messagebox.showerror("Error", "Gender selection is required", parent=self.root)
                return

            cur.execute("UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE eid=?", (
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_contact.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_pass.get(),
                self.var_utype.get(),
                self.txt_address.get('1.0', END).strip(),
                salary,
                int(self.var_emp_id.get()),
                ))
            con.commit()
            messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
                return
            if not self.var_emp_id.get().isdigit():
                messagebox.showerror("Error", "Employee ID must be numeric", parent=self.root)
                return
            cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                return
            op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
            if op:
                cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                con.commit()
                messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Employee")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                query = f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))                
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()

