import tkinter as tk


window=tk.Tk()
window.configure(background="orange")
window.geometry("600x600+400+80")
window.title("secure entrance")
window.resizable(width="FALSE", height="FALSE")

title=tk.Label(window,text="NL ATM", fg="white", bg="orange", font="Times 30 bold")
title.pack()

# entryBox = tk.Entry(window)
# entryBox.place(x = 200, y = 50, width=200,height=50)
#
# button_login = tk.Button(window,text="Log In",width=10,height=2, fg="orange",font=("Verdana","8","bold"))
# button_login.pack(pady=60)

button_1=tk.Button(window,text="Check Balance",width=20,height=5, fg="orange",font=("Verdana","10","bold"))
button_1.place(x=20,y=100)

button_2=tk.Button(window,text="Insert Money",width=20,height=5,fg="orange",font=("Verdana","10","bold"))
button_2.place(x=20,y=250)

button_3=tk.Button(window,text="Withdraw Money",width=20,height=5,fg="orange",font=("Verdana","10","bold"))
button_3.place(x=20,y=400)

button_4=tk.Button(window,text="Transfer Money",width=20,height=5,fg="orange",font=("Verdana","10","bold"))
button_4.place(x=390,y=100)

button_5=tk.Button(window,text="Edit User Information",width=20,height=5,fg="orange",font=("Verdana","10","bold"))
button_5.place(x=390,y=250)

button_6=tk.Button(window,text="Log out",width=20,height=5,fg="orange",font=("Verdana","10","bold"))
button_6.place(x=390,y=400)

button_7=tk.Button(window,text="kerim&erkan@partnership.com",width=30,height=2,fg="orange",font=("Verdana","10","bold"))
button_7.place(x=150,y=550)

window.mainloop()