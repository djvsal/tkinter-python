import tkinter as tk
import random
window=tk.Tk()
window.title('Greetings____')
window.geometry('400x400')


#FUNCTIONS
def phrase_generator():
	phrases=['hello','whats up', 'aloha','Nameste']
	name=str(entry1.get())
	return phrases[random.randint(0,3)] + name


def phrase_display():
	greeting=phrase_generator()# store the greeting in greeting

	#this creates the text field
	greeting_display=tk.Text(master=window, height=10,width=30)  # putting inside the window
	greeting_display.grid(column=0, row=3)

	greeting_display.insert(tk.END, greeting)

#LABEL
label1=tk.Label(text='welcome to my app')
label1.grid(column=0,row=0)

label2=tk.Label(text='what is your name?')
label2.grid(column=0,row=1)

#ENTRIES
entry1=tk.Entry()
entry1.grid(column=1,row=1)

#BUTTON
button1=tk.Button(text='click me', command=phrase_display, bg='red')
button1.grid(column=0,row=2)

window.mainloop()
