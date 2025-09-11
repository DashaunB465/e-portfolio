# import basic gui
import tkinter
import tkinter.messagebox

class TipGUI:
    def __init__(self):
        
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create 5 frames
        self.subtotal_frame = tkinter.Frame(self.main_window)
        self.percent_frame = tkinter.Frame(self.main_window)
        self.tip_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the subtotal frame
        self.subtotal_label = tkinter.Label \
                             (self.subtotal_frame, \
                              text = "Enter the amount of the ticket $10 = 10")
        self.subtotal_entry = tkinter.Entry(self.subtotal_frame, width = 10)

        # Pack the subtotal frame widgets
        self.subtotal_label.pack(side = "left")
        self.subtotal_entry.pack(side = "left")

        # Create the widgets for the percent frame
        self.percent_label = tkinter.Label \
                             (self.percent_frame, \
                              text = "Enter the tip as a percentage 10% = 0.1")
        self.percent_entry = tkinter.Entry(self.percent_frame, width = 10)

        # Pack the percent frame widgets
        self.percent_label.pack(side = "left")
        self.percent_entry.pack(side = "left")

        # Create the widgets for the tip frame
        self.tip_label = tkinter.Label \
                            (self.tip_frame, \
                             text = "Tip Amount: $")
        
        # Create the widgets for the total frame
        self.total_label = tkinter.Label \
                            (self.total_frame, \
                             text = "Total Amount: $")

        # Create a blank label for tip
        self.showtip = tkinter.StringVar()
        self.showtip_label = tkinter.Label(self.tip_frame, \
                                       textvariable= self.showtip)
        # Create a blank label for total
        self.showtotal = tkinter.StringVar()
        self.showtotal_label = tkinter.Label(self.total_frame, \
                                       textvariable= self.showtotal)

        # Pack the tip and total frame widgets
        self.total_label.pack(side = 'left')
        self.tip_label.pack(side = 'left')
        self.showtip_label.pack(side = 'right')
        self.showtotal_label.pack(side = 'right')

        # Create the two buttons in the bottom frame
        self.calculate_button = tkinter.Button \
                          (self.button_frame, \
                           text = 'Calculate', \
                           command = self.calculate_tip)

        self.quit_button = tkinter.Button \
                           (self.button_frame, \
                            text = 'Quit', \
                            command = self.main_window.destroy)

        # Pack the widgets in the button frame
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.subtotal_frame.pack()
        self.percent_frame.pack()
        self.tip_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()
        
# create the calculation method
    def calculate_tip(self):

        # Get the values entered
        self.subtotal = float(self.subtotal_entry.get())
        while self.subtotal < 0:
            tkinter.messagebox.showinfo("Message Box",\
                                        "Enter a positive numbers only in the amount box\nTry Again.")
            self.subtotal_entry.select()
            
        self.percent = float(self.percent_entry.get())
        while self.percent < 0:
            tkinter.messagebox.showinfo("Message Box",\
                                        "Enter positive numbers only in the percent box\nTry Again.")
            self.percent_entry.select()
            
        # Calculate tip
        self.tipper_ticket = float(self.subtotal) * self.percent

        # Calculate total 
        self.totalwith_tip = float(self.subtotal) + self.tipper_ticket

        # Update the tip label
        self.showtip.set(self.tipper_ticket)

        # update total label
        self.showtotal.set(self.totalwith_tip)

# Create an instance of TipGUI
tip = TipGUI()
