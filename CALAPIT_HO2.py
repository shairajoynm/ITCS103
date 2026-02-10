import tkinter as profile

window = profile.Tk()

#palit title ng app - str
window.title("About Me")

#size and pixels
window.geometry("600x600")

#resizable height
window.resizable(False,True) 

#cursor
window.configure(bg="#A24857",cursor="hand2")

#text sa loob
#first
label = profile.Label(window,text="Student Profile",
    font = ("Fixedsys","30","bold"),
    fg = "black", 
    bg = "pink", 
    anchor = "center") 

label.pack(pady=40)
    
#name
label = profile.Label(window,text="Name:  Shaira Joy A. Calapit",
    font = ("Fixedsys","19"),
    fg = "black", 
    bg = "#A24857", 
) 

label.pack(padx=10,anchor = "w")


#age
label = profile.Label(window,text="Age: 19",
    font = ("Fixedsys","19"),
    fg = "black", 
    bg = "#A24857", 
) 

label.pack(padx=10,anchor = "w")


#course and section
label = profile.Label(window,text="Course and Section:  BSIT - 1A",
    font = ("Fixedsys","19"),
    fg = "black", 
    bg = "#A24857", 
) 

label.pack(padx=10,anchor = "w")

#birthday
label = profile.Label(window,text="Birthday:  January 09, 2007",
    font = ("Fixedsys","19"),
    fg = "black", 
    bg = "#A24857", 
) 

label.pack(padx=10,anchor = "w")

#personal motto
label = profile.Label(window,text="Motto:  Let go and Let God",
    font = ("Fixedsys","19"),
    fg = "black", 
    bg = "#A24857", 
) 

label.pack(padx=10,anchor = "w")

#tawag
window.mainloop()



