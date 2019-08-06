# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:20:27 2019

@author: MR
"""

#Executable file

#import modules needed and classes file
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as box
from PIL import ImageTk, Image
import Farming19cl_t
import numpy as np
from random import random
#import plotting
import matplotlib.pyplot as plt
from time import *

import pytest

#__spec__=None

#main window, title, image
win=Tk()
win.title('Farming 19')
img=ImageTk.PhotoImage(Image.open('farming19.jpg'))

#testing
if __name__=='__main__':
    test=0
else:
    test=1

#instances
var=Farming19cl_t.Vars()
gui=Farming19cl_t.Gui(win,img)
p1=Farming19cl_t.Players(1,gui.framep1,'red')
p2=Farming19cl_t.Players(2,gui.framep2,'green')
p3=Farming19cl_t.Players(3,gui.framep3,'blue')
p4=Farming19cl_t.Players(4,gui.framep4,'magenta')
p5=Farming19cl_t.Players(5,gui.framep5,'cyan')

cardssa1=Farming19cl_t.SSA1()
cardssa2=Farming19cl_t.SSA2()
cardssa3=Farming19cl_t.SSA3()
cardssa4=Farming19cl_t.SSA4()
carddhc1=Farming19cl_t.DHC1()
carddhc2=Farming19cl_t.DHC2()
carddhc3=Farming19cl_t.DHC3()
carddhc4=Farming19cl_t.DHC4()
card0=Farming19cl_t.Card0()
card1=Farming19cl_t.Card1()
card2=Farming19cl_t.Card2()
card3=Farming19cl_t.Card3()
card4=Farming19cl_t.Card4()
card5=Farming19cl_t.Card5()
card6=Farming19cl_t.Card6()
card7=Farming19cl_t.Card7()
card8=Farming19cl_t.Card8()
card9=Farming19cl_t.Card9()
card10=Farming19cl_t.Card10()
card11=Farming19cl_t.Card11()
card12=Farming19cl_t.Card12()
card13=Farming19cl_t.Card13()
card14=Farming19cl_t.Card14()
card15=Farming19cl_t.Card15()
card16=Farming19cl_t.Card16()
card17=Farming19cl_t.Card17()
card18=Farming19cl_t.Card18()
card19=Farming19cl_t.Card19()
card20=Farming19cl_t.Card20()
card21=Farming19cl_t.Card21()
card22=Farming19cl_t.Card22()
card23=Farming19cl_t.Card23()
card24=Farming19cl_t.Card24()
card25=Farming19cl_t.Card25()
card26=Farming19cl_t.Card26()
card27=Farming19cl_t.Card27()
card28=Farming19cl_t.Card28()
card29=Farming19cl_t.Card29()
card30=Farming19cl_t.Card30()
card31=Farming19cl_t.Card31()
card32=Farming19cl_t.Card32()
card33=Farming19cl_t.Card33()
card34=Farming19cl_t.Card34()
card35=Farming19cl_t.Card35()
card36=Farming19cl_t.Card36()
card37=Farming19cl_t.Card37()
card38=Farming19cl_t.Card38()
card39=Farming19cl_t.Card39()
card40=Farming19cl_t.Card40()
card41=Farming19cl_t.Card41()
card42=Farming19cl_t.Card42()
card43=Farming19cl_t.Card43()
card44=Farming19cl_t.Card44()
card45=Farming19cl_t.Card45()
card46=Farming19cl_t.Card46()
card47=Farming19cl_t.Card47()
card48=Farming19cl_t.Card48()
card49=Farming19cl_t.Card49()
card50=Farming19cl_t.Card50()
card51=Farming19cl_t.Card51()
card52=Farming19cl_t.Card52()
card53=Farming19cl_t.Card53()
debt=Farming19cl_t.Debt()
stocklim=Farming19cl_t.Stocklimit()
deck=[card0,card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30,card31,card32,card33,card34,card35,card36,card37,card38,card39,card40,card41,card42,card43,card44,card45,card46,card47,card48,card49,card50,card51,card52,card53,'null',cardssa1,cardssa2,cardssa3,cardssa4,carddhc1,carddhc2,carddhc3,carddhc4,'null',debt,stocklim]

game=Farming19cl_t.Game(gui,var,p1,p2,p3,p4,p5,win,deck,test)

#fpset=[fp1,fp2,fp3,fp4,fp5]

#pytest.main('farming19test.py')

#if __name__=='__main__':    
win.mainloop()
#else:
    #print('testing')
