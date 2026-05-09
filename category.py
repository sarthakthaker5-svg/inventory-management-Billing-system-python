from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Billing and Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #title
        lbl_title=Label(self.root,text="Manage Product Category",font=("Bahnschrift Semi Bold",30,'bold'),bg="brown",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("Bahnschrift Semi Bold",30,'bold'),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Bahnschrift Semi Bold",18),bg="lightyellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="Add",command=self.add,font=("Bahnschrift Semi Bold",18),bg="blue",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete_category,font=("Bahnschrift Semi Bold",18),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)

        #Category Detail
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=400,height=370)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid",text="C ID")
        self.category_table.heading("name",text="NAME")
        
        self.category_table["show"]="headings"

        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)

        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        
        #image
        self.im1=Image.open("Image/cat.jpg")
        self.im1 = self.im1.resize((610, 250), Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RIDGE)
        self.lbl_im1.place(x=50,y=220)

        self.show()
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            if not self.var_name.get() or not self.var_name.get():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Category already exists", parent=self.root)
                return

            cur.execute("INSERT INTO category ( name) ""VALUES (?)",(
                    self.var_name.get(),
                )
            )
            con.commit()
            messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        try:
            f = self.category_table.focus()
            content = self.category_table.item(f)
            row = content['values']
            if row:
                print("Retrieved Row:", row)  # Debugging line
                self.var_cat_id.set(row[0])
                self.var_name.set(row[1])
            else:
                messagebox.showerror("Error", "No data selected", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving data: {str(e)}", parent=self.root)

    def delete_category(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select a category to delete", parent=self.root)
                return
            cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Category", parent=self.root)
                return
            op = messagebox.askyesno("Confirm", "Deleting this category will also delete its products. Continue?", parent=self.root)
            if op:
                cur.execute("DELETE FROM product WHERE Category=(SELECT name FROM category WHERE cid=?)", (self.var_cat_id.get(),))
                cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                con.commit()
                messagebox.showinfo("Delete", "Category and its products deleted successfully", parent=self.root)
                self.show()
        except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


            

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()

