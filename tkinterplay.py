
import tkinter as tk
from tkinter import ttk

from playsound import playsound


root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
ttk.Style().configure('green/black.TButton', foreground='green', background='black')

label = ttk.Label(root, text='I am a ttk.Label with text!', style='green/black.TLabel') 
label.pack()

button = ttk.Button(root, text='Click Me!', style='black/black.TButton')
button.pack()

def lift_win1():
    win1.lift(aboveThis=root)
def lower_win1():
    win1.lower(belowThis=root)
    gotobed = tk.Toplevel(win1, bg='red')
    playsound('woosh.wav')
    l = tk.Label(gotobed, text="my mom said so")
    b = tk.Button(gotobed, text="do not press this", command=lower_win1)
    l.pack()
    b.pack()

root = tk.Tk()
root.title('root win')
root.geometry("200x100+30+30")
root.configure(bg='yellow')
# create a child/top window
win1 = tk.Toplevel(bg='red')
win1.title('top/child window win1')
win1.geometry("300x150+120+120")
btn_lift = tk.Button(win1, text="Why would you ever press this button?", command=lift_win1)
btn_lift.pack(padx=30, pady=5)
btn_lower = tk.Button(win1, text="MY MOM SAID SO", highlightbackground="blue", highlightthickness="30", command=lower_win1)

btn_lower.pack(pady=5)
win1.mainloop()


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # background="..." doesn't work...
# ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
# ttk.Style().configure('green/black.TButton', foreground='green', background='black')

# label = ttk.Label(root, text='I am a ttk.Label with text!', style='green/black.TLabel')
# label.pack()

# button = ttk.Button(root, text='Click Me!', style='green/black.TButton')
# button.pack()


