from tkinter import *

class main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Body Mass Index")
        self.window.geometry("400x400")
        self.window.eval(f'tk::PlaceWindow {self.window.winfo_pathname(self.window.winfo_id())} center')

        self.label1 = Label(self.window, text="Body Mass Index", font=("Arial", 19))
        self.label1.place(x=120, y=12)

        self.label2 = Label(self.window, text="Enter weight:", font=("Arial", 11))
        self.label2.place(x=52, y=85)
        self.entry1 = Entry(self.window, width=18)
        self.entry1.place(x=140, y=85)

        self.label3 = Label(self.window, text="Enter height:", font=("Arial", 11))
        self.label3.place(x=52, y=115)
        self.entry2 = Entry(self.window, width=18)
        self.entry2.place(x=140, y=115)

        self.label4 = Label(self.window, text="BMI", font=("Arial", 11))
        self.label4.place(x=140, y=150)
   
        self.label4 = Label(self.window, text="0", font=("Arial", 11))
        self.label4.place(x=170, y=150)

        self.calculate_button = Button(self.window, text="Calculate BMI", font=("Arial", 11), command=self.calculate)
        self.calculate_button.place(x=150, y=190)

        self.quit_button = Button(self.window, text="Quit", font=("Arial", 11), command=self.window.quit)
        self.quit_button.place(x=270, y=190)

        self.window.mainloop()

    def calculate(self):
        try:
            w = getdouble(self.entry1.get())
            h = getdouble(self.entry2.get())
            mpg = w / (h**2)
            self.label4.configure(text=str(mpg))
        except ValueError as err:
            self.label4.configure(text="Invalid Input")
            print(err)
        except ZeroDivisionError as err:
            self.label4.configure(text="Zero Division Error")
            print(err)

if __name__ == '__main__':
    main()

 


