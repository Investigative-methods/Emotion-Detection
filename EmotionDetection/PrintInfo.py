from Tkinter import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import Tkinter as tk
def PrintInfo():
    window = tk.Tk()
    window.title("Evaluate testing data")
         
    window.geometry('800x500')
             
    lbl_text1 = tk.Label(window, text="EmotionDetection v1, sentiment analysis system operating off a multinomial Naive Bayes classififer")                           
    lbl_text1.grid(column=0, row=0)

            #lbl_text2 = Label(window, text=) ""
            #lbl_text2.grid(column=0, row=2)
    lbl_text3 = Label(window, text="There are 13 possible labels that text can be labelled as, the emotions are :empty, sadness, enthusiasm, neutral, worry, surprise, love, fun, hate, happiness, boredom, relief and anger.")
    lbl_text3.grid(column=0, row=2)


    lbl_text5 = Label(window, text="1. Training      - Generates a WordMap using a text file and emotion value file.")
    lbl_text5.grid(column=0, row=4)

    lbl_text6 = Label(window, text="                   A word map is required for both testing and evaluation.")
    lbl_text6.grid(column=0, row=5)

    lbl_text7 = Label(window, text="2. Testing       - Run the system and test its accuracy by supplying correct ")
    lbl_text7.grid(column=0, row=6)

    lbl_text8 = Label(window, text="                   emotion values. Also produces reports and confusion plot")
    lbl_text8.grid(column=0, row=7)

    lbl_text9 = Label(window, text="3. Evaluate Text - Run the system without given values. Used to evaluate input")
    lbl_text9.grid(column=0, row=8)

    lbl_text10 = Label(window, text="                    file that has not been pre-labelled.t")
    lbl_text10.grid(column=0, row=9)  

    mainloop()
            
        
 

