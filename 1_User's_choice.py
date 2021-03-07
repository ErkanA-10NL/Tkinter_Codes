import tkinter as tk

window=tk.Tk()
window.configure(background="orange")
window.geometry("600x600+400+80")
window.title("secure entrance")
window.resizable(width="FALSE", height="FALSE")

title=tk.Label(window,text="NL ATM", fg="white", bg="orange", font="Times 30 bold")
title.pack()

title=tk.Label(window,text="***Welcome to ATM***", fg="white", bg="orange", font="Times 20 bold")
title.pack()

button_1=tk.Button(window,text="User Login",width=20,height=5, fg="orange",font=("Verdana","15","bold"))
button_1.place(x=150,y=150)

button_2=tk.Button(window,text="New User",width=20,height=5, fg="orange",font=("Verdana","15","bold"))
button_2.place(x=150,y=300)

button_3=tk.Button(window,text="kerim&erkan@partnership.com",width=30,height=2,fg="orange",font=("Verdana","10","bold"))
button_3.place(x=150,y=550)

window.mainloop()