import tkinter as tk 

from tkinter import messagebox

class BudgetApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("World's Best Budgeting App")

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)
       
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Welcome to the World's Best Budgeting App!", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.label2 = tk.Label(self.root, text="Please enter your name Below!")
        self.label2.pack(padx=10, pady=10)

        self.name_entry = tk.Entry()
        self.name_entry.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Ready to Budget? Click Me!!!", font=('Arial', 18), command=self.enterforum)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def enterforum(self):
        if self.name_entry.get() == "":
            self.show_message()
        else:
            self.root2 = tk.Tk()

            self.root2.title(f"{self.name_entry.get()}'s Budget!")

            self.budgetlabel = tk.Label(self.root2, text=f"{self.name_entry.get()}", font=('Arial', 18))
            self.budgetlabel.pack(padx=10, pady=10)

            self.root2.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def show_message(self): 
        messagebox.showinfo(title="Message", message="Please enter your name first!")
        
 
BudgetApp()