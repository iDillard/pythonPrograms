#
# Isaiah Dillard
# This program was built to show GUI use
# This is a simple program that calculates tax

import tkinter as tk

# create the object for the GUI
class TaxGUI:

    def __init__(self):
        # Create the main window for GUI
        self.main_window = tk.Tk()
        # Create the label for title label for the GUI
        self.main_window.title('Tax Calculator')
        # set the size of the window
        self.main_window.geometry('250x125')

        # Create the first line of the GUI
        self.line1_frame = tk.Frame(self.main_window)
        self.input_label1 = tk.Label(self.line1_frame,
                                    text='Total Purchase: ')
        self.input_box1 = tk.Entry(self.line1_frame,
                                   width=10)

        # pack Line 1 and the items within it
        self.input_label1.pack(side='left')
        self.input_box1.pack(side='left')
        self.line1_frame.pack()

        # Create the second line of the GUI
        self.line2_frame = tk.Frame(self.main_window)
        self.input_label2 = tk.Label(self.line2_frame,
                                     text='Tax Rate: ')
        self.input_box2 = tk.Entry(self.line2_frame,
                                   width=10)
        self.input_label2.pack(side='left')
        self.input_box2.pack(side='left')
        self.line2_frame.pack()

        # Create the third line of GUI
        self.line3_frame = tk.Frame(self.main_window)
        self.sales_tax = tk.StringVar()
        self.sales_tax.set('$ 0.00')
        self.sales_tax_label = tk.Label(self.line3_frame,
                                        text='Sales Tax: ')
        self.tax_result_label = tk.Label(self.line3_frame,
                                         textvariable=self.sales_tax)
        self.sales_tax_label.pack(side='left')
        self.tax_result_label.pack(side='left')
        self.line3_frame.pack()

        # Line four
        self.line4_frame = tk.Frame(self.main_window)
        self.amount_due = tk.StringVar()
        self.amount_due.set('$ 0.00')
        self.amount_due_label = tk.Label(self.line4_frame,
                                         text='Amount Due: ')
        self.amount_result = tk.Label(self.line4_frame,
                                      textvariable=self.amount_due)
        self.amount_due_label.pack(side='left')
        self.amount_result.pack(side='left')
        self.line4_frame.pack()

        # button creation
        self.button_line = tk.Frame(self.main_window)
        self.calc_btn = tk.Button(self.button_line,
                                  text='Calculate',
                                  command=self.calc_tax)
        self.quit_btn = tk.Button(self.button_line,
                                  text='Quit',
                                  command=self.main_window.destroy)
        self.calc_btn.pack(side='left')
        self.quit_btn.pack(side='left')
        self.button_line.pack()

        tk.mainloop()

    def calc_tax(self):
        # function for doing the math on the calculator

        try:
            purchase_amount = float(self.input_box1.get())
            tax_rate = int(self.input_box2.get())

            sales_tax = (tax_rate * 0.01) * purchase_amount

            total_due = sales_tax + purchase_amount

            self.amount_due.set(f'$ {total_due:.2f}')
            self.sales_tax.set(f'$ {sales_tax:.2f}')
        except ValueError:
            self.amount_due.set('Error')
            self.sales_tax.set('Error')
        pass


run_gui = TaxGUI()
