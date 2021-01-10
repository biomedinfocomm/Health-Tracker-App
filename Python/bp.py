from tkinter import *

class main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mean Arterial Blood Pressure")
        self.window.geometry("400x400")
        self.window.eval(f'tk::PlaceWindow {self.window.winfo_pathname(self.window.winfo_id())} center')

        self.label1 = Label(self.window, text="Blood Pressure", font=("Arial", 19))
        self.label1.place(x=120, y=12)

        self.label2 = Label(self.window, text="Enter systolic:", font=("Arial", 11))
        self.label2.place(x=52, y=85)
        self.entry1 = Entry(self.window, width=21)
        self.entry1.place(x=140, y=85)

        self.label3 = Label(self.window, text="Enter diastolic:", font=("Arial", 11))
        self.label3.place(x=52, y=115)
        self.entry2 = Entry(self.window, width=21)
        self.entry2.place(x=140, y=115)

        self.label4 = Label(self.window, text="BP", font=("Arial", 11))
        self.label4.place(x=140, y=150)
    
        self.label4 = Label(self.window, text="0", font=("Arial", 11))
        self.label4.place(x=170, y=150)

        self.calculate_button = Button(self.window, text="Calculate BP", font=("Arial", 11), command=self.calculate)
        self.calculate_button.place(x=150, y=190)

        self.quit_button = Button(self.window, text="Quit", font=("Arial", 11), command=self.window.quit)
        self.quit_button.place(x=270, y=190)

        self.window.mainloop()

    def calculate(self):
        try:
            s = getdouble(self.entry1.get())
            d = getdouble(self.entry2.get())
            map = 1/3 * s + 2/3 * d
            self.label4.configure(text=str(map))
        except ValueError as err:
            self.label4.configure(text="Invalid Input")
            print(err)
        except ZeroDivisionError as err:
            self.label4.configure(text="Zero Division Error")
            print(err)

if __name__ == '__main__':
    main()

 
