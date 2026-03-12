import tkinter as calcu

window = calcu.Tk()
window.title("Simple Calculator")
window.geometry("300x300")

window.resizable( True,True) 

window.configure(bg="#A24857",cursor="arrow")

frame = calcu.Frame(window, bg="white")
frame.grid(row=0, column=0, columnspan=3)

frame1 = calcu.Label(window, text="Hi, Welcome!", bg="white", font=("Arial", 16, "bold"))
frame1.grid(row=0,column=0,columnspan=4)

number_label = calcu.Label(window, text="Enter 1st number", font=("Arial", 12))
number_label.grid(row=4,column=0,pady=10)

number1_entry= calcu.Entry(window,bg="white")
number1_entry.grid(row=4,column=1,pady=5)
value = number1_entry.get()


number_label2 = calcu.Label(window,text="Enter 2nd number", font=("Arial", 12))
number_label2.grid(row=6,column=0,pady=5)

number2_entry= calcu.Entry(window,bg="white")
number2_entry.grid(row=6,column=1,pady=5,padx=2)
value = number2_entry.get()


def add():
    firstnum = int(number1_entry.get())
    secondnum = int(number2_entry.get())
    result = firstnum + secondnum
    frame1['text'] = f"The sum of {firstnum} + {secondnum} is {result}"

button=calcu.Button(window,text="Add",font=12,command=add)
button.grid(row=8,column=0,pady=5)


def mul():
    firstnum = int(number1_entry.get())
    secondnum = int(number2_entry.get())
    result = firstnum * secondnum
    frame1['text'] = f"The product of {firstnum} x {secondnum} is {result}"


button2=calcu.Button(window,text="Multiply",font=12,command=mul)
button2.grid(row=10,column=0)


def sub():
    firstnum = int(number1_entry.get())
    secondnum = int(number2_entry.get())
    result = firstnum - secondnum
    frame1['text'] = f"The difference of {firstnum} - {secondnum} is {result}"

button3=calcu.Button(window,text="Subtract",font=12,command=sub)
button3.grid(row=8,column=1,pady=5)


def div():
    firstnum = int(number1_entry.get())
    secondnum = int(number2_entry.get())
    if secondnum != 0:
        result = firstnum / secondnum
        frame1['text'] = f"The quotient of {firstnum} / {secondnum} is {result}"
    else:
        frame1['text'] = "Error"

button4=calcu.Button(window,text="Division",font=12,command=div)
button4.grid(row=10,column=1)



window.mainloop()