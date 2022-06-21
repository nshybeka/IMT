from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"


def count_bmi():

    try:
        your_height = float(input_height.get())
        your_mass = float(input_mass.get())
        if your_height > 3 or your_mass > 300:
            messagebox.showinfo(title="Oops", message="Please enter correct value.")
        else:
            bmi = round(your_mass / (your_height*your_height))
    except ValueError:
        messagebox.showinfo(title="Oops", message="Please enter you correct value.")
        print("Enter correct value")
    else:
        yor_bmi_answer.config(text=bmi)
        print(bmi)


window = Tk()
window.title("Body mass index (BMI) ")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=750, height=530)
phone_img = PhotoImage(file="picture.png")
canvas.create_image(375, 265, image=phone_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 19, "bold"))
canvas.grid(row=0, column=1, columnspan=2)


# label
height_label = Label(width=15, text="Your height (m): ")
height_label.grid(row=1, column=1)

mass_label = Label(width=15, text="Your mass (kg): ")
mass_label.grid(row=2, column=1)

your_bmi = Label(width=15, text="Your BMI: ")
your_bmi.grid(row=4, column=1)

yor_bmi_answer = Label(width=15, text="")
yor_bmi_answer.grid(row=4, column=2)

# enter
input_height = Entry(width=15)
height = input_height.get()
input_height.grid(row=1, column=2)

input_mass = Entry(width=15)
mass = input_mass.get()
input_mass.grid(row=2, column=2)

# button
count_button = Button(text="Count", command=count_bmi)
count_button.grid(row=3, column=1, columnspan=2)

window.mainloop()
