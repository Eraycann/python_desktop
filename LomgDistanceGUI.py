import tkinter
import tkinter.messagebox

class LongDistanceGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long Distance Call Calculator")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.rb_var = tkinter.IntVar()
        self.rb_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Daytime (06:00-17:59)',
                                       variable=self.rb_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Evening (18:00-23:59)',
                                       variable=self.rb_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Night (00:00-05:59)',
                                       variable=self.rb_var, value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.minutes_label = tkinter.Label(self.mid_frame,
                                           text='How many minutes did you talk?')
        self.minutes_entry = tkinter.Entry(self.mid_frame,width=10)

        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        self.display_button = tkinter.Button(self.bottom_frame,
                                             text='Show Charges',
                                             command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        self.minutes = float(self.minutes_entry.get())

        if self.rb_var.get() == 1:
            self.rate = 0.07
        if self.rb_var.get() == 2:
            self.rate = 0.12
        if self.rb_var.get() == 3:
            self.rate = 0.05

        self.charges = self.minutes * self.rate
        tkinter.messagebox.showinfo('Total Charges',
                                    'Total charges = $' +
                                    format(self.charges,',.2f'))

# Run the GUI
LongDistanceGUI()
