try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from Tkinter import *

from EmotionDetection import WordMap
from EmotionDetection import EvaluateText
from EmotionDetection import GUI
from EmotionDetection import Training
from EmotionDetection import Testing
from EmotionDetection import Evaluate
from EmotionDetection import PrintInfo

import sys
reload(sys)
sys.setdefaultencoding('utf8')

main = tk.Tk()
main.deiconify() 
v = tk.IntVar()

top = tk.Frame(main, bg="white",width=600, height=100)

center = tk.Frame(main, bg="SlateGray2",width=400, height=400)
bottom = tk.Frame(main, bg="white",width=600, height=100)

top.grid(row=1,column=1)
center.grid(row=2,column=1)
bottom.grid(row=3,column=1)


top.pack_propagate(0)
center.pack_propagate(0)
bottom.pack_propagate(0)
v.set(0)

choice = 0
flag = " "

options = [
    ("Training"),
    ("Testing"),
    ("Evaluate Text"),
    ("GUI Evaluation"),
    ("Information"),
    ("Exit")
]

tk.Label(center, text=" ", fg="black", bg="SlateGray2", anchor="ne", justify="left").pack()
tk.Label(center, text="Emotion Detection", fg="black", bg="SlateGray2", font=("Arial Bold", 20), padx=20, justify="left").pack()
tk.Label(center, text=" ", fg="white", bg="SlateGray2", justify="left").pack()
tk.Label(center, text=" ", fg="white", bg="SlateGray2", justify="left").pack()

def ShowChoice():
    global choice
    choice = v.get()

def submit():
        global choice, flag
        if choice == 0 and flag == " ":
            flag = "X"    
            train()
        elif choice == 1:
            test()
        elif choice == 2:
            evaluate()
        elif choice == 3:
            gui()
        elif choice == 4:
            printInfo()
        elif choice == 5:
            main.destroy()
        else:
            choice = True
            
for val, option in enumerate(options):
    tk.Radiobutton(center, 
                  text=option, 
                  padx=20,
                  bg="SlateGray2", 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

tk.Label(center, text=" ", fg="white", bg="SlateGray2", anchor="ne", justify="left").pack()
tk.Label(center, text=" ", fg="white", bg="SlateGray2", anchor="ne", justify="left").pack()
button = Button(center, text="Submit" , bg="Gray", width=10, padx=10, command=submit)
button.pack()

def train():
    window = Training.Training()    
def test():
    window = Testing.Testing()
    print "Results"
def evaluate():
    window = Evaluate.Evaluate()
    print "Results"
def gui():
    window = GUI.Evaluator()
def printInfo():
    window = PrintInfo.PrintInfo()

tk.mainloop()
            
# Training Program, builds map of words and emotion values from annotated corpus

    





