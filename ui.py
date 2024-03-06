import tkinter as tk 
from tkinter import ttk, messagebox
from database import MouseDatabase

class MouseApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mouse Database')
        self.database = MouseDatabase()

        # Create GUI elements  
        self.cage_label = ttk.Label(self, text="Cage Number:")
        self.cage_input = ttk.Entry(self)

        self.mouse_label = ttk.Label(self, text="Mouse Number:")        
        self.mouse_input = ttk.Entry(self)  

        self.dob_label = ttk.Label(self, text="Date of Birth:")  
        self.dob_input = ttk.Entry(self)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)        
        self.import_button = ttk.Button(self, text="Export", command=self.export_pandas)
        self.delete_button = ttk.Button(self, text="Delete Data", command=self.delete_data)


        # Layout
        self.cage_label.grid(row=0, column=0)
        self.cage_input.grid(row=0, column=1)
        
        self.mouse_label.grid(row=1, column=0)
        self.mouse_input.grid(row=1, column=1)
        
        self.dob_label.grid(row=2, column=0)
        self.dob_input.grid(row=2, column=1) 
        
        self.submit_button.grid(row=3, column=0, columnspan=2) 
        self.import_button.grid(row=4, column=0, columnspan=2)
        self.delete_button.grid(row=5, column=0, columnspan=2)

    def submit(self):
        cage_number = self.cage_input.get()
        mouse_number = self.mouse_input.get() 
        dob = self.dob_input.get()
        if cage_number and mouse_number and dob:  
            self.database.add_mouse(cage_number, mouse_number, dob) 
            self.clear_inputs()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def export_pandas(self):
        self.database.import_pandas()

    def delete_data(self):
        cage_number = self.cage_input.get()
        mouse_number = self.mouse_input.get()

        if cage_number:
            self.database.delete_data(cage_number=cage_number)
            messagebox.showinfo("Success", f"Data with cage number {cage_number} has been deleted.")
        elif mouse_number:
            self.database.delete_data(mouse_number=mouse_number)
            messagebox.showinfo("Success", f"Data with mouse number {mouse_number} has been deleted.")
        else:
            confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all data from the database?")
            if confirmation:
                self.database.delete_data()
                messagebox.showinfo("Success", "All data has been deleted from the database.")
        
        self.clear_inputs()

    def clear_inputs(self):
        self.cage_input.delete(0, tk.END)
        self.mouse_input.delete(0, tk.END) 
        self.dob_input.delete(0, tk.END) 