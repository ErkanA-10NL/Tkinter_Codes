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

title=tk.Label(window,text="Enter your name:", fg="white", bg="orange", font="Times 15 bold")
title.place(x=50,y=150)

title=tk.Label(window,text="Create your password:", fg="white", bg="orange", font="Times 15 bold")
title.place(x=50,y=250)

title=tk.Label(window,text="Enter your mail:", fg="white", bg="orange", font="Times 15 bold")
title.place(x=50,y=350)

button_1=tk.Button(window,text="Creating New User Account",width=30,height=2,fg="orange",font=("Verdana","10","bold"))
button_1.place(x=150,y=400)

button_2=tk.Button(window,text="Go to User Page",width=30,height=2,fg="orange",font=("Verdana","10","bold"))
button_2.place(x=150,y=450)

entryBox = tk.Entry(window)
entryBox.place(x = 250, y = 150, width=200,height=30)

entryBox = tk.Entry(window)
entryBox.place(x = 250, y = 250, width=200,height=30)

entryBox = tk.Entry(window)
entryBox.place(x = 250, y = 350, width=200,height=30)

button_7=tk.Button(window,text="kerim&erkan@partnership.com",width=30,height=2,fg="orange",font=("Verdana","10","bold"))
button_7.place(x=150,y=550)

window.mainloop()

