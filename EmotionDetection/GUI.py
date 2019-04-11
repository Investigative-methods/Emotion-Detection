# this is final gui window developed by suresh
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from sys import argv    
from Tkinter import *
from Tkinter import PhotoImage
from math import log10
import pdb
from WordFilter import WordFilter
from EvaluateText import evaluateWord
from EvaluateText import guessEmotion

remove = ' '
canvas = ' '
text = ' '
canvas1 = ' ' 
class Evaluator():
    def __init__(self):
        global main, text
        main = tk.Tk()
        main.title("Emotion Evaluator")
        main.geometry('1000x700')
        tk.Label(main, text="Input text:", font=(None, 15)).grid(row=0, sticky="nsew", pady=5)
    
        self.inputStr = tk.Entry(main, font=(None, 10), width=50)

        self.inputStr.grid(row=0, column=1, sticky="nsew", pady=10, padx=(0, 10))

        tk.Button(main,
                  text='Clear',
                  command=self.clearButton,
                  font=(None, 10)).grid(row=2, column=0, stick="nsew", pady=(8, 2), padx=10)
        tk.Button(main,
                  text='Quit',
                  command=main.destroy,
                  font=(None, 10)).grid(row=3, column=0, sticky="nsew", pady=(2, 8), padx=10)
        tk.Button(main,
                  text='Predict',
                  command=self.predButton,
                  font=(None, 15)).grid(row=2, column=1, rowspan=2, sticky="nsew", pady=9, padx=20)
       
        
        tk.mainloop()
        
    def predButton(self):
        global canvas, remove, canvas1
        if canvas == ' ' and  canvas1 == ' ':
            canvas1 = tk.Canvas(main, width=200, height=400)
            canvas1.pack(side=LEFT)
            
            canvas = tk.Canvas(main, width=600, height=400)
            canvas.pack(side=BOTTOM)

            
        with open("./data/Priors.csv", "r") as priorFile:
            priors = priorFile.readline().strip().split(',')[1:]
            priors = [log10(float(x)) for x in priors]
        predValues = []
        unfound = []

        wf = WordFilter()
        words = self.inputStr.get()
        print "Input:", words
        words = wf.filterWords(words)

        print "Tokens:", words
        for word in words:
            try:
                values = evaluateWord(word)
            except IOError:
                print "WordMap not found. Please train system first.\n"
                raise
            if values is not None:
                predValues.append(values)
            else:
                unfound.append(word)

        predValues = map(sum, zip(*predValues))
        predProb = map(sum, zip(priors, predValues))
        predEmotion = guessEmotion(predProb)

#Redraw the canvas for each prediction
        if remove=='X':  
            canvas.delete('all')
            canvas1.delete('all')
  
        text = choice = predEmotion
        if text == ' ':
            text = 'Empty'
            
        label = canvas1.create_text(100,10,text='Predicted Emotion:  '+text)             

        if choice in ('Empty'):
            self.getImage('Empty.gif')
        elif choice in ('Sadness', 'Sad'):
            self.getImage('Sadness.gif')
        elif choice == 'Enthusiasm':
            self.getImage('Enthusiasm.gif')
        elif choice == 'neutral':
            self.getImage('Neutral.gif')
        elif choice in ('Worri', 'worry'):
            self.getImage('Worry.jpg')
        elif choice == 'Surprise':
            self.getImage('Surprise.gif')
        elif choice == 'Love':
            self.getImage('love.gif')
        elif choice == 'Fun':
            self.getImage('Fun.gif')
        elif choice == 'hate':
            self.getImage('Hate.gif')
        elif choice in ('happy','Happiness'):
            self.getImage('Happiness.gif')
        elif choice in ('bore','Boredom'):
            self.getImage('Boredom.gif')
        elif choice == 'Relief':
            self.getImage('Relief.gif')
        elif choice == 'Anger':     
            self.getImage('Anger.gif')
        else:
            self.getImage('Empty.gif')
            
        print "Unfound:", unfound
        print "Prob:", ','.join([('%.2f ') % x for x in predProb])
        
    def clearButton(self):
        global text, canvas, canvas1
        canvas.delete('all')
        canvas1.delete('all')
        text = ' '
        self.inputStr.delete(0, 'end')

    def getImage(self,image):
        global canvas
        main.photo = photo = PhotoImage(master = canvas, file=image)   
        canvas.create_image(0, 0, image=photo, anchor='nw')
        self.setFlag('X')
        
    def setFlag(self,flag):
        global remove
        remove = 'X'
        
 
