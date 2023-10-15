import tkinter as tk
from tkinter import messagebox, PhotoImage

# PizzaMate class is the main application class
class PizzaMate:
    def __init__(self, root):
        """
        Initialize the PizzaMate application.

        Args:
            root (tk.Tk): The main application window.
        """
        self.root = root
        self.root.title('PizzaMate')

        # Load images for the welcome and pizza selection screens
        self.image1 = PhotoImage(file='C:\\Users\\tacoc\\Downloads\\FinalGUIProject\\image01.png') # Welcome screen image
        self.image2 = PhotoImage(file='C:\\Users\\tacoc\\Downloads\\FinalGUIProject\\image02.png') # Pizza selection screen image

        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root)  # Frame for the welcome screen
        self.welcome_frame.pack()
        tk.Label(self.welcome_frame, text='Welcome to PizzaMate!', image=self.image1, compound='left').pack()
        tk.Button(self.welcome_frame, text='Start Order', command=self.start_order).pack()

    def start_order(self):
        """
        Display the pizza selection screen when the user clicks 'Start Order'.
        """
        if not self.validate_input():
            return
        self.welcome_frame.pack_forget()

        # Pizza Selection Screen
        self.selection_frame = tk.Frame(self.root)  # Frame for the pizza selection screen
        self.selection_frame.pack()
        tk.Label(self.selection_frame, text='Select your pizza', image=self.image2, compound='left').pack()
        self.pizza_var = tk.StringVar()  # Variable to store the selected pizza type
        self.pizza_var.set('Cheese')  # Default pizza selection
        pizza_options = ['Cheese', 'Pepperoni', 'Sausage', 'Hawaiian']
        for option in pizza_options:
            tk.Radiobutton(self.selection_frame, text=option, variable=self.pizza_var, value=option).pack()
        tk.Button(self.selection_frame, text='Next', command=self.select_toppings).pack()

    def select_toppings(self):
        """
        Display the toppings selection screen when the user clicks 'Next' on the pizza selection screen.
        """
        if not self.validate_input():
            return
        self.selection_frame.pack_forget()

        # Toppings Selection Screen
        self.toppings_frame = tk.Frame(self.root)  # Frame for the toppings selection screen
        self.toppings_frame.pack()
        tk.Label(self.toppings_frame, text='Select your toppings').pack()
        toppings_options = ['Mushrooms', 'Peppers', 'Olives', 'Onions']
        self.toppings_vars = []  # List to store BooleanVars for selected toppings
        for option in toppings_options:
            var = tk.BooleanVar()
            tk.Checkbutton(self.toppings_frame, text=option, variable=var).pack()
            self.toppings_vars.append(var)
        tk.Button(self.toppings_frame, text='Next', command=self.select_quantity).pack()

    def select_quantity(self):
        """
        Display the quantity selection screen when the user clicks 'Next' on the toppings selection screen.
        """
        if not self.validate_input():
            return
        self.toppings_frame.pack_forget()

        # Quantity Selection Screen
        self.quantity_frame = tk.Frame(self.root)  # Frame for the quantity selection screen
        self.quantity_frame.pack()
        tk.Label(self.quantity_frame, text='Select quantity').pack()
        self.quantity_var = tk.IntVar(value=1)  # Variable to store the selected quantity (default value is 1)
        tk.Spinbox(self.quantity_frame, from_=1, to=10, textvariable=self.quantity_var).pack()
        tk.Button(self.quantity_frame, text='Next', command=self.order_summary).pack()

    def order_summary(self):
        """
        Display the order summary screen when the user clicks 'Next' on the quantity selection screen.
        """
        if not self.validate_input():
            return
        self.quantity_frame.pack_forget()

        # Order Summary Screen
        self.summary_frame = tk.Frame(self.root)  # Frame for the order summary screen
        self.summary_frame.pack()

        # Delivery Details Entry
        tk.Label(self.summary_frame, text='Enter your delivery details:').pack()
        self.address_entry = tk.Entry(self.summary_frame)  # Entry box for delivery details
        self.address_entry.pack()

        # Payment Method Selection
        tk.Label(self.summary_frame, text='Select payment method:').pack()
        self.payment_var = tk.StringVar(value='Cash')  # Variable to store the selected payment method (default is Cash)
        payment_options = ['Cash', 'Credit Card', 'Debit Card']
        for option in payment_options:
            tk.Radiobutton(self.summary_frame, text=option, variable=self.payment_var, value=option).pack()

        tk.Button(self.summary_frame, text='Place Order', command=self.place_order).pack()

    def place_order(self):
        """
        Placeholder for the logic to place the order.
        """
        if not self.validate_input():
            messagebox.showerror("Error", "Invalid input. Please check your details and try again.")
        # Logic for placing the order

    def validate_input(self):
        """
        Placeholder for input validation logic.
        
        Returns:
            bool: True if input is valid, False otherwise.
        """
        # Placeholder for input validation .l
        #
        return True

root = tk.Tk()  # Main application window
app = PizzaMate(root)  # Create an instance of PizzaMate
root.mainloop()  # Start the application
