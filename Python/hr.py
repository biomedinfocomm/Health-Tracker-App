from tkinter import *

class main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Heart Rate")
        self.window.geometry("400x400")
        self.window.eval(f'tk::PlaceWindow {self.window.winfo_pathname(self.window.winfo_id())} center')

        self.label1 = Label(self.window, text="Heart Rate", font=("Arial", 19))
        self.label1.place(x=140, y=12)

        self.label2 = Label(self.window, text="Enter age:", font=("Arial", 11))
        self.label2.place(x=52, y=85)
        self.entry1 = Entry(self.window, width=21)
        self.entry1.place(x=120, y=85)

        self.label4 = Label(self.window, text="HRmax", font=("Arial", 11))
        self.label4.place(x=125, y=150)
    
        self.label4 = Label(self.window, text="0", font=("Arial", 11))
        self.label4.place(x=170, y=150)

        self.calculate_button = Button(self.window, text="Calculate HRmax", font=("Arial", 11), command=self.calculate)
        self.calculate_button.place(x=150, y=190)

        self.quit_button = Button(self.window, text="Quit", font=("Arial", 11), command=self.window.quit)
        self.quit_button.place(x=270, y=190)

        self.window.mainloop()

    def calculate(self):
        try:
            age = getdouble(self.entry1.get())
           
            HRmax = 220 - 0.7 * age 
            self.label4.configure(text=str(HRmax))
        except ValueError as err:
            self.label4.configure(text="Invalid Input")
            print(err)
        except ZeroDivisionError as err:
            self.label4.configure(text="Zero Division Error")
            print(err)

if __name__ == '__main__':
    main()
