# Imports
from tkinter import *
from _struct import pack
#import numpy as np
import os
import math


#GUI Window -------------------------------------------------------
window = Tk()
window.title("DOMO Plan")
window.geometry('1280x1024')

def show_entry_fields():
    print("Distribution Plan\n")
    print("Lines Available: %s\nEst. Drop-In Lines: %s\nPlanned Lines: %s\nLabor (Picking): %s\nLabor (Support):%s" % (BoxDistrLines.get(), BoxDistrLineDrop.get(), BoxDistrLinePlan.get(), BoxDistrHrPick.get(), BoxDistrHrSupport.get()))
   
Label(window, text="Distribution Plan").grid(row=0)
Label(window, text="Lines Available:").grid(row=1)
Label(window, text="Est. Drop-In Lines:").grid(row=2)
Label(window, text="Planned Lines:").grid(row=3)
Label(window, text="Labor Hrs. (Picking):").grid(row=4)
Label(window, text="Labor Hrs. (Support):").grid(row=5)
labelresult = Label(window, text="LPH:  ")
labelresult.grid(row=7, column=1)

   
DistrLines = DoubleVar()
DistrLineDrop = DoubleVar()
DistrLinePlan = DoubleVar()
DistrHrPick = DoubleVar()
DistrHrSupport = DoubleVar()

#FUNCTIONS -------------------------------------------------------
# Calculate Plan LPH
def CalcDistro ():
    lines = float(DistrLinePlan.get())
    hours = float(DistrHrPick.get()) + float(DistrHrSupport.get())  #TODO:  Add var for Shipping hours
    if hours == 0:
        result = 0
    result = lines + hours
    labelresult.config(text="LPH:  %.1f" % result)
    return result



BoxDistrLines = Entry(window, textvariable=DistrLines)
BoxDistrLineDrop = Entry(window, textvariable=DistrLineDrop)
BoxDistrLinePlan = Entry(window, textvariable=DistrLinePlan)
BoxDistrHrPick = Entry(window, textvariable=DistrHrPick)
BoxDistrHrSupport = Entry(window, textvariable=DistrHrSupport)

BoxDistrLines.grid(row=1, column=1)
BoxDistrLineDrop.grid(row=2, column=1)
BoxDistrLinePlan.grid(row=3, column=1)
BoxDistrHrPick.grid(row=4, column=1)
BoxDistrHrSupport.grid(row=5, column=1)


btnCalcDistro = Button(window, text="Calculate Plan LPH", command=CalcDistro)
btnCalcDistro.grid(row=6, column=1)


print('\n')
print("Shipping Plan\n")
    

print("Seasonal Distr. Plan\n")
    

print("Receiving Plan (PNA)\n")
    

print("Receiving Plan (GM)\n")
    

print("Returns Plan\n")


print("Quality Plan\n")


window.mainloop()

