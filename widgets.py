#import necessary libraties
from tkinter import*
from datetime import date

#create window
root=Tk()
root.title('Getting started with widgets')
root.geometry('400x300')

#add widgets
#add label
lbl=Label(text="Hey there!",fg="white",bg="#072F5F",height=1,width=300)

#add label for getting name as input
#use entry widget to create a text box for user to enter details
name_lbl=Label(text="Full Name",bg="#3895D3")
name_entry=Entry()

#function to display the massage
def display():
    #read input given by user
    name=name_entry.get()
    #declaring a global variable
    #to make is acceseble anywhere in the program 
    global massage
    massage="Welcome to the aplication!\n today's date is: "
    greet="Hello "+name +"\n"
    #display details in a text box
    #specify where to add the details inside the text box
    text_box.insert(END,greet)
    text_box.insert(END,massage)
    text_box.insert(END,date.today())
    #add a text widget to display information
text_box=Text(height=3)
#add button to give value of command as name of the function
#press button,display function will be clear automatically
btn=Button(text="Begin",command=display,height=1,bg="black",fg="white")

#organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()

