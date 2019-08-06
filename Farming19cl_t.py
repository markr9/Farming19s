# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:20:15 2019

@author: MR
"""

#Classes

#import tkinter, plotting as plt and pil for image
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as box
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
from random import random
from time import *
#import multiprocessing as mp
#import signal
import threading
import queue
import time

import pytest

class Guicommonfn:
    '''Base class of common gui functions'''
    
    def enable(self,x,v):
        '''Enable or disable a widgit: v=1 enable, v=0 disable, x=widgit in class to change'''
        if v==1:
            x.configure(state=NORMAL)
        elif v==0:
            x.configure(state=DISABLED)
        else:
            print('er enable')
            
    def getvalue(self,x):
        '''Get value from widgit: x=widgit to get from'''
        a=x.get()
        return a
        
    def settxvalue(self,x,tx):
        '''Set text in label wigit: x=wigit, tx=text/value'''
        x.configure(text=tx)
        
class NumericUpDown(Guicommonfn):
    '''Numerical Up Down wigit set'''
    count=0
    value=0
    incup=1
    incdown=1
    maxvalue=75
    minvalue=0
    
    def __init__(self,frame,ur,uc,dr,dc,vr,vc,stick):
        '''Set frame and posistion for widget set: frame=frame to put in, ur=up button row, uc=up button column, dr=down button row, dc=down button column, vr=value row, vc=value column'''
        #create widgits
        self.frame=frame
        self.btnup=Button(frame,text='+',command=lambda:self.up(),width=1)
        self.btndown=Button(frame,text='-',command=lambda:self.down(),width=1)
        self.txvalue=Label(frame,text=0)
        #set posistion and defaults
        self.pos(ur,uc,dr,dc,vr,vc,stick)
        self.defaults()
        
    def pos(self,ur,uc,dr,dc,vr,vc,stick):
        '''Posistion wigit set'''
        self.btnup.grid(row=ur,column=uc,sticky=stick)
        self.btndown.grid(row=dr,column=dc,sticky=stick)
        self.txvalue.grid(row=vr,column=vc,sticky=E)
    
    def up(self):
        '''Up button fn'''
        if self.value<=(self.maxvalue-self.incup):
            self.value+=self.incup
            self.txvalue.configure(text=self.value)
        else:
            self.value=self.value
            
    def down(self):
        '''Down button fn'''
        if self.value>=(self.minvalue+self.incdown):
            self.value-=self.incdown
            self.txvalue.configure(text=self.value)
        else:
            self.value=self.value
            
    def defaults(self):
        '''Default button states'''
        self.btnup.configure(state=DISABLED)
        self.btndown.configure(state=DISABLED)
            
    def enable(self,v):
        '''Enable v=1 or diable v=0 the widgit'''
        if v==1:
            self.btnup.configure(state=NORMAL)
            self.btndown.configure(state=NORMAL)
        elif v==0:
            self.btnup.configure(state=DISABLED)
            self.btndown.configure(state=DISABLED)
        else:
            print('er enable')

    def reset(self):
        '''Reset the value to 0'''
        self.value=0
        self.txvalue.configure(text=self.value)
        
    def setvalues(self,start=0,incup=1,incdown=1,maxv=75,minv=0):
        '''Set the values of the button: start=value to start at, incup=increment of the value up, indown=increment down, maxv=max value allowed, minv= min value allowed'''
        self.value=start
        self.maxvalue=maxv
        self.minvalue=minv
        self.incup=incup
        self.incdown=incdown
        self.txvalue.configure(text=self.value)
        
    def getvalue(self):
        '''Get value from widgit'''
        a=self.value
        return a

    #destructor method
    def __del__(self):
        print('op destroyed')
            
class Gui(Guicommonfn):
    '''Graphics class'''
    #changes to make: fix screen size via player frame and options text plus ancher parts
    def __init__(self,win,img):
        #setting up window
        self.win=win
        self.img=img
        swidth=win.winfo_screenwidth()
        sheight=win.winfo_screenheight()
        print(swidth,sheight)
        s=str(swidth)+'x'+str(sheight)
        #win.geometry(s)
        
        #checkbox values
        self.opv1=IntVar()
        self.opv2=IntVar()
        self.opv3=IntVar()
        self.opv4=IntVar()
        self.opv5=IntVar()
        self.opv6=IntVar()
        
        #progress bar value
        self.pbarvalue=0
        
        #frames
        self.frame=Frame(win)
        self.framep1=Frame(self.frame,bg='red')
        self.framep2=Frame(self.frame,bg='green')
        self.framep3=Frame(self.frame,bg='blue')
        self.framep4=Frame(self.frame,bg='magenta')
        self.framep5=Frame(self.frame,bg='cyan')
        self.tlframe=Frame(self.frame)
        self.trframe=Frame(self.frame)
        self.bframe=Frame(self.frame)
        self.txframe=Frame(self.frame,bg='white')
        self.mframe=Frame(self.frame)#self.txframe)#,width=618,height=200)
        self.tmframe=Frame(self.txframe)
        #self.mframe.grid_propagate(False)
        self.oframe=Frame(self.frame,bg='white')
        self.tframe=Frame(self.frame)
        self.dframe=Frame(self.frame)
        
        #display fns
        self.farmepos()
        self.widgits()
        self.pos()
        self.defaults()
        self.btnwidgits()
        self.btnpos()
        self.btndefaults()
        self.config()
        
    def farmepos(self):
        '''Position frames'''
        self.frame.grid(row=1,column=1)
        self.tlframe.grid(row=1,column=1)
        self.tframe.grid(row=1,column=2)
        self.trframe.grid(row=1,column=3)
        #self.txframe.grid(row=2,column=2,rowspan=2)
        #self.tmframe.pack()#side=TOP)
        #self.mframe.pack()#side=TOP)
        #self.tmframe.grid(row=2,column=2,sticky=N)
        self.mframe.grid(row=2,column=2,rowspan=1)#,sticky=N)
        self.oframe.grid(row=3,column=2)
        self.bframe.grid(row=4,column=2)
        self.dframe.grid(row=4,column=3)
        self.framep1.grid(row=2,column=1,rowspan=1,pady=(20,0))
        self.framep2.grid(row=2,column=3,rowspan=1,pady=(20,0))
        self.framep3.grid(row=3,column=1)#,pady=(0,15))
        self.framep4.grid(row=3,column=3)#,pady=(0,15))
        self.framep5.grid(row=4,column=1,sticky=N)#,pady=(0,15))
        
    def widgits(self):
        '''Widgits'''
        #top-left
        self.txpnum=Label(self.tlframe,text='Number of Players')
        self.pnum=Combobox(self.tlframe,values=[2,3,4,5],width=5)
        #top-right
        self.txpbar=Label(self.trframe,text='Progress')
        self.pbar=Progressbar(self.trframe)
        self.pbarar=Progressbar(self.trframe)
        #top
        self.image=Canvas(self.tframe,width=618,height=98,bg='yellow')
        self.image.create_image(0,-6,image=self.img,anchor='nw')
        #self.image.image=self.img
        #middle
        self.txcard=Label(self.mframe,text='##',font=('',10))#,anchor='nw')
        self.txf=Label(self.mframe,text='FARMING',font=('',10))#,anchor='ne',height=1,width=8,relief=SUNKEN)
        self.txtitle=Label(self.mframe,text='Title',anchor='n',font=('',12,'bold'),height=2)
        self.txmain=Message(self.mframe,width=612,relief=SUNKEN,text='Main text',anchor='n')
        self.txoutput=Message(self.oframe,width=612,relief=SUNKEN,text='Output text')#,anchor='n')
        #self.labelrow=Label(self.mframe,width=86,height=0,relief=SUNKEN)
        #self.labelcol=Label(self.mframe,height=9,width=0,relief=SUNKEN)
        #bottom right
        self.dtitle=Label(self.dframe,text='Dice',pady=10,font=('',12))
        self.txdroll=Label(self.dframe,text=6)
        self.txdiceroll=Label(self.dframe,text='Dice Roll:')
        self.dice=Combobox(self.dframe,value=[1,2,3,4,5,6],width=5)
        self.txblank=Label(self.dframe,text='',height=5)
        #bottom
        self.opstitle=Label(self.bframe,text='Player options',font=('',12))
        self.txpops=Label(self.bframe,text='Player buying:')
        self.pops=Combobox(self.bframe,width=10)
        self.txpound=Label(self.bframe,text='£')
        self.cb1=Checkbutton(self.bframe,text='Option 1',variable=self.opv1,onvalue=1,offvalue=0)
        self.cb2=Checkbutton(self.bframe,text='Option 2',variable=self.opv2,onvalue=1,offvalue=0)
        self.cb3=Checkbutton(self.bframe,text='Option 3',variable=self.opv3,onvalue=1,offvalue=0)
        self.cb4=Checkbutton(self.bframe,text='Option 4',variable=self.opv4,onvalue=1,offvalue=0)
        self.cb5=Checkbutton(self.bframe,text='Option 5',variable=self.opv5,onvalue=1,offvalue=0)
        self.cb6=Checkbutton(self.bframe,text='Option 6',variable=self.opv6,onvalue=1,offvalue=0)
        #own made widgits
        self.mop=NumericUpDown(self.bframe,2,4,2,7,2,6,'w')
        self.op1=NumericUpDown(self.bframe,3,1,4,1,3,2,'e')
        self.op2=NumericUpDown(self.bframe,5,1,6,1,5,2,'e')
        self.op3=NumericUpDown(self.bframe,7,1,8,1,7,2,'e')
        self.op4=NumericUpDown(self.bframe,3,4,4,4,3,5,'e')
        self.op5=NumericUpDown(self.bframe,5,4,6,4,5,5,'e')
        self.op6=NumericUpDown(self.bframe,7,4,8,4,7,5,'e')
        self.cb=[self.cb1,self.cb2,self.cb3,self.cb4,self.cb5,self.cb6]
        self.op=[self.op1,self.op2,self.op3,self.op4,self.op5,self.op6]
        
    def pos(self):
        ''''Posistion widgits'''
        #top left
        self.txpnum.grid(row=1,column=1)
        self.pnum.grid(row=2,column=1)
        #top right
        self.txpbar.grid(row=1,column=1)
        self.pbar.grid(row=2,column=1)
        self.pbarar.grid(row=3,column=1)
        #top
        self.image.grid(row=1,column=1,columnspan=2)
        #middle
        #self.labelrow.grid(row=3,column=1,columnspan=2)
        #self.labelrow.lower()
        #self.labelcol.grid(row=3,column=1)
        #self.labelcol.lower()
        self.txcard.grid(row=1,column=1,sticky=NW)
        self.txf.grid(row=1,column=2,sticky=NE)
        self.txtitle.grid(row=2,column=1,columnspan=2)#,sticky=E+W)
        self.txmain.grid(row=3,column=1,columnspan=2,sticky=N+E+S+W)#,sticky=S)
        self.txoutput.grid(row=1,column=1,columnspan=2,sticky=N+E+S+W)
       
#        self.txcard.pack(anchor=NW)#anchor='nw',side=LEFT,fill=X)
#        self.txf.pack()#anchor='ne',side=RIGHT,fill=X)
#        self.txtitle.pack()#fill=X,side=TOP)
#        self.txmain.pack()#side=TOP)
#        self.txoutput.pack()#side=TOP)
#        self.labelrow.pack()#side=TOP)
        #bottom right
        self.dtitle.grid(row=1,column=2)
        self.txdroll.grid(row=2,column=2)
        self.txdiceroll.grid(row=3,column=1)
        self.dice.grid(row=3,column=2)
        self.txblank.grid(row=4,column=1,columnspan=3)
        #bottom
        self.opstitle.grid(row=1,column=1,columnspan=7)
        self.txpops.grid(row=2,column=1,columnspan=2)
        self.pops.grid(row=2,column=3)
        self.txpound.grid(row=2,column=5)
        self.cb1.grid(row=3,column=3)
        self.cb2.grid(row=5,column=3)
        self.cb3.grid(row=7,column=3)
        self.cb4.grid(row=3,column=6,columnspan=2)
        self.cb5.grid(row=5,column=6,columnspan=2)
        self.cb6.grid(row=7,column=6,columnspan=2)
        
    def config(self):
        '''m'''
        #configuration
        self.frame.grid_columnconfigure(1,weight=1)
        self.bframe.grid_columnconfigure(1,weight=1)
        self.bframe.grid_columnconfigure(7,weight=1)
        self.oframe.grid_columnconfigure(1,minsize=618)
        self.oframe.grid_rowconfigure(1,minsize=190)
        self.mframe.grid_columnconfigure(1,minsize=309)
        self.mframe.grid_columnconfigure(2,minsize=309)
        self.mframe.grid_rowconfigure(3,minsize=143)
        #a=self.framep2.winfo_height()
        #print(a)
        #self.win.grid_columnconfigure(1,minsize=a)
        #self.win.grid_columnconfigure(2, weight=1)
        
    def defaults(self):
        '''Widgits deafults on start'''
        #top-left
        self.pnum.configure(state=NORMAL)
        self.pnum.set(2)
        #top-right
        #none
        #top
        #none
        #self.image.image=self.img
        #middle
        #none
        #bottom right
        self.dice.configure(state=DISABLED)
        self.dice.set(6)
        #bottom
        self.popvalues=['None',1,2,3,4,5]
        self.pops.configure(state=DISABLED,value=self.popvalues)
        self.pops.set('None')
        self.cb1.configure(state=DISABLED)
        self.cb2.configure(state=DISABLED)
        self.cb3.configure(state=DISABLED)
        self.cb4.configure(state=DISABLED)
        self.cb5.configure(state=DISABLED)
        self.cb6.configure(state=DISABLED)
        self.txtitle.configure(text='WELCOME')
        self.txcard.configure(text=0)
        self.txmain.configure(text='Welcome to Farming. For this game you need at least 2 players, 1 dice and a calculator (or human equivalent).\nBasic rules: each card will be resolved as a whole action, not several actions. Players may therefore not be in debt after any card, but may during a card. When resolving a card if an action cannot be done, it will be completed as well as possible. All players are subjected to stock limits of: 75 cows, 60 ewes, 20 sow and 4 horses to keep within ECC regulation. If any player goes above this limit they will be notified and stock returned to the limit.')
        self.txoutput.configure(text='Select the number of players in the drop down box in the top left corner and click the adjacent Select button.')
    
    #button wigits
    def btnwidgits(self):
        '''Button widgitd'''
        self.btnpnum=Button(self.tlframe,text='Select')
        self.btndice=Button(self.dframe,text='Roll Dice!')
        self.btndselect=Button(self.dframe,text='Select')
        self.btnadvance=Button(self.dframe,text='Advance')
        self.btnnext=Button(self.dframe,text='Next Card')
        self.btnquit=Button(self.dframe,text='Quit')

    def btnpos(self):
        '''Posistion for buttons'''
        self.btnpnum.grid(row=3,column=1)
        self.btndice.grid(row=2,column=1)
        self.btndselect.grid(row=3,column=3)
        self.btnadvance.grid(row=5,column=1,sticky='s')
        self.btnnext.grid(row=5,column=2,sticky='s')
        self.btnquit.grid(row=5,column=3,sticky='s')
        
    def btndefaults(self):
        '''Defaults for buttons'''
        self.btnpnum.configure(state=NORMAL)
        self.btndice.configure(state=DISABLED)
        self.btndselect.configure(state=DISABLED)
        self.btnadvance.configure(state=DISABLED)
        self.btnnext.configure(state=DISABLED)
        self.btnquit.configure(state=NORMAL)
    
    def settxop(self,num,tx):
        '''Set options text: num=number of options, text=array of text'''
        i=0
        while i<num:
            self.settxvalue(self.cb[i],tx[i])
            i+=1
        
    def resetcb(self,x):
        ''''Deselect combobox'''
        x.deselect()
        
    def cbenable(self,num,v):
        '''Enable v=1 or disable v=0 comboboxes: num=number to'''
        i=0
        while i<num:
            self.enable(self.cb[i],v)
            i+=1
            
    def openable(self,num,v):
        '''Enable v=1 or diable v=0 numeric up down options: num=number to'''
        i=0
        while i<num:
            self.op[i].enable(v)
            i+=1
            
    def btnswap(self,v):
        ''''Swap advance and next button state'''
        if v==1:
            self.btnadvance.configure(state=DISABLED)
            self.btnnext.configure(state=NORMAL)
        elif v==0:
            self.btnadvance.configure(state=NORMAL)
            self.btnnext.configure(state=DISABLED)
        else:
            print('er btn swap')
    
    #progess bar fn
    def progess(self):
        '''Increment progress bar by 1'''
        self.pbar.configure(value=self.pbarvalue)
        
    #destructor method
    def __del__(self):
        print('gui destroyed')
        
class Data:
    '''Data class'''
    #all info for each card start and end plus actions- ie a black box
    header='Card\tClick\tPlayer\tMoney\tCows\tEwes\tSows\tHorses\tHeifer\tBull\tLambs\tStore Pigs\tWheat\tBarley\tOates\tPotatoes\tLey\tRHP\nData is gathered at the end of a click.\n'
    f=0
    
    def createfile(self):
        '''Create and set up data file'''
        self.f=open('dataf19.txt','w')
        self.f.write(self.header)
        self.f.close()
        
    def writedata(self,var,pset,deck):
        '''Write data to file: var=global variable instance, pset=player instance array, deck=card instance array'''
        self.f=open('dataf19.txt','a')
        tx=str(var.cardnum)+'\t'+str(deck[var.cardnum].click)+'\t'
        i=0
        while i<var.pnum:
            if i!=0:
                tx=tx+'\t\t'
            tx=tx+str(pset[i].pid)+'\t'+str(pset[i].money)+'\t'+str(pset[i].cows)+'\t'+str(pset[i].ewes)+'\t'+str(pset[i].sows)+'\t'+str(pset[i].horses)+'\t'+str(pset[i].hcalves)+'\t'+str(pset[i].bcalves)+'\t'+str(pset[i].lambs)+'\t'+str(pset[i].spigs)+'\t\t'+str(pset[i].wheat)+'\t'+str(pset[i].barley)+'\t'+str(pset[i].oats)+'\t'+str(pset[i].potatoes)+'\t\t'+str(pset[i].ley)+'\t'+str(pset[i].roots)+str(pset[i].hay)+str(pset[i].pasture)+'\n'
            i+=1
        self.f.write(tx)
        self.f.close()   
    
    def writefn(self,tx):
        '''Write fn name to file: tx=text to write'''
        self.f=open('dataf19.txt','a')
        self.f.write(tx)
        self.f.close()
        
    def writedice(self,player,roll):
        '''Writedice roll to file: player=player, roll=dice roll'''
        self.f=open('dataf19.txt','a')
        tx='\t\t'+str(player.pid)+'\t'+'Roll: '+str(roll)+'\n'
        self.f.write(tx)
        self.f.close()
        
class Game(Data):
    '''Game class'''
    def __init__(self,gui,var,p1,p2,p3,p4,p5,win,deck,test):
        '''Take isntances into game: gui, var, players, window, all cards'''
        self.win=win
        self.gui=gui
        self.var=var
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.p5=p5
        self.pset=[self.p1,self.p2,self.p3,self.p4,self.p5]
        self.deck=deck
        self.createfile()
        #set button commands
        self.btncommand()
        #testing
        self.test=test
        if self.test==1:
            self.testing()

    def btncommand(self):
        ''''Button commands'''
        #set later to allow passing of instances
        self.gui.btnpnum.configure(command=lambda:self.pnums())
        self.gui.btndice.configure(command=lambda:self.droll())
        self.gui.btndselect.configure(command=lambda:self.dselect())
        self.gui.btnadvance.configure(command=lambda:self.click())
        self.gui.btnnext.configure(command=lambda:self.nextcard())
        self.gui.btnquit.configure(command=lambda:self.quitgame())
    
    #button fns
    def ppos(self,inst):
        pass
        
    def pnums(self):
        '''Take the value from the players drop down list '''
        if self.test==0:
            self.gui.config()
            #get value
            self.var.pnum=int(self.gui.getvalue(self.gui.pnum))
            #set values for each player based on if in game
            self.p1.set0value(self.var.pnum)
            self.p2.set0value(self.var.pnum)
            self.p3.set0value(self.var.pnum)
            self.p4.set0value(self.var.pnum)
            self.p5.set0value(self.var.pnum)
            #set widigts for next screen
            self.gui.enable(self.gui.btnpnum,0)
            self.gui.enable(self.gui.pnum,0)
            self.gui.enable(self.gui.btnadvance,1)
            #run game fn
            self.game()
            #enable edditing of player names
            i=0
            while i<self.var.pnum:
                self.pset[i].enable(self.pset[i].txname,1)
                i+=1
        else:
            pytest.main(['farming19test.py'])
            
    def testing(self):
        self.gui.btnpnum.configure(text='Start Testing')
        self.gui.enable(self.gui.pnum,0)
        self.gui.txmain.configure(text='Testing!\nClick the Start Testing button to run unit tests.')
        self.gui.txoutput.configure(text='')
    
    def droll(self):
        a=int(random()*6+1)
        self.gui.settxvalue(self.gui.txdroll,a)
        self.deck[self.var.cardnum].diceresult(a,self.gui,self.var,self.deck[self.var.cardnum].dtype,self.deck[self.var.cardnum].txdice,self.deck[self.var.cardnum].tx,self.pset,self.deck[self.var.cardnum].pnum,self.writedice)
        #dhc2+3 test
        if ((self.var.cardnum==60 or self.var.cardnum==61) and self.deck[self.var.cardnum].dswitch==1):
            self.deck[self.var.cardnum].diceroll(self.gui,self.var,self.deck[self.var.cardnum].txdice2,self.deck[self.var.cardnum].tx2,self.pset,self.pset[self.deck[self.var.cardnum].click-7],self.deck[self.var.cardnum].drolldhc2,self.deck[self.var.cardnum].pay)
        #state changes
        self.gui.enable(self.gui.btndice,0)
        self.gui.enable(self.gui.btnadvance,1)
    
    def dselect(self):
        a=int(self.gui.getvalue(self.gui.dice))
        self.deck[self.var.cardnum].diceresult(a,self.gui,self.var,self.deck[self.var.cardnum].dtype,self.deck[self.var.cardnum].txdice,self.deck[self.var.cardnum].tx,self.pset,self.deck[self.var.cardnum].pnum,self.writedice)
        #dhc2+3 test
        if ((self.var.cardnum==60 or self.var.cardnum==61) and self.deck[self.var.cardnum].dswitch==1):
            self.deck[self.var.cardnum].diceroll(self.gui,self.var,self.deck[self.var.cardnum].txdice2,self.deck[self.var.cardnum].tx2,self.pset,self.pset[self.deck[self.var.cardnum].click-7],self.deck[self.var.cardnum].drolldhc2,self.deck[self.var.cardnum].pay)
        #state changes
        self.gui.enable(self.gui.btndselect,0)
        self.gui.enable(self.gui.dice,0)
        self.gui.enable(self.gui.btnadvance,1)
    
    def click(self):
        ''''Advance button action'''
        #increase click value for current card
        self.deck[self.var.cardnum].click+=1
        #run game fn
        self.game()
        
#    def handler(self):
#        #,signum,frame):
#        j=0
#        while j<self.var.pnum:
#                self.pset[j].atrisk(self.gui,self.var)
#                j+=1
#        #raise Exception
#        
#    def timer(self):
#        if self.timercount>self.totaltime:
#            if self.atriskid is not None:
#                self.win.after_cancel(self.atriskid)
#            print('at risk timeout')
#            self.var.atrisklim-=1
#        else:
#            self.timercount+=1
#            #self.win.after(1000)
#        print('hi')
        
    def runatrisk(self,th):
        j=0
        while j<self.var.pnum:
            if not th.isSet():
                self.pset[j].atrisk(self.gui,self.var,th)
            else:
                return
            j+=1
        self.queue.put("Task finished")
        self.win.after_cancel(self.job)
        self.gui.pbarar.configure(value=self.var.atriskprgress)
            
    def checkpb(self,gui,var,t):
        #print('heres')
        try:
            msg = self.queue.get(0)
            print(msg)
            #button swap
            self.gui.btnswap(0)
            self.nextp2()
            # Show result of the task if needed
        except queue.Empty:
            gui.pbarar.configure(value=var.atriskprgress)
            gui.pbarar.after(100,self.checkpb,gui,var,t)
#        if t.is_alive():
#            
#        else:
#            return
            
    def endatrisk(self,t,th):
        if t.is_alive():
            self.queue.put("Task not finished")
            print('At risk too long')
            self.var.atrisklim-=1
            var=box.showinfo('Risk','Risk function took too long to run, click to continue')
            #button swap
            self.gui.btnswap(0)
            self.nextp2()
        else:
            print('At risk done in time')
        th.set()
        t.join()
        print('pbarlim',self.var.atriskprgress)
    
    def nextcard(self):
        ''''Next button fn'''
        #stop card being in play- for inter card fn in game fn
        self.var.cardinplay=0
        #add data to graphs
        i=0
        while i<self.var.pnum:
            stock=[self.pset[i].cows,self.pset[i].ewes,self.pset[i].sows,self.pset[i].horses,self.pset[i].bcalves,self.pset[i].hcalves,self.pset[i].lambs,self.pset[i].spigs]
            money=self.pset[i].money
            self.pset[i].adddatagraph(self.var.cardnum,money,stock)
            i+=1
        #increase card num value for next card
        self.var.cardnum+=1
        #pbar increase
        self.gui.pbarvalue+=1
        self.gui.pbar.configure(value=self.gui.pbarvalue)
        #next disable
        self.gui.enable(self.gui.btnnext,0)
        #at risk run
        if self.var.atriskoption==1:
            self.gui.pbarar.configure(value=0)
            self.var.atriskprgress=0
            timeout=10
            totaltime=timeout*self.var.pnum
            self.queue = queue.Queue()
            th=threading.Event()
            t=threading.Thread(group=None,target=self.runatrisk,name=None, args=(th,))#target=self.runatrisk,name='atrisk',args(th,))
            #progress on thread
            pbmax=(39-(self.var.cardnum-1))*self.var.pnum
            self.gui.pbarar.configure(maximum=pbmax)
            print('pbar',pbmax)
            #self.checkpb(self.gui,self.var,t)
            #start
            t.start()
            self.gui.pbarar.after(100,self.checkpb,self.gui,self.var,t)
            self.job=self.gui.win.after(totaltime*1000,self.endatrisk,t,th)
            self.t=t
            self.th=th
            #t.join(totaltime)
            
#            timeout=1
#            self.totaltime=timeout*self.var.pnum*1000
#            #set up at risk and timer  fn
#            self.timercount=0
#            self.atriskid=None
#            self.win.after(1000,self.timer)
#            self.atriskid=self.win.after(1010,self.handler)
            
#                signal.signal(signal.SIGBREAK,self.handler)
#                signal.alarm(timeout)
#                try:
#                    self.pset[j].atrisk(self.gui,self.var)
#                    signal.alarm(0)
#                except Exception:
#                    self.var.atrisklim-=1
#                    j-=1
#                #if __name__ == '__main__':
#                    #__spec__=None
#                    #__spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
#                p=mp.Process(target=self.onefn)#,args=(self.gui,self.var,))#self.pset[j].atrisk(self.gui,self.var),name='atrisk')
#                print('reachhere')
#                p.start()
#                print('rh')
#                #time.sleep(timeout)
#                p.join(timeout)
#                if p.is_alive():
#                    print('atrisk timeout')
#                    p.terminate()
#                    p.join()
#                    self.var.atrisklim-=1
                
        elif self.var.cardnum==1:
            k=0
            while k<5:
                self.pset[k].settxvalue(self.pset[k].txc19,0)
                self.pset[k].settxvalue(self.pset[k].txc29,0)
                self.pset[k].settxvalue(self.pset[k].txc36,0)
                self.pset[k].settxvalue(self.pset[k].txc39,0)
                k+=1
            #button swap
            self.gui.btnswap(0)
            self.nextp2()
        else:
            #button swap
            self.gui.btnswap(0)
            self.nextp2()
        
    def nextp2(self):
        if self.var.atriskoption==1:
            #add to gui
            k=0
            while k<self.var.pnum:
                if self.pset[k].ingame==1:
                    self.pset[k].atriskgui(self.gui,self.var)
                k+=1
        #run game fn
        self.game()
    
    def quitgame(self):
        '''Quit button fn'''
        #display box to ask if sure
        var=box.askyesno('Quitting','Are you sure?')
        #yes button quits and no returns to game
        if var==1:
            self.th.set()
            self.t.join()
            self.win.destroy()
        else:
            print('Quit avoided')
            
    def getrandcard(self):
        '''Find lowest unsued random card number; returns a=card number'''
        cset=[100]
        i=0
        while i<8:
            if self.deck[55+i].used==0:
                cset.append(self.deck[55+i].cardnum2)
            i+=1
        a=min(cset)
        return a
        
    def findrandcard(self,num):
        '''Find random card from card number: num=card number'''
        i=0
        while i<8:
            if num==self.deck[55+i].cardnum2:
                pcardnum=self.var.cardnum
                self.var.cardnum=55+i
                self.deck[55+i].pcardnum=pcardnum
                break
            i+=1
            
    #inter card fn
    def inter_card(self):
        ''''Between cards fn'''
        #end if between 52 and 53
        if self.var.cardnum==53:
            #set card in play
            self.var.cardinplay=1
            self.game()
            return
        #stock limit, debt, random card detection
        found=self.deck[65].detectsl(self.gui,self.var,self.pset)
        if found==0:
            found2=self.deck[64].detectd(self.gui,self.var,self.pset)
            if found2==0:
                #test see any player in game
                if (self.pset[0].ingame==0 and self.pset[1].ingame==0 and self.pset[2].ingame==0 and self.pset[3].ingame==0 and self.pset[4].ingame==0):
                    self.gui.enable(self.gui.btnadvance,0)
                    tx='Game Over!\nAll players are out the game.'
                    self.deck[0].settx(self.gui,tx)
                    return
                #random card test
                else:
                    #only if random cards in play
                    if self.var.randoption!=0:
                        #get random card
                        x=self.getrandcard()
                        #print(x)
                        #test if random card in range
                        if ((self.var.cardnum-1 < x) and (self.var.cardnum > x)):
                            self.findrandcard(x)
                            #run random card
                            self.deck[self.var.cardnum].run(self.gui,self.var,self.pset,self.deck,self.writefn)
        #set card in play
        self.var.cardinplay=1
        self.game()
            
    #main game fn
    def game(self):
        '''Main game fn'''
        #write data to file
        self.writedata(self.var,self.pset,self.deck)
        #test for if between or within a card
        if self.var.cardinplay==0:
            self.inter_card()
        elif self.var.cardinplay==1:
#            if self.var.cardnum==2:
#                self.var.cardnum=21
#                self.p2.money=-5000
#                self.p1.money=-2500
#            if self.var.cardnum==3:
#                self.p1.cows=80
#                self.p2.sows=25
#            if self.var.cardnum==21:
#                self.p2.bcalves=2
#                self.p1.bcalves=20
#                self.p2.hcalves=20
#                self.p1.lambs=50
#                self.p2.spigs=50
#            if self.var.cardnum==10:
#                self.p2.sows=0
#            if self.var.cardnum==23:
#                self.p2.horses=1
#                self.p1.cows=1
#            if self.var.cardnum==24:
#                self.p1.hcalves=10
#            if self.var.cardnum==26:
#                self.p2.bcalves=20
#            if self.var.cardnum==31:
#                self.p2.ewes=5
#                self.p1.hcalves=10
#                self.p2.bcalves=20
#                self.p1.lambs=30
#            if self.var.cardnum==42:
#                self.p1.spigs=100
#                self.p2.lambs=20
#            if self.var.cardnum==49:
#                self.p1.lambs=20
#                self.p1.hcalves=10
#                self.p2.spigs=50
#                self.p2.bcalves=10
            if self.var.cardnum>39 and self.var.cardnum<52:
                self.var.cardnum=52
                #self.p2.horses=1
                #self.p2.lambs=75
                #self.p1.cows=2
                #pass
#            if self.var.cardnum>30 and self.var.cardnum<32:
#                self.var.cardnum=52
            #run card
            self.deck[self.var.cardnum].run(self.gui,self.var,self.pset,self.deck,self.writefn)
        else:
            print('er game')
    
class Playertx(Guicommonfn):
    '''Player frame widgits'''
    count=0
    
    def gui(self,frame,colour):
        '''Player widgits'''
        self.frame=frame
        self.colour=colour
        #set default player name
        text=('Player ' + str(Playertx.count))
        #widgits
        self.txname=Entry(frame,text=text,bg=colour,font=('',12),width=8)
        self.txmtx=Label(frame,text='Money: £',bg=colour)
        self.txm=Label(frame,text=15000,bg=colour,width=5)
        self.txcowstx=Label(frame,text='Cows:',bg=colour)
        self.txcows=Label(frame,text=555,bg=colour,width=3)
        self.txewestx=Label(frame,text='Ewes:',bg=colour)
        self.txewes=Label(frame,text=555,bg=colour,width=3)
        self.txsowstx=Label(frame,text='Sows:',bg=colour)
        self.txsows=Label(frame,text=555,bg=colour,width=3)
        self.txhorsestx=Label(frame,text='Horses:',bg=colour)
        self.txhorses=Label(frame,text=555,bg=colour,width=3)
        self.txhctx=Label(frame,text='Heifer calves:',bg=colour)
        self.txhc=Label(frame,text=555,bg=colour,width=3)
        self.txbctx=Label(frame,text='Bull calves:',bg=colour)
        self.txbc=Label(frame,text=555,bg=colour,width=3)
        self.txlambstx=Label(frame,text='Lambs:',bg=colour)
        self.txlambs=Label(frame,text=555,bg=colour,width=3)
        self.txsptx=Label(frame,text='Store pigs:',bg=colour)
        self.txsp=Label(frame,text=555,bg=colour,width=3)
        self.txwheattx=Label(frame,text='Wheat:',bg=colour)
        self.txwheat=Label(frame,text=555,bg=colour,width=5)
        self.txbarleytx=Label(frame,text='Barley:',bg=colour)
        self.txbarley=Label(frame,text=555,bg=colour,width=5)
        self.txoatstx=Label(frame,text='Oats:',bg=colour)
        self.txoats=Label(frame,text=555,bg=colour,width=5)
        self.txpotatoestx=Label(frame,text='Potatoes:',bg=colour)
        self.txpotatoes=Label(frame,text=555,bg=colour,width=5)
        self.txrootstx=Label(frame,text='Roots:',bg=colour)
        self.txroots=Label(frame,text=555,bg=colour,width=5)
        self.txhaytx=Label(frame,text='Hay:',bg=colour)
        self.txhay=Label(frame,text=555,bg=colour,width=5)
        self.txpasturetx=Label(frame,text='Pasture:',bg=colour)
        self.txpasture=Label(frame,text=555,bg=colour,width=5)
        self.txleytx=Label(frame,text='Ley:',bg=colour)
        self.txley=Label(frame,text=555,bg=colour,width=5)
        self.txrisk=Label(frame,text='Risk',bg='white')
        self.c19=Label(frame,text='Card 19',bg='white')
        self.c19pound=Label(frame,text='£',bg=colour)
        self.txc19=Label(frame,text='2500',bg=colour)
        self.c29=Label(frame,text='Card 29',bg='white')
        self.c29pound=Label(frame,text='£',bg=colour)
        self.txc29=Label(frame,text='2500',bg=colour)
        self.c36=Label(frame,text='Card 36',bg='white')
        self.c36pound=Label(frame,text='£',bg=colour)
        self.txc36=Label(frame,text='2500',bg=colour)
        self.c39=Label(frame,text='Card 39',bg='white')
        self.c39pound=Label(frame,text='£',bg=colour)
        self.txc39=Label(frame,text='2500',bg=colour)
        #increase each isntance use
        Playertx.count+=1
        #run posisiton and default fns
        self.posplayer()
        self.defaults()
        #dictonary
        self.guidic={'cows':self.txcows,'ewes':self.txewes,'sows':self.txsows,'horses':self.txhorses,'bcalves':self.txbc,'hcalves':self.txhc,'lambs':self.txlambs,'spigs':self.txsp}
        
    def posplayer(self):
        ''''Posistion widgits'''
        self.txname.grid(row=1,column=1)
        self.txmtx.grid(row=1,column=3)
        self.txm.grid(row=1,column=4)
        self.txcowstx.grid(row=2,column=1)
        self.txcows.grid(row=2,column=2)
        self.txewestx.grid(row=3,column=1)
        self.txewes.grid(row=3,column=2)
        self.txsowstx.grid(row=4,column=1)
        self.txsows.grid(row=4,column=2)
        self.txhorsestx.grid(row=5,column=1)
        self.txhorses.grid(row=5,column=2)
        self.txhctx.grid(row=6,column=1)
        self.txhc.grid(row=6,column=2)
        self.txbctx.grid(row=7,column=1)
        self.txbc.grid(row=7,column=2)
        self.txlambstx.grid(row=8,column=1)
        self.txlambs.grid(row=8,column=2)
        self.txsptx.grid(row=9,column=1)
        self.txsp.grid(row=9,column=2)
        self.txwheattx.grid(row=2,column=3)
        self.txwheat.grid(row=2,column=4)
        self.txbarleytx.grid(row=3,column=3)
        self.txbarley.grid(row=3,column=4)
        self.txoatstx.grid(row=4,column=3)
        self.txoats.grid(row=4,column=4)
        self.txpotatoestx.grid(row=5,column=3)
        self.txpotatoes.grid(row=5,column=4)
        self.txrootstx.grid(row=6,column=3)
        self.txroots.grid(row=6,column=4)
        self.txhaytx.grid(row=7,column=3)
        self.txhay.grid(row=7,column=4)
        self.txpasturetx.grid(row=8,column=3)
        self.txpasture.grid(row=8,column=4)
        self.txleytx.grid(row=9,column=3)
        self.txley.grid(row=9,column=4)
        self.txrisk.grid(row=1,column=5,columnspan=2)
        self.c19.grid(row=2,column=5,columnspan=2)
        self.c19pound.grid(row=3,column=5,sticky=E)
        self.txc19.grid(row=3,column=6,sticky=W)
        self.c29.grid(row=4,column=5,columnspan=2)
        self.c29pound.grid(row=5,column=5,sticky=E)
        self.txc29.grid(row=5,column=6,sticky=W)
        self.c36.grid(row=6,column=5,columnspan=2)
        self.c36pound.grid(row=7,column=5,sticky=E)
        self.txc36.grid(row=7,column=6,sticky=W)
        self.c39.grid(row=8,column=5,columnspan=2)
        self.c39pound.grid(row=9,column=5,sticky=E)
        self.txc39.grid(row=9,column=6,sticky=W)
        
    def defaults(self):
        '''Defaults'''
        #inserts inital player names into entry
        tx='Player'+str(self.count)
        self.txname.insert(0,tx) 
        #makes sure entry is disabled
        self.txname.configure(state=DISABLED)
    
    #destructor method
    def __del__(self):
        print('p destroyed')
                
#graph class
class GraphPlayer:
    '''Graph class- players'''
    
    def setinit(self):
        #card and players money arrays
        self.pltcard=[1]
        self.pltm=[1500]
        #additional- stock graph arrays
        self.pltc=[60]
        self.plte=[50]
        self.plts=[16]
        self.plth=[2]
        self.pltbc=[0]
        self.plthc=[0]
        self.pltl=[0]
        self.pltsp=[0]
        #dice roll arrays
        self.pltcard2=[]
        self.pltr=[]
        self.dcount=[0,0,0,0,0,0]
        #at risk arrays
        self.pltcard19=[]
        self.pltcard29=[]
        self.pltcard36=[]
        self.pltcard39=[]
        self.pltmatrisk19=[]
        self.pltmatrisk29=[]
        self.pltmatrisk36=[]
        self.pltmatrisk39=[]
        self.pltmatrisk19mn=[]
        self.pltmatrisk29mn=[]
        self.pltmatrisk36mn=[]
        self.pltmatrisk39mn=[]
        self.pltmatrisk19mx=[]
        self.pltmatrisk29mx=[]
        self.pltmatrisk36mx=[]
        self.pltmatrisk39mx=[]
    
    def adddatagraph(self,card,money,stock):
        '''Add data to graph: card=card number, money=money, stock=array of stock- cows,ewes,sows,horses,bcalves,hcalves,lambs,spigs'''
        self.pltcard.append(card)
        self.pltm.append(money)
        self.pltc.append(stock[0])
        self.plte.append(stock[1])
        self.plts.append(stock[2])
        self.plth.append(stock[3])
        self.pltbc.append(stock[4])
        self.plthc.append(stock[5])
        self.pltl.append(stock[6])
        self.pltsp.append(stock[7])
        
    def adddatagraphdice(self,card,roll):
        self.pltcard2.append(card)
        self.pltr.append(roll)
        self.dcount[roll-1]+=1
        
    def adddatagrapghatrisk(self,card,money19,money29,money36,money39):
        if card<19:
            self.pltcard19.append(card)
            self.pltmatrisk19.append(money19[2])
            self.pltmatrisk19mn.append(money19[0])
            self.pltmatrisk19mx.append(money19[1])
        if card<29:
            self.pltcard29.append(card)
            self.pltmatrisk29.append(money29[2])
            self.pltmatrisk29mn.append(money29[0])
            self.pltmatrisk29mx.append(money29[1])
        if card<36:
            self.pltcard36.append(card)
            self.pltmatrisk36.append(money36[2])
            self.pltmatrisk36mn.append(money36[0])
            self.pltmatrisk36mx.append(money36[1])
        if card<39:
            self.pltcard39.append(card)
            self.pltmatrisk39.append(money39[2])
            self.pltmatrisk39mn.append(money39[0])
            self.pltmatrisk39mx.append(money39[1])
        #print('length',len(self.pltcard36),len(self.pltmatrisk36),len(self.pltcard39),len())
        
class GraphPlot:
    '''Graph class- plotting'''
    
    def plotmain(self,gui,var,pset):
        '''Plot main graph: gui=gui instance, var=global variable instance, pset=player set array'''
        #figure and figure size
        fig=plt.figure()
        fig.set_size_inches(55,25,forward=True)#was 60,40; 75,50
        #sub plots in the figure
        p1=plt.subplot(2,3,2) #rows,colums,posistion
        p2=plt.subplot(2,3,3)
        p3=plt.subplot(2,3,4)
        p4=plt.subplot(2,3,5)
        p5=plt.subplot(2,3,6)
        forall=plt.subplot(2,3,1)
        parray=[p1,p2,p3,p4,p5,forall]
        colarray=['r','b','g','c','m']
        #plot- card, money, marker, colour; 1st 2 players will always be plotted- other player only if in the game
        i=0
        while i<var.pnum:
            parray[i].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[5].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            i+=1
#        p1.plot(self.pltcard,self.pltm1,marker='.',color='r')
#        p2.plot(self.pltcard,self.pltm2,marker='.',color='b')
#        forall.plot(self.pltcard,self.pltm1,marker='.',color='r')
#        forall.plot(self.pltcard,self.pltm2,marker='.',color='b')
#        if vars0.pnum>=3:
#            p3.plot(self.pltcard,self.pltm3,marker='.',color='g')
#            forall.plot(self.pltcard,self.pltm3,marker='.',color='g')
#        if vars0.pnum>=4:
#            p4.plot(self.pltcard,self.pltm4,marker='.',color='c')
#            forall.plot(self.pltcard,self.pltm4,marker='.',color='c')
#        if vars0.pnum>=5:
#            p5.plot(self.pltcard,self.pltm5,marker='.',color='m')
#            forall.plot(self.pltcard,self.pltm5,marker='.',color='m')
        #set titles, labels, x range, x bins/ticks placement
        #add grid and save plot
        p1.set_title('Player 1')
        p1.set_xlabel('Card')
        p1.set_ylabel('Money')
        p1.set_xlim(1,54)
        p1.locator_params(axis='x',tight=True,nbins=60)
        p1.grid(True)
        p2.set_title('Player 2')
        p2.set_xlabel('Card')
        p2.set_ylabel('Money')
        p2.set_xlim(1,54)
        p2.locator_params(axis='x',tight=True,nbins=60)
        p2.grid(True)
        p3.set_title('Player 3')
        p3.set_xlabel('Card')
        p3.set_ylabel('Money')
        p3.set_xlim(1,54)
        p3.locator_params(axis='x',tight=True,nbins=60)
        p3.grid(True)
        p4.set_title('Player 4')
        p4.set_xlabel('Card')
        p4.set_ylabel('Money')
        p4.set_xlim(1,54)
        p4.locator_params(axis='x',tight=True,nbins=60)
        p4.grid(True)
        p5.set_title('Player 5')
        p5.set_xlabel('Card')
        p5.set_ylabel('Money')
        p5.set_xlim(1,54)
        p5.locator_params(axis='x',tight=True,nbins=60)
        p5.grid(True)
        forall.set_title('All Players')
        forall.set_xlabel('Card')
        forall.set_ylabel('Money')
        forall.set_xlim(1,54)
        forall.locator_params(axis='x',tight=True,nbins=60)
        forall.grid(True)
        plt.savefig('farmingplot19.png')
        
    def plotstock(self,gui,var,pset):
        '''Plot stock graph: gui=gui instance, var=global variable instance, pset=player set array'''
        fig2=plt.figure()
        fig2.set_size_inches(55,25,forward=True)#was 60,40; 75,50
        #sub plots in the figure
        pt1=plt.subplot(2,3,2) #rows,colums,posistion; ewes
        pt2=plt.subplot(2,3,3) #sows horses
        pt3=plt.subplot(2,3,4) #hc bc
        pt4=plt.subplot(2,3,5) #lambs
        pt5=plt.subplot(2,3,6) #sp
        pt6=plt.subplot(2,3,1) #cows
        #parray2=[pt1,pt2,pt3,pt4,pt5,pt6]
        colarray=['r','b','g','c','m']
        #plot- card, money, marker, colour; 1st 2 players will always be plotted- other player only if in the game
        i=0
        while i<var.pnum:
            pt6.plot(pset[i].pltcard,pset[i].pltc,marker='.',color=colarray[i])
            pt1.plot(pset[i].pltcard,pset[i].plte,marker='.',color=colarray[i])
            pt2.plot(pset[i].pltcard,pset[i].plts,marker='.',color=colarray[i])
            pt2.plot(pset[i].pltcard,pset[i].plth,marker='.',color=colarray[i])
            pt3.plot(pset[i].pltcard,pset[i].pltbc,marker='.',color=colarray[i])
            pt3.plot(pset[i].pltcard,pset[i].plthc,marker='.',color=colarray[i])
            pt4.plot(pset[i].pltcard,pset[i].pltl,marker='.',color=colarray[i])
            pt5.plot(pset[i].pltcard,pset[i].pltsp,marker='.',color=colarray[i])
            i+=1
#        pt6.plot(self.pltcard,self.pltc1,marker='.',color='r')
#        pt6.plot(self.pltcard,self.pltc2,marker='.',color='b')
#        pt1.plot(self.pltcard,self.plte1,marker='.',color='r')
#        pt1.plot(self.pltcard,self.plte2,marker='.',color='b')
#        pt2.plot(self.pltcard,self.plts1,marker='.',color='r')
#        pt2.plot(self.pltcard,self.plts2,marker='.',color='b')
#        pt2.plot(self.pltcard,self.plth1,marker='.',color='r')
#        pt2.plot(self.pltcard,self.plth2,marker='.',color='b')
#        pt3.plot(self.pltcard,self.pltbc1,marker='.',color='r')
#        pt3.plot(self.pltcard,self.pltbc2,marker='.',color='b')
#        pt3.plot(self.pltcard,self.plthc1,marker='.',color='r')
#        pt3.plot(self.pltcard,self.plthc2,marker='.',color='b')
#        pt4.plot(self.pltcard,self.pltl1,marker='.',color='r')
#        pt4.plot(self.pltcard,self.pltl2,marker='.',color='b')
#        pt5.plot(self.pltcard,self.pltsp1,marker='.',color='r')
#        pt5.plot(self.pltcard,self.pltsp2,marker='.',color='b')
#        if vars0.pnum>=3:
#            pt6.plot(self.pltcard,self.pltc3,marker='.',color='g')
#            pt1.plot(self.pltcard,self.plte3,marker='.',color='g')
#            pt2.plot(self.pltcard,self.plts3,marker='.',color='g')
#            pt2.plot(self.pltcard,self.plth3,marker='.',color='g')
#            pt3.plot(self.pltcard,self.pltbc3,marker='.',color='g')
#            pt3.plot(self.pltcard,self.plthc3,marker='.',color='g')
#            pt4.plot(self.pltcard,self.pltl3,marker='.',color='g')
#            pt5.plot(self.pltcard,self.pltsp3,marker='.',color='g')
#        if vars0.pnum>=4:
#            pt6.plot(self.pltcard,self.pltc4,marker='.',color='c')
#            pt1.plot(self.pltcard,self.plte4,marker='.',color='c')
#            pt2.plot(self.pltcard,self.plts4,marker='.',color='c')
#            pt2.plot(self.pltcard,self.plth4,marker='.',color='c')
#            pt3.plot(self.pltcard,self.pltbc4,marker='.',color='c')
#            pt3.plot(self.pltcard,self.plthc4,marker='.',color='c')
#            pt4.plot(self.pltcard,self.pltl4,marker='.',color='c')
#            pt5.plot(self.pltcard,self.pltsp4,marker='.',color='c')
#        if vars0.pnum>=5:
#            pt6.plot(self.pltcard,self.pltc5,marker='.',color='m')
#            pt1.plot(self.pltcard,self.plte5,marker='.',color='m')
#            pt2.plot(self.pltcard,self.plts5,marker='.',color='m')
#            pt2.plot(self.pltcard,self.plth5,marker='.',color='m')
#            pt3.plot(self.pltcard,self.pltbc5,marker='.',color='m')
#            pt3.plot(self.pltcard,self.plthc5,marker='.',color='m')
#            pt4.plot(self.pltcard,self.pltl5,marker='.',color='m')
#            pt5.plot(self.pltcard,self.pltsp5,marker='.',color='m')
        #set titles, labels, x range, x bins/ticks placement
            #add grid and save plot
        pt1.set_title('Ewes')
        pt1.set_xlabel('Card')
        pt1.set_ylabel('#')
        pt1.set_xlim(1,54)
        pt1.locator_params(axis='x',tight=True,nbins=60)
        pt1.grid(True)
        pt2.set_title('Sows Horses')
        pt2.set_xlabel('Card')
        pt2.set_ylabel('#')
        pt2.set_xlim(1,54)
        pt2.locator_params(axis='x',tight=True,nbins=60)
        pt2.grid(True)
        pt3.set_title('Bull and Heifer calves')
        pt3.set_xlabel('Card')
        pt3.set_ylabel('#')
        pt3.set_xlim(1,54)
        pt3.locator_params(axis='x',tight=True,nbins=60)
        pt3.grid(True)
        pt4.set_title('Lambs')
        pt4.set_xlabel('Card')
        pt4.set_ylabel('#')
        pt4.set_xlim(1,54)
        pt4.locator_params(axis='x',tight=True,nbins=60)
        pt4.grid(True)
        pt5.set_title('Store pigs')
        pt5.set_xlabel('Card')
        pt5.set_ylabel('#')
        pt5.set_xlim(1,54)
        pt5.locator_params(axis='x',tight=True,nbins=60)
        pt5.grid(True)
        pt6.set_title('Cows')
        pt6.set_xlabel('Card')
        pt6.set_ylabel('#')
        pt6.set_xlim(1,54)
        pt6.locator_params(axis='x',tight=True,nbins=60)
        pt6.grid(True)
        plt.savefig('farmingplot219.png')
        
    def plotdice(self,gui,var,pset):
        '''Plot dice graph: gui=gui instance, var=global variable instance, pset=player set array'''
        #figure and figure size
        fig3=plt.figure()
        fig3.set_size_inches(55,25,forward=True)#was 60,40; 75,50
        #sub plots in the figure
        d1=plt.subplot(2,3,2) #rows,colums,posistion
        d2=plt.subplot(2,3,3)
        d3=plt.subplot(2,3,4)
        d4=plt.subplot(2,3,5)
        d5=plt.subplot(2,3,6)
        forall=plt.subplot(2,3,1)
        parray=[d1,d2,d3,d4,d5,forall]
        colarray=['r','b','g','c','m']
        #plot- card, money, marker, colour; 1st 2 players will always be plotted- other player only if in the game
        i=0
        while i<var.pnum:
            parray[i].scatter(pset[i].pltcard2,pset[i].pltr,marker='x',color=colarray[i])
            parray[5].plot(pset[i].pltcard2,pset[i].pltr,marker='x',color=colarray[i])
            i+=1
        #set titles, labels, x range, x bins/ticks placement
        #add grid and save plot
        d1.set_title('Player 1')
        d1.set_xlabel('Card')
        d1.set_ylabel('Roll')
        d1.set_xlim(1,54)
        d1.locator_params(axis='x',tight=True,nbins=60)
        d1.grid(True)
        d2.set_title('Player 2')
        d2.set_xlabel('Card')
        d2.set_ylabel('Roll')
        d2.set_xlim(1,54)
        d2.locator_params(axis='x',tight=True,nbins=60)
        d2.grid(True)
        d3.set_title('Player 3')
        d3.set_xlabel('Card')
        d3.set_ylabel('Roll')
        d3.set_xlim(1,54)
        d3.locator_params(axis='x',tight=True,nbins=60)
        d3.grid(True)
        d4.set_title('Player 4')
        d4.set_xlabel('Card')
        d4.set_ylabel('Roll')
        d4.set_xlim(1,54)
        d4.locator_params(axis='x',tight=True,nbins=60)
        d4.grid(True)
        d5.set_title('Player 5')
        d5.set_xlabel('Card')
        d5.set_ylabel('Roll')
        d5.set_xlim(1,54)
        d5.locator_params(axis='x',tight=True,nbins=60)
        d5.grid(True)
        forall.set_title('All Players')
        forall.set_xlabel('Card')
        forall.set_ylabel('Roll')
        forall.set_xlim(1,54)
        forall.locator_params(axis='x',tight=True,nbins=60)
        forall.grid(True)
        plt.savefig('farmingplot19d.png')
        
    def plotdice2(self,gui,var,pset):
        '''Plot dice graph: gui=gui instance, var=global variable instance, pset=player set array'''
        #figure and figure size
        fig4=plt.figure()
        fig4.set_size_inches(55,25,forward=True)#was 60,40; 75,50
        #sub plots in the figure
        d1=plt.subplot(2,3,2) #rows,colums,posistion
        d2=plt.subplot(2,3,3)
        d3=plt.subplot(2,3,4)
        d4=plt.subplot(2,3,5)
        d5=plt.subplot(2,3,6)
        forall=plt.subplot(2,3,1)
        parray=[d1,d2,d3,d4,d5,forall]
        colarray=['r','b','g','c','m']
        dvalues=[1,2,3,4,5,6]
        bottoms=[0,0,0,0,0,0]
        #plot- card, money, marker, colour; 1st 2 players will always be plotted- other player only if in the game
        i=0
        while i<var.pnum:
            parray[i].bar(dvalues,pset[i].dcount,color=colarray[i])
            parray[5].bar(dvalues,pset[i].dcount,bottom=bottoms,color=colarray[i])
            j=0
            while j<6:
                bottoms[j]+=pset[i].dcount[j]
                j+=1
            i+=1
        #set titles, labels, x range, x bins/ticks placement
        #add grid and save plot
        d1.set_title('Player 1')
        d1.set_xlabel('Roll')
        d1.set_ylabel('Number')
        #d1.set_xlim(1,54)
        #d1.locator_params(axis='x',tight=True,nbins=60)
        d1.grid(True)
        d2.set_title('Player 2')
        d2.set_xlabel('Roll')
        d2.set_ylabel('Number')
        #d2.set_xlim(1,54)
        #d2.locator_params(axis='x',tight=True,nbins=60)
        d2.grid(True)
        d3.set_title('Player 3')
        d3.set_xlabel('Roll')
        d3.set_ylabel('Number')
        #d3.set_xlim(1,54)
        #d3.locator_params(axis='x',tight=True,nbins=60)
        d3.grid(True)
        d4.set_title('Player 4')
        d4.set_xlabel('Roll')
        d4.set_ylabel('Number')
        #d4.set_xlim(1,54)
        #d4.locator_params(axis='x',tight=True,nbins=60)
        d4.grid(True)
        d5.set_title('Player 5')
        d5.set_xlabel('Roll')
        d5.set_ylabel('Number')
        #d5.set_xlim(1,54)
        #d5.locator_params(axis='x',tight=True,nbins=60)
        d5.grid(True)
        forall.set_title('All Players')
        forall.set_xlabel('Roll')
        forall.set_ylabel('Number')
        #forall.set_xlim(1,54)
        #forall.locator_params(axis='x',tight=True,nbins=60)
        forall.grid(True)
        plt.savefig('farmingplot19d2.png')
        
    def plotatrisk(self,gui,var,pset):
        '''Plot main graph: gui=gui instance, var=global variable instance, pset=player set array'''
        #figure and figure size
        fig5=plt.figure()
        fig5.set_size_inches(55,25,forward=True)#was 60,40; 75,50
        #sub plots in the figure
        ar1=plt.subplot(2,3,2) #rows,colums,posistion
        ar2=plt.subplot(2,3,3)
        ar3=plt.subplot(2,3,4)
        ar4=plt.subplot(2,3,5)
        ar5=plt.subplot(2,3,6)
        forall=plt.subplot(2,3,1)
        parray=[ar1,ar2,ar3,ar4,ar5,forall]
        colarray=['r','b','g','c','m']
        #plot- card, money, marker, colour; 1st 2 players will always be plotted- other player only if in the game
        i=0
        while i<var.pnum:
            #average
            parray[i].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[i].plot(pset[i].pltcard19,pset[i].pltmatrisk19,marker='x',color=colarray[i])
            parray[i].plot(pset[i].pltcard29,pset[i].pltmatrisk29,marker='+',color=colarray[i])
            parray[i].plot(pset[i].pltcard36,pset[i].pltmatrisk36,marker='^',color=colarray[i])
            parray[i].plot(pset[i].pltcard39,pset[i].pltmatrisk39,marker='*',color=colarray[i])
            parray[5].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[5].plot(pset[i].pltcard19,pset[i].pltmatrisk19,marker='x',color=colarray[i])
            parray[5].plot(pset[i].pltcard29,pset[i].pltmatrisk29,marker='+',color=colarray[i])
            parray[5].plot(pset[i].pltcard36,pset[i].pltmatrisk36,marker='^',color=colarray[i])
            parray[5].plot(pset[i].pltcard39,pset[i].pltmatrisk39,marker='*',color=colarray[i])
            #min
            #parray[i].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[i].plot(pset[i].pltcard19,pset[i].pltmatrisk19mn,marker='x',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard29,pset[i].pltmatrisk29mn,marker='+',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard36,pset[i].pltmatrisk36mn,marker='^',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard39,pset[i].pltmatrisk39mn,marker='*',linestyle=':',color=colarray[i])
            #parray[5].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[5].plot(pset[i].pltcard19,pset[i].pltmatrisk19mn,marker='x',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard29,pset[i].pltmatrisk29mn,marker='+',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard36,pset[i].pltmatrisk36mn,marker='^',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard39,pset[i].pltmatrisk39mn,marker='*',linestyle=':',color=colarray[i])
            #max
            #parray[i].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[i].plot(pset[i].pltcard19,pset[i].pltmatrisk19mx,marker='x',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard29,pset[i].pltmatrisk29mx,marker='+',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard36,pset[i].pltmatrisk36mx,marker='^',linestyle=':',color=colarray[i])
            parray[i].plot(pset[i].pltcard39,pset[i].pltmatrisk39mx,marker='*',linestyle=':',color=colarray[i])
            #parray[5].plot(pset[i].pltcard,pset[i].pltm,marker='.',color=colarray[i])
            parray[5].plot(pset[i].pltcard19,pset[i].pltmatrisk19mx,marker='x',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard29,pset[i].pltmatrisk29mx,marker='+',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard36,pset[i].pltmatrisk36mx,marker='^',linestyle=':',color=colarray[i])
            parray[5].plot(pset[i].pltcard39,pset[i].pltmatrisk39mx,marker='*',linestyle=':',color=colarray[i])
            i+=1
        #set titles, labels, x range, x bins/ticks placement
        #add grid and save plot
        ar1.set_title('Player 1')
        ar1.set_xlabel('Card')
        ar1.set_ylabel('Money')
        ar1.set_xlim(1,54)
        ar1.locator_params(axis='x',tight=True,nbins=60)
        ar1.grid(True)
        ar2.set_title('Player 2')
        ar2.set_xlabel('Card')
        ar2.set_ylabel('Money')
        ar2.set_xlim(1,54)
        ar2.locator_params(axis='x',tight=True,nbins=60)
        ar2.grid(True)
        ar3.set_title('Player 3')
        ar3.set_xlabel('Card')
        ar3.set_ylabel('Money')
        ar3.set_xlim(1,54)
        ar3.locator_params(axis='x',tight=True,nbins=60)
        ar3.grid(True)
        ar4.set_title('Player 4')
        ar4.set_xlabel('Card')
        ar4.set_ylabel('Money')
        ar4.set_xlim(1,54)
        ar4.locator_params(axis='x',tight=True,nbins=60)
        ar4.grid(True)
        ar5.set_title('Player 5')
        ar5.set_xlabel('Card')
        ar5.set_ylabel('Money')
        ar5.set_xlim(1,54)
        ar5.locator_params(axis='x',tight=True,nbins=60)
        ar5.grid(True)
        forall.set_title('All Players')
        forall.set_xlabel('Card')
        forall.set_ylabel('Money')
        forall.set_xlim(1,54)
        forall.locator_params(axis='x',tight=True,nbins=60)
        forall.grid(True)
        plt.savefig('farmingplot19ar.png')

class Vars:
    '''Class of global variables'''
    pnum=2 #number of players
    cardnum=0 #current card number
    cardinplay=0 #card in play
    #randcardinplay=0 #rad card in play
    diceoption=0 #dice option
    randoption=0 #random card placement option
    atriskoption=0 #at risk option
    atrisklim=16 #at risk power limit
    atriskprgress=0 #at risk progress
    
class Players(Playertx,GraphPlayer):
    '''Player class'''
    #stock, crops, money and ingame values
    cows, ewes, sows, horses = 60, 50, 16, 2
    hcalves=bcalves=lambs=spigs=0
    wheat=barley=oats=potatoes=0
    roots, hay, pasture, ley = 1, 4, 5, 0
    money=1500
    ingame=1
    name='name'
    
#    #player and stock dictonairies
#    stockdic={'cows':cows,'ewes':ewes,'sows':sows,'horses':horses,'bcalves':bcalves,'hcalves':hcalves,'lambs':lambs,'spigs':spigs}
    
    def __init__(self,pid,frame,colour):
        '''Instance initialisation and passes player name: name=player name, pid=player id, frame, colour'''
        self.c19values=[0,0,0] #max,min,mean
        self.c29values=[0,0,0]
        self.c36values=[0,0,0]
        self.c39values=[0,0,0]
        self.pid=pid
        self.gui(frame,colour)
        self.setinit()
        
    def set0value(self,pnum):
        '''Set player value based on if in game at start'''
        #in game
        if self.pid<=pnum:
            self.txcows.configure(text=self.cows)
            self.txewes.configure(text=self.ewes)
            self.txsows.configure(text=self.sows)
            self.txhorses.configure(text=self.horses)
            self.txhc.configure(text=self.hcalves)
            self.txbc.configure(text=self.bcalves)
            self.txlambs.configure(text=self.lambs)
            self.txsp.configure(text=self.spigs)
            self.txwheat.configure(text=self.wheat)
            self.txbarley.configure(text=self.barley)
            self.txoats.configure(text=self.oats)
            self.txpotatoes.configure(text=self.potatoes)
            self.txroots.configure(text=self.roots)
            self.txhay.configure(text=self.hay)
            self.txpasture.configure(text=self.pasture)
            self.txley.configure(text=self.ley)
            self.txm.configure(text=self.money)
            self.ingame=1
        #out game
        else:
            self.txcows.configure(text=0)
            self.txewes.configure(text=0)
            self.txsows.configure(text=0)
            self.txhorses.configure(text=0)
            self.txhc.configure(text=0)
            self.txbc.configure(text=0)
            self.txlambs.configure(text=0)
            self.txsp.configure(text=0)
            self.txwheat.configure(text=0)
            self.txbarley.configure(text=0)
            self.txoats.configure(text=0)
            self.txpotatoes.configure(text=0)
            self.txroots.configure(text=0)
            self.txhay.configure(text=0)
            self.txcows.configure(text=0)
            self.txpasture.configure(text=0)
            self.txley.configure(text=0)
            self.txm.configure(text=0)
            self.ingame=0
            
    def setname(self):
        '''Set player name'''
        self.name=self.txname.get()
        
    def atriskgui(self,gui,var):
        '''Set gui at risk values- can't do in thread'''
        if var.cardnum<19:
            self.settxvalue(self.txc19,self.c19values[2])
            self.adddatagrapghatrisk(var.cardnum,self.c19values,self.c29values,self.c36values,self.c39values)
            if self.c19values[1]>0:
                self.txrisk.configure(bg='green')
                self.c19.configure(bg='green')
            elif self.c19values[0]<0:
                self.txrisk.configure(bg='red')
                self.c19.configure(bg='red')
            else:
                self.txrisk.configure(bg='yellow')
                self.c19.configure(bg='yellow')
        if var.cardnum<29:
            self.settxvalue(self.txc29,self.c29values[2])
            self.adddatagrapghatrisk(var.cardnum,self.c19values,self.c29values,self.c36values,self.c39values)
            if self.c29values[1]>0:
                self.txrisk.configure(bg='green')
                self.c29.configure(bg='green')
            elif self.c29values[0]<0:
                self.txrisk.configure(bg='red')
                self.c29.configure(bg='red')
            else:
                self.txrisk.configure(bg='yellow')
                self.c29.configure(bg='yellow')
#            self.txrisk.configure(bg='white')
#            self.c29.configure(bg='white')
        if var.cardnum<36:
            self.settxvalue(self.txc36,self.c36values[2])
            self.adddatagrapghatrisk(var.cardnum,self.c19values,self.c29values,self.c36values,self.c39values)
            if self.c36values[1]>0:
                self.txrisk.configure(bg='green')
                self.c36.configure(bg='green')
            elif self.c36values[0]<0:
                self.txrisk.configure(bg='red')
                self.c36.configure(bg='red')
            else:
                self.txrisk.configure(bg='yellow')
                self.c36.configure(bg='yellow')
#            self.txrisk.configure(bg='white')
#            self.c36.configure(bg='white')
        if var.cardnum<39:
            self.settxvalue(self.txc39,self.c39values[2])
            self.adddatagrapghatrisk(var.cardnum,self.c19values,self.c29values,self.c36values,self.c39values)
            if self.c39values[1]>0:
                self.txrisk.configure(bg='green')
                self.c39.configure(bg='green')
            elif self.c39values[0]<0:
                self.txrisk.configure(bg='red')
                self.c39.configure(bg='red')
            else:
                self.txrisk.configure(bg='yellow')
                self.c39.configure(bg='yellow')
#            self.txrisk.configure(bg='white')
#            self.c39.configure(bg='white')
        
    def atrisk(self,gui,var,th):
        '''At risk fn for c19, 29 and 39- run in thread'''
        #in game test
        if self.ingame==0:
            return
        
        m=[self.money]
        c=[self.cows]
        e=[self.ewes]
        s=[self.sows]
        h=[self.horses]
        bc=[self.bcalves]
        hc=[self.hcalves]
        l=[self.lambs]
        sp=[self.spigs]
        wh=[self.wheat]
        array=[m,c,e,s,h,bc,hc,l,sp,wh]
        i=var.cardnum-1 #-1 due to chaning cardnum before running
        ii=var.atrisklim
        j=6 #index total
        k=1 #power
        print(self.name,var.cardnum,array)
        print(k,ii)
        
        if i<0:
            #print(array
            print(0,len(m))
            var.atriskprgress+=1
        
        if i<1:
            #print(array
            print(1,len(m))
            var.atriskprgress+=1
        
        if i<2:
            #time up test
            if th.isSet():
                return
            #take money
            tot=100+150*self.potatoes+100*(1+self.potatoes)
            m[0]-=tot
            #print(array
            print(2,len(m))
            var.atriskprgress+=1
            
        if i<3:
            #time up test
            if th.isSet():
                return
            #no action
#            m[0]=m[0]
            #print(array
            print(3,len(m))
            var.atriskprgress+=1
            
        if i<4:
            #time up test
            if th.isSet():
                return
            #change arrays
            m1=[70,80,15,1,0,35]
            c1=[2,2,1,0,0,1]
            s1=[0,0,0,0,1,0]
            h1=[0,0,0,1,0,0]
            #run only if in limit
            if k<ii:
                #change all array sizes
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                #change values
                y=0
                while y<6:
                    if th.isSet():
                        return
                    m[y]+=m1[y]
                    c[y]-=c1[y]
                    s[y]-=s1[y]
                    h[y]-=h1[y]
                    y+=1
                k+=1
                j=6**k
            #if noy within lim- run average
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    c[z]-=c1[2]
                    #s[z]-=s1[2]
                    #h[z]-=h1[2]
                    z+=1
                
            #print(array
            print(4,len(m))
            var.atriskprgress+=1
            
        if i<5:
            #time up test
            if th.isSet():
                return
            #take money
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]-=125
                z+=1
            #print(array
            print(5,len(m))
            var.atriskprgress+=1
            
        if i<6:
            #time up test
            if th.isSet():
                return
            #change array and change sizes
            m1=[100,60,40,30,20,10]
            #run only if in limit
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                #change values
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]-=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            #if noy within lim- run average
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            #print(array
            print(6,len(m))
            var.atriskprgress+=1
            
        if i<7:
            if th.isSet():
                return
            m1=[110,70,65,10,1,0]
            c1=[3,2,2,1,0,0]
            s1=[0,0,0,0,0,1]
            h1=[0,0,0,0,1,0]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]+=m1[w]
                        c[v]-=c1[w]
                        s[v]-=s1[w]
                        h[v]-=h1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    c[z]-=c1[2]
                    #s[z]-=s1[2]
                    #h[z]-=h1[2]
                    z+=1
            #print(array
            print(7,len(m))
            var.atriskprgress+=1
            
        if i<8:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=6*c[z]-20*(1+self.wheat+self.barley+self.oats)
                m[z]+=tot
                z+=1
            #print(array
            print(8,len(m))
            var.atriskprgress+=1
            
        if i<9:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]-=125
                z+=1
            #print(array
            print(9,len(m))
            var.atriskprgress+=1
            
        if i<10:
            if th.isSet():
                return
            sp1=[4,5,6,6,7,8]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        sp[v]+=sp1[w]*s[v]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    sp[z]+=sp1[2]*s[z]
                    z+=1
            #print(array
            print(10,len(m))
            var.atriskprgress+=1
            
        if i<11:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]+=6*c[z]
                z+=1
            #print(array
            print(11,len(m))
            var.atriskprgress+=1
        
        if i<12:
            if th.isSet():
                return
            l1=[1.1,1.2,1.3,1.4,1.4,1.5]
            e1=[5,5,5,5,0,0]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        l[v]+=int(l1[w]*e[v])
                        e[v]-=e1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    l[z]+=int(l1[2]*e[z])
                    e[z]-=e1[2]
                    z+=1
            #print(array
            print(12,len(m))
            var.atriskprgress+=1
            
        if i<13:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=250-3*c[z]
                m[z]-=tot
                z+=1
            #print(array
            print(13,len(m))
            var.atriskprgress+=1
            
        if i<14:
            if th.isSet():
                return
            m1=[80,100,155,70,80,20]
            c1=[3,3,3,2,2,1]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        v=(6**(k-1))*w+y
                        if th.isSet():
                            return
                        m[v]+=m1[w]
                        c[v]-=c1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
               z=0
               while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    c[z]-=c1[2]
                    z+=1 
            #print(array
            print(14,len(m))
            var.atriskprgress+=1
            
        if i<15:
            if th.isSet():
                return
            m1=[80,70,60,50,40,30]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]-=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            #print(array)
            print(15,len(m))
            var.atriskprgress+=1
            
        if i<16:
            if th.isSet():
                return
#            y=0
#            while y<len(m):
#                m[y]=m[y]
#                y+=1
            #print(array)
            print(16,len(m))
            var.atriskprgress+=1
            
        if i<17:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=150+3*sp[z]+h[z]+s[z]+e[z]
                m[z]-=tot
                z+=1
            #print(array)
            print(17,len(m))
            var.atriskprgress+=1
            
        if i<18:
            if th.isSet():
                return
            hc1=[-1,-0.5,0,0,0.5,1]
            bc1=[4,3,0,0,1,2]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        calves=np.floor(c[z]/2)-bc1[w]
                        if w<3:
                            a=np.floor(calves/2+hc1[w])
                        else:
                            a=np.ceil(calves/2+hc1[w])
                        hc[v]+=int(a)
                        bc[v]+=int(calves-hc[v])
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    calves=np.floor(c[z]/2)-bc1[2]
                    a=np.floor(calves/2+hc1[2])
                    hc[z]+=int(a)
                    bc[z]+=int(calves-hc[z])
                    z+=1
            #print(array
            print(18,len(m))
            var.atriskprgress+=1
#            calves=np.floor(pset[player].cows/2)-tx[roll-1][2]
#                #heifer calves
#                if roll<4:
#                    hc=np.floor(calves/2-tx[roll-1][0])
#                else:
#                    hc=np.ceil(calves/2+tx[roll-1][0])
#                #bull calves
#                bc=calves-hc
            
        if i<19:
            if th.isSet():
                return
            m1=[80,70,60,50,40,30]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]-=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            #print(array)
            print(19,len(m))
            var.atriskprgress+=1
        
        if i<19:
            self.c19values[0]=max(m)
            self.c19values[1]=min(m)
            self.c19values[2]=int(np.floor(np.mean(m)))
            print('risk19')
                
        if i<20:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=6*c[z]+int(1.2*e[z])
                m[z]+=tot
                z+=1
            #print(array)
            print(20,len(m))
            var.atriskprgress+=1
            
        if i<21:
            if th.isSet():
                return
#            y=0
#            while y<len(m):
#                m[y]=m[y]
#                y+=1
            #print(array)
            print(21,len(m))
            var.atriskprgress+=1
            
        if i<22:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]-=175
                z+=1
            #print(array)
            print(22,len(m))
            var.atriskprgress+=1
            
        if i<23:
            if th.isSet():
                return
            m1=[140,90,110,65,1,-100]
            c1=[4,3,3,2,1,0]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        if w==5:
                            if h[z]<2:
                                m1[5]=-100
                            else:
                                m[5]=0
                        m[v]+=m1[w]
                        c[v]-=c1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    c[z]-=c1[2]
                    z+=1
            #print(array)
            print(23,len(m))
            var.atriskprgress+=1
            
        if i<24:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]+=4*c[z]-3*(hc[z]+bc[z])
                z+=1
            #print(array)
            print(24,len(m))
            var.atriskprgress+=1
            
        if i<25:
            if th.isSet():
                return
            m1=[200,125,90,75,60,40]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]-=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            #print(array)
            print(25,len(m))
            var.atriskprgress+=1
            
        if i<26:
            if th.isSet():
                return
            m1=[2,2,30,1,1,5]
            c1=[2,2,2,1,0,0]
            h1=[0,0,0,0,1,0]
            bc1=[0,0,0,0,0,1]
            hc1=[0,0,0,0,0,1]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        if w==5:
                            bc1[5]=bc[v]
                            hc1[5]=hc[v]
                            m1[5]=5*(bc1[5]+hc1[5])
                        m[v]+=m1[w]
                        c[v]-=c1[w]
                        h[v]-=h1[w]
                        bc[v]-=bc1[w]
                        hc[v]-=hc1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    c[z]-=c1[2]
                    z+=1
            #print(array)
            print(26,len(m))
            var.atriskprgress+=1
            
        if i<27:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=200+2*sp[z]+s[z]
                m[z]-=tot
                z+=1
            #print(array)
            print(27,len(m))
            var.atriskprgress+=1
            
        if i<28:
            if th.isSet():
                return
#            y=0
#            while y<len(m):
#                m[y]=m[y]
#                y+=1
            #print(array)
            print(28,len(m))
            var.atriskprgress+=1
            
        if i<29:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]+=3*c[z]-200
                z+=1
            #print(array)
            print(29,len(m))
            var.atriskprgress+=1
            
        if i<29:
            self.c29values[0]=max(m)
            self.c29values[1]=min(m)
            self.c29values[2]=int(np.floor(np.mean(m)))
            print('risk29')

        if i<30:
            if th.isSet():
                return
            m1=[100,90,75,60,-1,200]
            h1=[0,0,0,0,1,0]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        if w==5:
                            if h[z]<2:
                                m1[5]=100
                            else:
                                m[5]=0
                        m[v]-=m1[w]
                        h[v]-=h1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]+=4*c[z]
                z+=1
            #print(array)
            print(30,len(m))
            var.atriskprgress+=1
            
        if i<31:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                if e[z]<20:
                    e1=e[z]
                else:
                    e1=20
                m[z]+=3*e1+10*hc[z]+7*bc[z]
                e[z]-=e1
                hc[z]-=hc[z]
                bc[z]-=bc[z]
                z+=1
            #print(array)
            print(31,len(m))
            var.atriskprgress+=1
            
        if i<32:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=c[z]+h[z]+1/2*(e[z]+l[z])
                if tot>100:
                    m1=100
                elif tot>90:
                    m1=90
                else:
                    m1=0
                m[z]-=m1
                z+=1
            #print(array)
            print(32,len(m))
            var.atriskprgress+=1
            
        if i<33:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]-=200
                z+=1
            #print(array)
            print(33,len(m))
            var.atriskprgress+=1
            
        if i<34:
            if th.isSet():
                return
            m1=[-10,10,25,30,50,100]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]+=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]
                    z+=1
            #print(array)
            print(34,len(m))
            var.atriskprgress+=1
            
        if i<35:
            if th.isSet():
                return
            m1=[0,150,100,75,50,25]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        if w==5:
                            if (self.oats==0 and self.barley==0 and self.wheat!=0):
                                wh[v]-=1
                        m[v]-=m1[w]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]-=m1[2]
                    z+=1
            #print(array)
            print(35,len(m))
            var.atriskprgress+=1
            
        if i<36:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=5*c[z]-350-(3*sp[z]+s[z]+l[z])
                m[z]+=tot
                z+=1
            #print(array)
            print(36,len(m))
            var.atriskprgress+=1
            
        if i<36:
            self.c36values[0]=max(m)
            self.c36values[1]=min(m)
            self.c36values[2]=int(np.floor(np.mean(m)))
            print('risk36')
            
        if i<37:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                m[z]+=4*c[z]
                z+=1
            #print(array)
            print(37,len(m))
            var.atriskprgress+=1
            
        if i<38:
            if th.isSet():
                return
            m1=[190,190,200,200,210,220]
            if k<ii:
                for x in array:
                    z=0
                    while len(x)<j:
                        if th.isSet():
                            return
                        x.append(x[z])
                        z+=1
                y=0
                w=0
                while w<6:
                    y=0
                    while y<(6**(k-1)):
                        if th.isSet():
                            return
                        v=(6**(k-1))*w+y
                        m[v]+=m1[w]*wh[v]
                        y+=1
                    w+=1
                k+=1
                j=6**k
            else:
                z=0
                while z<len(m):
                    if th.isSet():
                        return
                    m[z]+=m1[2]*wh[z]
                    z+=1
            #print(array)
            print(38,len(m))
            var.atriskprgress+=1
            
        if i<39:
            if th.isSet():
                return
            z=0
            while z<len(m):
                if th.isSet():
                    return
                tot=50*self.potatoes+600
                m[z]-=tot
                z+=1
            #print(array)
            print(39,len(m))
            var.atriskprgress+=1
            
        if i<39:
            self.c39values[0]=max(m)
            self.c39values[1]=min(m)
            self.c39values[2]=int(np.floor(np.mean(m)))
            print('risk39')

            
        #m=[self.money]
        #c=[self.cows]
        #e=[self.ewes]
        #s=[self.sows]
        #h=[self.horses]
        #bc=[self.bcalves]
        #hc=[self.hcalves]
        #l=[self.lambs]
        #sp=[self.spigs]
        
        
#    def inGame(self):
#        '''Test to see if player in game'''
#        pass
        
    #destructor method
    def __del__(self):
        print('player destroyed')
        
#card fn classes
class Text:
    '''Base class for text methods'''
    def settx(self,gui,tx):
        '''Set output text: gui= graphics instance, tx=text to display'''
        gui.txoutput.configure(text=tx)
        
    def setpops(self,gui,pset):
        '''Append names to drop down menu: gui=gui, pset=plater instance array'''
        values=['None']
        i=0
        while i<5:
            if pset[i].ingame==1:
                values.append(pset[i].name)
            i+=1
        gui.pops.configure(value=values)

class Money:
    '''Base clase for money and stock transfers'''
        
    def takemoney(self,amount,player):
        '''Take money from player: amount, player'''
        player.money-=amount
        player.settxvalue(player.txm,player.money)
        
    def givemoney(self,amount,player):
        '''Give money from player: amount, player'''
        player.money+=amount
        player.settxvalue(player.txm,player.money)
    
    def transfermoney(self,amount,pfrom,pto):
        '''Give money from 1 player to another: amount, player from, player to'''
        self.takemoney(amount,pfrom)
        self.givemoney(amount,pto)
        
    def case(self,player,stock,num):
        '''Case fn for stock: player, stock, num=nummber- must enter as num or -num'''
        stock=stock.lower()
        if stock=='cows':
            player.cows+=num
            player.settxvalue(player.guidic[stock],player.cows)
        elif stock=='ewes':
            player.ewes+=num
            player.settxvalue(player.guidic[stock],player.ewes)
        elif stock=='sows':
            player.sows+=num
            player.settxvalue(player.guidic[stock],player.sows)
        elif stock=='horses':
            player.horses+=num
            player.settxvalue(player.guidic[stock],player.horses)
        elif stock=='hcalves':
            player.hcalves+=num
            player.settxvalue(player.guidic[stock],player.hcalves)
        elif stock=='bcalves':
            player.bcalves+=num
            player.settxvalue(player.guidic[stock],player.bcalves)
        elif stock=='lambs':
            player.lambs+=num
            player.settxvalue(player.guidic[stock],player.lambs)
        elif stock=='spigs':
            player.spigs+=num
            player.settxvalue(player.guidic[stock],player.spigs)
#        elif stock=='calves':
#            player.hcalves+=num
#            player.settxvalue(player.guidic[stock],player.hcalves)
#            self.takestock()
        else:
            print('case er')
        
    def takestock(self,num,value,stock,player):
        '''Take stock from a player: num=number of stock, value=money, stock (plural), player'''
        #change stock
        self.case(player,stock,-num)
        #give money
        self.givemoney(value,player)
        
    def givestock(self,num,value,stock,player):
        '''Give stock to a player: num=number of stock, value=money, stock (plural), player'''
        #change stock
        self.case(player,stock,num)
        #take money
        self.takemoney(value,player)
        
    def transferstock(self,num,value,stock,pfrom,pto):
        '''Give stock from 1 player to another: value=money, , player from, player to'''
        self.takestock(num,value,stock,pfrom)
        self.givestock(num,value,stock,pto)
        
    def zerostock(self,num,value,stock,player):
        '''Test for <0 stock: num=number want to take, value=money, stock=stock name eg 'cows', player=player instance; returns tx=text string'''
        tx=''
        #only apply if needed
        if (player.cows<0 or player.ewes<0 or player.sows<0 or player.horses<0):
            #find how many extra take
            if player.cows<0:
                a=abs(player.cows)
            elif player.ewes<0:
                a=abs(player.ewes)
            elif player.sows<0:
                a=abs(player.sows)
            elif player.horses<0:
                a=abs(player.horses)
            else:
                print('er 0stock')
            fract=float(value)/num
            fract=int(np.ceil(fract))
            self.givestock(a,fract*a,stock,player)
            #set text
            tx='\nPlayer '+player.name+' does not have the stock to comply with the action. Instead the action has been applied as far as possible. You recieve £'+str(fract*(num-a))+' for '+str(num-a)+' '+stock+' instead.'
        return tx
        
#add stop going below 0 stock
        
class PickCrops:
    '''Base class for picking crops'''
    txoptcrops=['Wheat','Barley','Oats','Potatoes','Ley']
    
    def pickcrops(self,gui):
        '''Pick player crops'''
        #enable options, set text and set limits
        gui.cbenable(5,1)
        gui.settxop(5,self.txoptcrops)
        gui.openable(5,1)
        gui.op1.setvalues(start=0,incup=1,incdown=1,minv=0,maxv=10)
        gui.op2.setvalues(start=0,incup=1,incdown=1,minv=0,maxv=10)
        gui.op3.setvalues(start=0,incup=1,incdown=1,minv=0,maxv=10)
        gui.op4.setvalues(start=0,incup=1,incdown=1,minv=0,maxv=10)
        gui.op5.setvalues(start=0,incup=1,incdown=1,minv=0,maxv=10)
        
    def getcrops(self,gui,player):
        '''Get crops fn'''
        #get options
        player.wheat=gui.op1.getvalue()
        player.barley=gui.op2.getvalue()
        player.oats=gui.op3.getvalue()
        player.potatoes=gui.op4.getvalue()
        player.ley=gui.op5.getvalue()
        player.ley=10-player.wheat-player.barley-player.oats-player.potatoes
        player.settxvalue(player.txwheat,player.wheat)
        player.settxvalue(player.txbarley,player.barley)
        player.settxvalue(player.txoats,player.oats)
        player.settxvalue(player.txpotatoes,player.potatoes)
        player.settxvalue(player.txley,player.ley)
        #disable options and reset
        gui.cbenable(5,0)
        gui.openable(5,0)
        gui.resetcb(gui.cb1)
        gui.resetcb(gui.cb2)
        gui.resetcb(gui.cb3)
        gui.resetcb(gui.cb4)
        gui.resetcb(gui.cb5)
        gui.op1.reset()
        gui.op2.reset()
        gui.op3.reset()
        gui.op4.reset()
        gui.op5.reset()
        
    def croplegal(self,gui,player):
        c=0
        tot=gui.op1.getvalue()+gui.op2.getvalue()+gui.op3.getvalue()+gui.op4.getvalue()+abs(gui.op5.getvalue())
        if tot>10:
            c=-1
        else:
            c=0
        return c
    
    def checkcrops(self,gui,click):
        if self.click==click:
            gui.mop.txvalue.after(200,self.checkcrops,gui,click)
            a=gui.op1.getvalue()+gui.op2.getvalue()+gui.op3.getvalue()+gui.op4.getvalue()+gui.op5.getvalue()
            gui.settxvalue(gui.mop.txvalue,a)
        elif self.click!=click:
            gui.settxvalue(gui.mop.txvalue,0)
            return
        else:
            gui.mop.txvalue.after(200,self.checkcrops,gui,click)
    
class PaySeeds(Money):
    ''''Base class to pay see costs'''
    def payseeds(self,player,w=0,b=0,o=0,p=0):
        '''Pay seeds functions for: wheat(w), barley(b), oats(o) and potatoes(p)'''
        cost=w*player.wheat+b*player.barley+o*player.oats+p*player.potatoes
        self.takemoney(cost,player)
        
class AuctionSell(Money,Text):
    '''Base class for selling auctions'''
    
    def setauctionsell(self,gui,tx,pset,stocknum,maxv,minv=0,inc=1,start=0):
        '''Set up auction fn: gui==graphics, tx=array stateing number, stock and money for auction; pset=player instance array, stocknum=array of direct call to stock value for each player eg p1.cows, maxv=max value for numerical up down, minv=min value, inc=incrementaion, start=starting value'''
        #enable and set options
        i=0
        while i<5:
            if pset[i].ingame==1:
                gui.enable(gui.cb[i],1)
                gui.op[i].enable(1)
                gui.settxvalue(gui.cb[i],pset[i].name)
                #sell more than have protection
                if stocknum[i]<maxv:
                    maxv2=stocknum[i]
                else:
                    maxv2=maxv
                gui.op[i].setvalues(minv=minv,maxv=maxv2,start=start,incup=inc,incdown=inc)
            i+=1
        #set text
        txtot='Does any player want to sell '+tx[0]+' '+tx[1]+' for '+tx[2]+'?\nEnter your values below.'
        self.settx(gui,txtot)
    
    def getauctionsell(self,gui,value,stock,pset,multi,tx):
        '''Get auction options: gui, value=money, stock=stock type eg 'cows', pset=player array, multi=yes/no sale (1) or multi-value sale (0), tx=array stateing number, stock and money for auction'''
        #get options
        ops=[gui.op1.getvalue(),gui.op2.getvalue(),gui.op3.getvalue(),gui.op4.getvalue(),gui.op5.getvalue()]
        #multi values
        if stock=='multi1':
            i=0
            print(ops)
            txtot=''
            while i<5:
                if pset[i].ingame==1:
                    if ops[i]==0:
                        value1=0
                        value2=0
                        value3=0
                    else:
                        value1=value
                        value2=10
                        value3=15
                    self.takestock(value2,value1,'ewes',pset[i])
                    self.takestock(value3,0,'lambs',pset[i])
                    gui.resetcb(gui.cb[i])
                    gui.op[i].reset()
                    txtot=txtot+'Player '+pset[i].name+' has sold '+str(value2)+' and '+str(value3)+' '+tx[1]+' for £'+str(value1)+'.\n'
                i+=1
        else:
            #change player values
            i=0
            txtot=''
            while i<5:
                if pset[i].ingame==1:
                    if multi==0:
                        value2=int(value*ops[i])
                    elif ops[i]!=0:
                        value2=value
                    else:
                        value2=0
                    self.takestock(ops[i],value2,stock,pset[i])
                    gui.resetcb(gui.cb[i])
                    gui.op[i].reset()
                    txtot=txtot+'Player '+pset[i].name+' has sold '+str(ops[i])+' '+tx[1]+' for £'+str(value2)+'.\n'
                i+=1
        #set text
        txtot=txtot+'Click the Advance button to continue.'
        self.settx(gui,txtot)
        #reset and diabled
        gui.cbenable(5,0)
        gui.openable(5,0)
        
    def auctionsellmulti(self,var,pset,stock1,stock2,num1,num2):
        '''Fn for multi stock sell: var=golbal variables isntance, pset=player instance array, stock1=1st stock name, stock2=2nd stock name, num1=number for sell of stock1, num2=number for sell of stock2'''
        if (stock1=='ewes' and stock2=='lambs'):
            ret=[0,0,0,0,0]
            i=0
            while i<var.pnum:
                if (pset[i].ewes>=num1 and pset[i].lambs>=num2):
                    ret[i]=35
                else:
                    ret[i]=0
                i+=1
            return ret
    
class AuctionBuy(Money,Text):
    '''Base class for buying auctions'''
    def setauctionbuy(self,gui,tx,pset):
        '''Set up auction fn: gui==graphics, tx=array stateing number, stock and money for auction; pset=player instance array'''
        #enable
        gui.enable(gui.pops,1)
        gui.mop.enable(1)
        #set numeric up down limits
        gui.mop.setvalues(start=tx[2],incup=5,incdown=1,maxv=1500,minv=tx[2])
        #set combobox
        self.setpops(gui,pset)
        #set text
        txtot='Players may now bid to buy '+str(tx[0])+' '+tx[1]+' with reserve £'+str(tx[2])+'.\nEnter the name of the winning player and their bid into the player buying menu and value to the side. If no players want to bid select \'None\'.'
        self.settx(gui,txtot)
        
    def getauctionbuy(self,gui,stock,pset,tx):
        '''Get auction options: gui, stock=stock type eg 'cows', pset=player array, tx=array stateing number, stock and money for auction'''
        #get player and amount
        player=gui.getvalue(gui.pops)
        value=gui.mop.getvalue()
        if player=='None':
            txtot='No player brought the lot; click the Advance button to continue.'
        else:
            i=0
            while i<5:
                if pset[i].name==player:
                    break
                i+=1
            #add 's' if needed or short name
            if stock[-1]!='s':
                stock+='s'
            elif stock=='bull calves':
                stock='bcalves'
            elif stock=='heifer calves':
                stock='hcalves'
            elif stock=='store pigs':
                stock='spigs'
            self.givestock(tx[0],value,stock,pset[i])
            txtot='Player '+player+' has bought '+str(tx[0])+' '+tx[1]+' for £'+str(value)+'.\nClick the Advance button to continue.'
        #set text
        self.settx(gui,txtot)
        #reset and diabled
        gui.pops.set('None')
        gui.mop.reset()
        gui.enable(gui.pops,0)
        gui.mop.enable(0)
    
class Auction(Money,Text):
    '''Base class for buy and sell auctions'''
    #maybe redundant
    
class Bills(Money):
    '''Base class for bill payments'''
    def paybills(self,player,amount):
        self.takemoney(amount,player)
        
class Milk(Money):
    '''Base class for milk payments'''
    def milk(self,player,amount,cows,amount2=0,bc=0,hc=0):
        '''milk payment: amount=amount/cow, cows=number of cows, bc=number of bull calves where needed, hc= number of heifer calves where needed'''
        tot=amount*cows-amount2*(bc+hc)
        self.givemoney(tot,player)
        
class CornBills(Money):
    '''Base class for corn bill payments'''
    def cornbills(self,player,l=0,sp=0,e=0,s=0,h=0):
        tot=l*player.lambs+sp*player.spigs+e*player.ewes+s*player.sows+h*player.horses
        self.takemoney(tot,player)
        
class Wool(Money):
    '''Base class for wool payment'''
    def paywool(self,player,ewes):
        '''Wool payment: player=player isntance, ewes=number of ewes'''
        tot=int(1.2*ewes)
        self.givemoney(tot,player)
        
class Sale(Money):
    '''Base class for compulsoary sells'''
    
    def compsale(self,num,value,stock,player,multi):
        ''''Sell stock: num=number, value=amount total/per stock, stock=stock, player=player, multi=yes/no sale (1) or multi-value sale (0)'''
        if multi==0:
            value*=num
        self.takestock(num,value,stock,player)
    
class Drought(Money):
    '''Base class for drought/'''
    
    def drought(self,cows,horses,ewes,lambs,player):
        '''Works out drought payment: cows=number of cows etc, player=player instance'''
        self.cost=[0,50,100]
        self.limit=[90,100]
        self.txops=[' acres and pays £0.\n',
           ' acres and pays £50 to rent a 10 acre autumn ley.\n',
           ' acres and pays £100 to rent a 20 acre autumn ley.\n']
        total=cows+horses+1/2*(ewes+lambs)
        if total>self.limit[1]:
            n=2
        elif total>self.limit[0]:
            n=1
        else:
            n=0
        self.takemoney(self.cost[n],player)
        tx=self.txops[n]
        return total, tx
    
    def hay(self,cows,horses,ewes,lambs,player):
        '''Works out drought payment: cows=number of cows etc, player=player instance'''
        self.cost2=[0,12]
        self.limit2=76
        self.txops2=[' tonnes and pays £0.\n',
           ' tonnes and pays £12/tonne for extra hay.\n']
        total=cows+horses+1/4*(ewes+lambs)
        if total>self.limit2:
            n=1
        else:
            n=0
        self.takemoney(int(self.cost2[n]*(total-76)),player)
        tx=self.txops2[n]
        return total, tx
    
class StockEqu(Money,Text):
    ''''Base class for stock equalisation'''
    stock=[60,50,16,2]
    
    def postivestock(self,gui,cows,ewes,sows,horses,player):
        '''Correct for +ve stock'''
        money=[50,5,20,40]
        c=cows-self.stock[0]
        e=ewes-self.stock[1]
        s=sows-self.stock[2]
        h=horses-self.stock[3]
        total=0
        tx='Player '+player.name+' has received: £'
        if c>0:
            total+=c*money[0]
            tx+=str(c*money[0])+' for cows, £'
        else:
            tx+='0 for cows, £'
        if e>0:
            total+=e*money[1]
            tx+=str(e*money[1])+' for ewes, £'
        else:
            tx+='0 for ewes, £'
        if s>0:
            total+=s*money[2]
            tx+=str(s*money[2])+' for sows and £'
        else:
            tx+='0 for sows and £'
        if h>0:
            total+=h*money[3]
            tx+=str(h*money[3])+' for horses.'
        else:
            tx+='0 for horses.'
        self.givemoney(total,player)
        self.settx(gui,tx)
        self.blackout(player)
    
    def negativestock(self,gui,cows,ewes,sows,horses,player):
        '''Correct for -ve stock'''
        money=[60,6,30,50]
        c=self.stock[0]-cows
        e=self.stock[1]-ewes
        s=self.stock[2]-sows
        h=self.stock[3]-horses
        total=0
        tx='Player '+player.name+' has paid: £'
        if c>0:
            total+=c*money[0]
            tx+=str(c*money[0])+' for cows, £'
        else:
            tx+='0 for cows, £'
        if e>0:
            total+=e*money[1]
            tx+=str(e*money[1])+' for ewes, £'
        else:
            tx+='0 for ewes, £'
        if s>0:
            total+=s*money[2]
            tx+=str(s*money[2])+' for sows and £'
        else:
            tx+='0 for sows and £'
        if h>0:
            total+=h*money[3]
            tx+=str(h*money[3])+' for horses.'
        else:
            tx+='0 for horses.'
        self.takemoney(total,player)
        self.settx(gui,tx)
        self.blackout(player)
    
    def profit(self,player):
        '''Take £1500 from player to give profit'''
        self.takemoney(1500,player)
        self.blackout(player)
    
    def blackout(self,player):
        '''Hide gui player money value'''
        player.settxvalue(player.txm,'????')
        
class Winner(Money):
    '''Base class for working out the winner of the game'''
    
    def sortvalues(self,money):
        '''Sorts the money order: money=array on players money values'''
        money.sort()
        #money.reverse()
        return money
    
    def findplayername(self,array,arraybase,arrayname):
        '''Find player name of value given: array=money array, arraybase=unsorted array, arrayname=name array'''
        a=array[0]
        b=arraybase.index(a)
        c=arrayname[b]
        array.remove(a)
        arraybase.remove(a)
        arrayname.remove(c)
        return c
    
class Dice(Money,Text):
    '''Base class for dice- hazard cards'''
    inclickd=0
    
    def setdice(self,gui,var,player):
        '''Set up dice: gui=gui, var=global variables, player=player instance that's rolling'''
        #set text
        tx='Player '+player.name+' please roll the dice.'
        self.settx(gui,tx)
        #enable- depends on option chossen
        if var.diceoption==0:
            gui.enable(gui.btndselect,1)
            gui.enable(gui.dice,1)
        elif var.diceoption==1:
            gui.enable(gui.btndice,1)
        else:
            print('dice er')
        #disable other
        gui.enable(gui.btnadvance,0)
            
    def diceresult(self,roll,gui,var,dtype,txdice,txv,pset,player,file):
        '''Apply dice result: roll= dice roll value, gui=gui,var=global variables, dtype=dice type (stock, money, crops or births), txdice=array of text of dice options, txv=array stateing number, stock and money for dice, pset=player instance array, player=pset index to use'''
        #print(txv)
        #wrtie file
        file(pset[player],roll)
        #add data to graph
        pset[player].adddatagraphdice(var.cardnum,roll)
        #multi test
        multi=0
        op=txv[roll-1][1]
        if op[-1]=='m':
            multi=1
            txv[roll-1][1]=op[:-1]
        else:
            multi=0
        #set text
        txtot='Player '+pset[player].name+': '+txdice[roll-1]
        #type of roll
        if dtype=='stock':
            #print(txv[roll-1][1])
            #if horse conditional
            if txv[roll-1][1]=='moneyhorse':
                txv[roll-1][1]='horses'
                #print(pset[player].horses)
                if pset[player].horses>=2:
                    txv[roll-1][2]=0
                    txtot+='\nYou have '+str(pset[player].horses)+' horses.'
                else:
                    txtot+='\nYou have '+str(pset[player].horses)+' horses.'
            elif txv[roll-1][1]=='calves':
                txv[roll-1][1]='hcalves'
                txv[roll-1][2]*=(txv[roll-1][0]+pset[player].bcalves)
                txtot+='\nYou have '+str(txv[roll-1][0]+pset[player].bcalves)+' calves.'
                self.takestock(pset[player].bcalves,0,'bcalves',pset[player])
                
        #else:
            #money test
            if txv[roll-1][1]=='money':
                self.takemoney(txv[roll-1][2]*txv[roll-1][0],pset[player])
            else:
                #take stock
                self.takestock(txv[roll-1][0],txv[roll-1][2],txv[roll-1][1],pset[player])
            #check for 0 stock and add text if needed
            #set text
            txtot=txtot+self.zerostock(txv[roll-1][0],txv[roll-1][2],txv[roll-1][1],pset[player])
        elif dtype=='money' or dtype=='dhcmoney':
            #take money
            self.takemoney(txv[roll-1][2]*txv[roll-1][0],pset[player])
        #crops/give money
        elif dtype=='crops':
            #crop type
            if txv[roll-1][1]=='money':
                tot=txv[roll-1][0]*txv[roll-1][2]
            elif (txv[roll-1][1]=='wheat' or txv[roll-1][1]=='barley' or txv[roll-1][1]=='oats' or txv[roll-1][1]=='potatoes'):
                tot=txv[roll-1][0]*txv[roll-1][2]
#            elif txv[roll-1][1]=='barley':
#                pass
#            elif txv[roll-1][1]=='oats':
#                pass
#            elif txv[roll-1][1]=='potatoes':
#                pass
            else:
                print('er dice crops')
            self.givemoney(tot,pset[player])
        #births
        elif dtype=='births':
            #differet between cows and other
            if (txv[roll-1][1]=='spigs' or txv[roll-1][1]=='lambs'):
                #get parents
                if txv[roll-1][1]=='spigs':
                    parent=pset[player].sows-txv[roll-1][2]
                    txparent='sows'
                elif txv[roll-1][1]=='lambs':
                    parent=pset[player].ewes
                    txparent='ewes'
    #            elif (txv[roll-1][1]=='bcalves' or txv[roll-1][1]=='hcalves'):
    #                parent=pset[player].cows
    #                txparent='cows'
                else:
                    print('er dice result')
                #give stock
                tot=int(parent*txv[roll-1][0])
                self.givestock(tot,0,txv[roll-1][1],pset[player])
                #take stock
                self.takestock(txv[roll-1][2],0,txparent,pset[player])
            #cows
            else:
                #calves
                calves=np.floor(pset[player].cows/2)-txv[roll-1][2]
                #heifer calves
                if roll<4:
                    hc=np.floor(calves/2-txv[roll-1][0])
                else:
                    hc=np.ceil(calves/2+txv[roll-1][0])
                #bull calves
                bc=calves-hc
                #give stock
                self.givestock(int(hc),0,'hcalves',pset[player])
                self.givestock(int(bc),0,'bcalves',pset[player])
        elif dtype=='dhccrops':
            w=[0,0,0,1,1,0]
            b=[0,1,0,0,0,1]
            o=[0,0,1,0,0,1]
            p=[1,0,0,0,1,0]
            pset[player].wheat+=w[roll-1]
            pset[player].barley+=b[roll-1]
            pset[player].oats+=o[roll-1]
            pset[player].potatoes+=p[roll-1]
            pset[player].settxvalue(pset[player].txwheat,pset[player].wheat)
            pset[player].settxvalue(pset[player].txbarley,pset[player].barley)
            pset[player].settxvalue(pset[player].txoats,pset[player].oats)
            pset[player].settxvalue(pset[player].txpotatoes,pset[player].potatoes)
            self.takemoney(txv[roll-1][2],pset[player])
        elif dtype=='dhc':
            if self.dswitch==0:
                self.drolldhc=roll
            else:
                self.drolldhc2=roll
                #txtot=''
                return
            self.click=7-1+player
        else:
            print('er dtype')
        #set text
        txtot=txtot+'\nClick the Advance button to continue.'
        self.settx(gui,txtot)
        #multi set
        if multi==1:
            self.click=7-1+player #-1 to correct
        
    def rollchoice(self,gui,var,txdice,txv,pset,player,file):
        '''Option choice fn: gui=gui, var=global variable instance, txdice=array of text of dice options, txv=array stateing number, stock and money for dice, pset=player instance array, player=pset index to use'''
        txc=['Wheat','Barley','Oats']
        txname=pset[player].name
        #wrtie file- move
        file('Roll choice '+str(self.inclickd))
        #multi roll- crop loss
        if txv[0][1]=='crop':
            #set up options
            if self.inclickd==0:
                #no crops
                if ((pset[player].wheat+pset[player].barley+pset[player].oats)==0):
                    #set text
                    a=txname+txdice[1]
                    self.settx(gui,a)
                    #correct click of card
                    self.click-=6
                else:
                    #change click values
                    self.click-=1
                    self.inclickd+=1
                    #enable options and set option text
                    if pset[player].wheat!=0:
                        gui.enable(gui.cb[0],1)
                    if pset[player].barley!=0:
                        gui.enable(gui.cb[1],1)
                    if pset[player].oats!=0:
                        gui.enable(gui.cb[2],1)
                    gui.settxop(3,txc)
                    #set text
                    self.settx(gui,txdice[0])
                    #multi selection test
                    gui.enable(gui.btnadvance,0)
                    gui.cb[0].after(200,self.checkcb,gui)
            elif self.inclickd==1:
                #get option
                a=[gui.getvalue(gui.opv1),gui.getvalue(gui.opv2),gui.getvalue(gui.opv3)]
                #apply result
                pset[player].wheat-=a[0]
                pset[player].barley-=a[1]
                pset[player].oats-=a[2]
                pset[player].settxvalue(pset[player].txwheat,pset[player].wheat)
                pset[player].settxvalue(pset[player].txbarley,pset[player].barley)
                pset[player].settxvalue(pset[player].txoats,pset[player].oats)
                #set text
                self.settx(gui,txname+txdice[a.index(1)+2])
                #disable and reset options
                gui.cbenable(3,0)
                gui.resetcb(gui.cb1)
                gui.resetcb(gui.cb2)
                gui.resetcb(gui.cb3)
                #change click values- reset
                self.click-=6
                self.inclickd=0
#        else:
#            #set up dice and take to dice roll
#            self.setdice(gui,var,pset[self.click-1])
                
    def checkcb(self,gui):
        #w=gui.getvalue(gui.opv1)
        #b=gui.getvalue(gui.opv2)
        #o=gui.getvalue(gui.opv3)
        if (self.inclickd==1 and (gui.getvalue(gui.opv1)+gui.getvalue(gui.opv2)+gui.getvalue(gui.opv3)==1)):
            gui.enable(gui.btnadvance,1)
            gui.cb[0].after(200,self.checkcb,gui)
        elif self.inclickd!=1:
            return
        else:
            gui.enable(gui.btnadvance,0)
            gui.cb[0].after(200,self.checkcb,gui)

class Cards(Money,Text):#? money
    '''Base class for cards'''
    click=0 #click for card
    
    def settxinit(self,gui,var,col):
        '''Set inital card text: gui=graphics instance, var=global variables instance'''
        #title
        gui.txtitle.configure(text=self.title)
        #card number
        gui.txcard.configure(text=self.cardnum)
        #main text
        gui.txmain.configure(text=self.txmain)
        #instruction/output text
        gui.txoutput.configure(text=self.txoutput[0])
        #set text colour
        gui.txtitle.configure(fg=self.cardfontcol)
        gui.txcard.configure(fg=self.cardfontcol)
        gui.txf.configure(fg=self.cardfontcol)
        gui.txmain.configure(fg=self.cardfontcol)
        gui.txoutput.configure(fg=self.cardfontcol)
        
    def settxout(self,gui,a):
        '''Set output text: gui= graphics instance, a=click value or posistion in array'''
        gui.txoutput.configure(text=self.txoutput[a])
        
    def settxoutwithtx(self,gui,a,tx,sep):
        '''Set output text with preciding text: gui and \'a\' like above, tx=preciding text, sep=seperator like n, t etc'''
        txtot=tx+sep+self.txoutput[a]
        gui.txoutput.configure(text=txtot)
        
    def settxoutwithtx2(self,gui,a,tx,sep):
        '''Set output text with post text: gui and \'a\' like above, tx=preciding text, sep=seperator like n, t etc'''
        txtot=self.txoutput[a]+sep+tx
        gui.txoutput.configure(text=txtot)
        
    def settxoutwithtx3(self,gui,a,tx,sep,tx2,sep2):
        '''Set output text with both text: gui and \'a\' like above, tx=preciding text, sep=seperator like n, t etc, tx2=post text, sep2=seperator'''
        txtot=tx+sep+self.txoutput[a]+sep2+tx2
        gui.txoutput.configure(text=txtot)
        
    def settxoutwithtx4(self,gui,a,tx,sep,sep2,b):
        '''Set output text with both text: gui and \'a\' like above, tx=central text, sep=pre-seperator like n, t etc, tx2=post text, sep2=post-seperator, b=ending text'''
        txtot=self.txoutput[a]+sep+tx+sep2+self.txoutput[b]
        gui.txoutput.configure(text=txtot)
    
class ARops:
    '''Base class for at risk options'''
    
    def opsetar(self,gui):
        '''Enable and set options'''
        self.txoptions=['Yes','No','Max value']
        #enable options
        gui.cbenable(3,1)
        gui.op3.enable(1)
        #set options text
        gui.settxop(3,self.txoptions)
        #set button values
        gui.op3.setvalues(start=8,incup=1,incdown=1,maxv=16,minv=1)
            
    def opgetar(self,gui,var):
        '''Get selected options'''
        #disable options
        gui.cbenable(3,0)
        gui.op3.enable(0)
        #get options
        yes=gui.getvalue(gui.opv1)
        no=gui.getvalue(gui.opv2)
        maxv=gui.op3.getvalue()
        #yes
        if (yes==1 and no==0):
            #change value
            var.atriskoption=1
            var.atrisklim=maxv
            #reset option
            gui.resetcb(gui.cb1)
            gui.resetcb(gui.cb3)
            gui.op3.reset()
            #return text
            return 'Players have selected to allow the at risk function.'
        #no, none or both
        elif (no==1 or (no==1 and yes==1) or (no==0 and yes==0)):
            var.atriskoption=0
            gui.resetcb(gui.cb1)
            gui.resetcb(gui.cb2)
            gui.resetcb(gui.cb3)
            gui.op3.reset()
            return 'Players have selected to not allow the use of the at risk function.'
        else:
            print('er at risk option')
    
class Dops:
    '''Base class for dice options'''
    
    def opsetd(self,gui):
        '''Enable and set options'''
        self.txoptions=['Yes','No']
        #enable options
        gui.cbenable(2,1)
        #set options text
        gui.settxop(2,self.txoptions)
            
    def opgetd(self,gui,var):
        '''Get selected options'''
        #disable options
        gui.cbenable(2,0)
        #get options
        yes=gui.getvalue(gui.opv1)
        no=gui.getvalue(gui.opv2)
        #yes
        if (yes==1 and no==0):
            #change value
            var.diceoption=1
            #reset option
            gui.resetcb(gui.cb1)
            #return text
            return 'Players have selected to use the computer dice.'
        #no, none or both
        elif (no==1 or (no==1 and yes==1) or (no==0 and yes==0)):
            var.diceoptions=0
            gui.resetcb(gui.cb1)
            gui.resetcb(gui.cb2)
            return 'Players have selected to use their own dice.'
        else:
            print('er dice option')
            
class Stocklimit(Cards):
    '''Class for stock limits'''
    cardnum=65
    pcardnum=0
    #stock limits
    limcows=75
    limewes=60
    limsows=20
    limhorses=4
    #players=[0,0,0,0,0]
    
    def detectsl(self,gui,var,pset):
        '''Detect stock limit fn'''
        detect=0
        tx=''
        i=0
        #loop to detect violations
        while i<var.pnum:
            if (pset[i].cows>self.limcows or pset[i].ewes>self.limewes or pset[i].sows>self.limsows or pset[i].horses>self.limhorses):
                #add text
                tx=tx+'Player '+pset[i].name+' has broken the stock limit.\n'
                #change detection
                detect+=1
                #self.players[i]=1
            i+=1
        #if detected
        if detect>0:
            #set text
            tx=tx+'Click the Advance button to continue.'
            self.settx(gui,tx)
            #store last card num
            self.pcardnum=var.cardnum
            #set game to this cardnum
            var.cardnum=self.cardnum
        #return dectection value
        return detect
            
    #stock limit adjustment
    def run(self,gui,var,pset,deck,file):
        '''Run card65 fn'''
        if self.click==1:
            #inital text
            tx='The following stock limit violations and changes have been made:\n'
            #find violations and correct
            i=0
            while i<var.pnum:
                player=pset[i]
                if player.cows>self.limcows:
                    exc=player.cows-self.limcows
                    money=25*exc
                    tx=tx+'Player '+player.name+' had '+str(player.cows)+' cows ('+str(exc)+' extra). The extra stock has been taken and you recieve £'+str(money)+' for that stock (£25/cow).\n'
                    self.takestock(exc,money,'cows',player)
                if player.ewes>self.limewes:
                    exc=player.ewes-self.limewes
                    money=3*exc
                    tx=tx+'Player '+player.name+' had '+str(player.ewes)+' ewes ('+str(exc)+' extra). The extra stock has been taken and you recieve £'+str(money)+' for that stock (£3/ewe).\n'
                    self.takestock(exc,money,'ewes',player)
                if player.sows>self.limsows:
                    exc=player.sows-self.limsows
                    money=10*exc
                    tx=tx+'Player '+player.name+' had '+str(player.sows)+' sows ('+str(exc)+' extra). The extra stock has been taken and you recieve £'+str(money)+' for that stock (£10/sow).\n'
                    self.takestock(exc,money,'sows',player)
                if player.horses>self.limhorses:
                    exc=player.horses-self.limhorses
                    money=20*exc
                    tx=tx+'Player '+player.name+' had '+str(player.horses)+' cows ('+str(exc)+' extra). The extra stock has been taken and you recieve £'+str(money)+' for that stock (£20/horse).\n'
                    self.takestock(exc,money,'cows',player)
                i+=1
            tx=tx+'Click the Advance button to continue.'
            self.settx(gui,tx)
            #exit card
        #elif self.click==2:
            self.click=0
            var.cardnum=self.pcardnum
            var.cardinplay=0
            deck[self.pcardnum].click=-1
            #self.run(gui,var,pset,deck)
    
class Debt(Cards):
    '''Class for debt'''
    cardnum=64
    pcardnum=0
    dset=[0,0,0,0,0]
    txops=['Cows','Ewes','Sows','Horses']
    
    def detectd(self,gui,var,pset):
        '''Detect debt fn'''
        detect=0
        tx=''
        i=0
        #loop to detect debt
        while i<var.pnum:
            if pset[i].money<0:
                #add text
                tx=tx+'Player '+pset[i].name+' has gone into debt.\n'
                #change detection
                detect+=1
                self.dset[i]=1
            i+=1
        #if detected
        if detect>0:
            #set text
            tx=tx+'Click the Advance button to continue.'
            self.settx(gui,tx)
            #store last card num
            self.pcardnum=var.cardnum
            #set game to this cardnum
            var.cardnum=self.cardnum
        #return dectection value
        return detect
           
    def run(self,gui,var,pset,deck,file):
        '''Run card64 fn'''
        #set up and find
        if self.click==1:
            #find player
            i=0
            while i<var.pnum:
                if self.dset[i]==1:
                    player=pset[i]
                    break
                i+=1
            #bankrupt
            maxmoney=25*player.cows+3*player.ewes+10*player.sows+20*player.horses
            if abs(player.money)>maxmoney:
                tx='Player '+player.name+' is bankrupt.\nYou only have £'+str(maxmoney)+' assets.\nThe bank has reposested the farm and you are out of the game.'
                self.settx(gui,tx)
                #set values
                player.ingame=0
                self.dset[i]=0
                player.cows=0
                player.ewes=0
                player.sows=0
                player.horses=0
                player.hcalves=0
                player.bcalves=0
                player.lambs=0
                player.spigs=0
                player.wheat=0
                player.barley=0
                player.oats=0
                player.potatoes=0
                player.ley=0
                player.roots=0
                player.pasture=0
                player.hay=0
                player.money=0
                player.txcows.configure(text=0)
                player.txewes.configure(text=0)
                player.txsows.configure(text=0)
                player.txhorses.configure(text=0)
                player.txhc.configure(text=0)
                player.txbc.configure(text=0)
                player.txlambs.configure(text=0)
                player.txsp.configure(text=0)
                player.txwheat.configure(text=0)
                player.txbarley.configure(text=0)
                player.txoats.configure(text=0)
                player.txpotatoes.configure(text=0)
                player.txroots.configure(text=0)
                player.txhay.configure(text=0)
                player.txcows.configure(text=0)
                player.txpasture.configure(text=0)
                player.txley.configure(text=0)
                player.txm.configure(text=0)
                #end card
                self.click=1
                var.cardnum=self.pcardnum
                var.cardinplay=0
                deck[self.pcardnum].click=-1
            else:
                #not bankrupt
                tx='Player '+player.name+': you must sell your stock to clear the outstanding money of £'+str(abs(player.money))+'.\nYou must sale your stock to the auction ring at the following prices until your debt is cleared.\n\t1: Sell cows to the Auction ring for £25/cow.\n\t2: Sell sheep to the Auction ring for £3/sheep.\n\t3: Sell sows to the Auction ring for £10/sow.\n\t4: Sell cows to the Auction ring for £20/horse.\nUse the buttons below to select the stock you want to sell, then click Advance button.'
                self.settx(gui,tx)
                #set options
                gui.cbenable(4,1)
                gui.openable(4,1)
                gui.settxop(4,self.txops)
                #set numeric up down values
                gui.op[0].setvalues(minv=0,maxv=pset[i].cows,start=0,incup=1,incdown=1)
                gui.op[1].setvalues(minv=0,maxv=pset[i].ewes,start=0,incup=5,incdown=5)
                gui.op[2].setvalues(minv=0,maxv=pset[i].sows,start=0,incup=1,incdown=1)
                gui.op[3].setvalues(minv=0,maxv=pset[i].horses,start=0,incup=1,incdown=1)
                #sum money
                gui.mop.txvalue.after(200,self.checkdebt,gui,self.click)
        #get options, apply disable
        if self.click==2:
            k=0
            while k<var.pnum:
                if self.dset[k]==1:
                    player=pset[k]
                    break
                k+=1
            #get options
            values=[]
            i=0
            while i<4:
                values.append(gui.op[i].getvalue())
                i+=1
            money=[values[0]*25,values[1]*3,values[2]*10,values[3]*20]
            j=0
            while j<4:
                self.takestock(values[j],money[j],self.txops[j],player)
                gui.resetcb(gui.cb[j])
                gui.op[j].reset()
                j+=1
            #disable and reset (abv) options
            gui.cbenable(4,0)
            gui.openable(4,0)
            #change dset
            if player.money>=0:
                self.dset[k]=0
            #set text
            self.settx(gui,tx='The stock has been sold.\nClick the Advance button to continue.')
            #exit card
            if sum(self.dset)!=0:
                self.click=0
            else:
                self.click=0
                var.cardnum=self.pcardnum
                var.cardinplay=0
                deck[self.pcardnum].click=-1
                
    def checkdebt(self,gui,click):
        if self.click==click:
            gui.mop.txvalue.after(200,self.checkdebt,gui,click)
            a=gui.op1.getvalue()*25+gui.op2.getvalue()*3+gui.op3.getvalue()*10+gui.op4.getvalue()*20
            gui.settxvalue(gui.mop.txvalue,a)
        elif self.click!=click:
            gui.settxvalue(gui.mop.txvalue,0)
            return
        else:
            gui.mop.txvalue.after(200,self.checkdebt,gui,click)
    
class Randops(Cards):
    '''Base class for random card options'''
    inclickrad=0 #interal click value
    
    def opsetr(self,gui):
        '''Enable and set options'''
        self.txoptions2=['Fully random','Game placed','Players placed','No additional']
        #enable options
        gui.cbenable(4,1)
        #set options teext
        gui.settxop(4,self.txoptions2)
            
    def opgetr(self,gui,var):
        '''Get selected options'''
        #disable options
        gui.cbenable(4,0)
        #get option values
        fr=gui.getvalue(gui.opv1)
        gp=gui.getvalue(gui.opv2)
        pp=gui.getvalue(gui.opv3)
        na=gui.getvalue(gui.opv4)
        #random placment
        if (fr==1 and gp==0 and pp==0 and na==0):
            #change value
            var.randoption=1
            #reset option
            gui.resetcb(gui.cb1)
            #return text
            return 'Players have selected to use the 8 additional cards and for them to be placed randomly.'
        #game placed
        elif (gp==1 and fr==0 and pp==0 and na==0):
            var.randoption=2
            gui.resetcb(gui.cb2)
            return 'Players have selected to use the 8 additional cards and for them to be placed as defualt by the game.'
        #player placed
        elif (pp==1 and fr==0 and gp==0 and na==0):
            var.randoption=3
            gui.resetcb(gui.cb3)
            return 'Players have selected to use the 8 additional cards and to place them themselves.'
        #no additional, all, none or multiple
        elif (na==1 or (na==1 and (fr==1 or gp==1 or pp==1)) or (na==0 and pp==0 and gp==0 and fr==0)):
            self.randoption=0
            gui.resetcb(gui.cb1)
            gui.resetcb(gui.cb2)
            gui.resetcb(gui.cb3)
            gui.resetcb(gui.cb4)
            return 'Players have selected not to use the 8 additional cards.'
        else:
            print('er random option')
    
    def setrandcards(self,gui,var,deck,txout):
        ''''Set random cards in the deck fn'''
        tx=''
        c=0 #click change return value
        #fully random
        if var.randoption==1:
            #set each card randomly
            deck[55].cardnum2=float(random()*51+1) #ss1
            deck[56].cardnum2=float(random()*51+1) #ss2
            deck[57].cardnum2=float(random()*51+1) #ss3
            deck[58].cardnum2=float(random()*51+1) #ss4
            deck[59].cardnum2=float(random()*8+8) #dhc1
            deck[60].cardnum2=float(random()*51+1) #dhc2
            deck[61].cardnum2=float(random()*51+1) #dhc3
            deck[62].cardnum2=float(random()*51+1) #dhc4
            #change progress bar max value
            gui.pbar.configure(maximum=61)
            #set click value
            c=0
        #game placed
        elif var.randoption==2:
            #set each card as I feel fit
            deck[55].cardnum2=6.5
            deck[56].cardnum2=20.5
            deck[57].cardnum2=41.5
            deck[58].cardnum2=46.3
            deck[59].cardnum2=9.5
            deck[60].cardnum2=30.5
            deck[61].cardnum2=23.5
            deck[62].cardnum2=46.6
            gui.pbar.configure(maximum=61)
            c=0
        #player placed
        elif var.randoption==3:
            #set up player options
            if self.inclickrad==0:
                tx=txout+'\nPlease place the 8 additional random cards in the deck by selecting the required number in the corresponsing option. Click the Advance button once decided.'
                txopsrad=['Special stock adjustments 1','Special stock adjustments 2','Special stock adjustments 3','Special stock adjustments 4']
                #set text
                self.settx(gui,tx)
                #enable options, set text and set nemeric up down limits
                gui.cbenable(4,1)
                gui.settxop(4,txopsrad)
                gui.openable(4,1)
                gui.op1.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                gui.op2.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                gui.op3.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                gui.op4.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                #increase internal click
                self.inclickrad+=1
                #keep at current card click value
                c=-1
            #get 1st round of options and set 2nd round of options
            elif self.inclickrad==1:
                #get and set player options
                deck[55].cardnum2=gui.op1.getvalue()+float(random()/10)
                deck[56].cardnum2=gui.op2.getvalue()+float(random()/10)
                deck[57].cardnum2=gui.op3.getvalue()+float(random()/10)
                deck[58].cardnum2=gui.op4.getvalue()+float(random()/10)
                tx='Please continue to place the remaining 4 cards. Click the Advance button once decided.'
                txopsrad=['Double Hazard Card 1','Double Hazard Card 2','Double Hazard Card 3','Double Hazard Card 4']
                #display text
                self.settx(gui,tx)
                #set 2nd round of options
                gui.settxop(4,txopsrad)
                gui.op1.setvalues(start=9.5,incup=2,incdown=0.25,minv=8.25,maxv=15.75)
                gui.op2.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                gui.op3.setvalues(start=12.5,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                gui.op4.setvalues(start=12.75,incup=2,incdown=0.25,minv=1.25,maxv=51.75)
                self.inclickrad+=1
                c=-1
            #get 2nd round of options
            elif self.inclickrad==2:
                #get and set player options
                deck[59].cardnum2=gui.op1.getvalue()+float(random()/10)
                deck[60].cardnum2=gui.op2.getvalue()+float(random()/10)
                deck[61].cardnum2=gui.op3.getvalue()+float(random()/10)
                deck[62].cardnum2=gui.op4.getvalue()+float(random()/10)
                tx='The cards have been placed within the deck.'
                #display text
                self.settx(gui,tx)
                #diable options and reset
                gui.cbenable(4,0)
                gui.openable(4,0)
                gui.resetcb(gui.cb1)
                gui.resetcb(gui.cb2)
                gui.resetcb(gui.cb3)
                gui.resetcb(gui.cb4)
                gui.op1.reset()
                gui.op2.reset()
                gui.op3.reset()
                gui.op4.reset()
                #change progress bar max value
                gui.pbar.configure(maximum=61)
                self.inclickrad+=1
                c=0
        #no additonal
        else:
            deck[55].used=1
            deck[56].used=1
            deck[57].used=1
            deck[58].used=1
            deck[59].used=1
            deck[60].used=1
            deck[61].used=1
            deck[62].used=1
            gui.pbar.configure(maximum=53)
            c=0
        #return change to click value
        return c, tx
    
class SSA(Money,Text):
    ''''Base class for Special stock adjustments'''
    ssatxops=['Cows','Ewes','Sows','Horses']
    
    def setbuyssa(self,gui,player):
        '''Set up ssa options: gui==graphics, player=player instance'''
        #enable
        gui.openable(4,1)
        gui.cbenable(4,1)
        #set numeric up down limits
        gui.op1.setvalues(start=0,incup=1,incdown=1,maxv=75-player.cows,minv=0)
        gui.op2.setvalues(start=0,incup=5,incdown=5,maxv=60-player.ewes,minv=0)
        gui.op3.setvalues(start=0,incup=1,incdown=1,maxv=20-player.sows,minv=0)
        gui.op4.setvalues(start=0,incup=1,incdown=1,maxv=4-player.horses,minv=0)
        #set option text
        gui.settxop(4,self.ssatxops)
    
    def getbuyssa(self,gui,player,values):
        '''Get ssa options: gui=gui, player=player instance, values=money array for stock'''
        #get options
        ops=[gui.op1.getvalue(),gui.op2.getvalue(),gui.op3.getvalue(),gui.op4.getvalue(),gui.op5.getvalue()]
        delta=player.money
        #apply options
        i=0
        while i<4:
            self.givestock(ops[i],values[i]*ops[i],self.ssatxops[i].lower(),player)
            #reset
            gui.resetcb(gui.cb[i])
            gui.op[i].reset()
            i+=1
        delta=delta-player.money
        #set text
        tx='Player '+player.name+' has brought '+str(ops[0])+' cows for £'+str(ops[0]*values[0])+', '+str(ops[1])+' ewes for £'+str(ops[1]*values[1])+', '+str(ops[2])+' sows for £'+str(ops[2]*values[2])+' and '+str(ops[3])+' horses for £'+str(ops[3]*values[3])+' for a total of £'+str(delta)+'.'
        self.settx(gui,tx)
        #disable
        gui.openable(4,0)
        gui.cbenable(4,0)
        
    def checkssa(self,gui,click,values):
        if self.click==click:
            gui.mop.txvalue.after(200,self.checkssa,gui,click,values)
            a=gui.op1.getvalue()*values[0]+gui.op2.getvalue()*values[1]+gui.op3.getvalue()*values[2]+gui.op4.getvalue()*values[3]
            gui.settxvalue(gui.mop.txvalue,a)
        elif self.click!=click:
            gui.settxvalue(gui.mop.txvalue,0)
            return
        else:
            gui.mop.txvalue.after(200,self.checkssa,gui,click,values)
        
class DHC(Money,Text):
    '''Base class for Double hazard cards'''
    inclickdhc=0
    inclickdhc2=0
    #drolldhc=0
    #pnumdhc=0
    
    def condition(self,gui,var,sk,lim,value,pset,player,pay):
        '''Apply only if conditions fulfilled: gui=gui, var=global variable instance, sk=array of stock of a certain type, lim=limit testing, value=money, pset=player instance array, player=player instance, pay=1/0'''
        #test condition for each player
        i=0
        tx=''
        while i<var.pnum:
            #skip self
            if pset[i].pid!=player.pid and pset[i].ingame==1:
                #condition test
                if sk[i]>lim:
                    #pay/receive test
                    if pay==1:
                        self.transfermoney(value,player,pset[i])
                        tx+='Player '+player.name+' has paid £'+str(value)+' to '+pset[i].name+'.\n'
                    elif pay==0:
                        self.transfermoney(value,pset[i],player)
                        tx+='Player '+player.name+' has received £'+str(value)+' from '+pset[i].name+'.\n'
                    else:
                        print('er pay')
                else:
                    if pay==1:
                        tx+='Player '+player.name+' has paid £0 to '+pset[i].name+'.\n'
                    elif pay==0:
                        tx+='Player '+player.name+' has received £0 from '+pset[i].name+'.\n'
                    else:
                        print('er pay')
            i+=1
        #lambs
        if lim==40:
            j=0
            while j<var.pnum:
                if pset[j].pid!=player.pid and pset[i].ingame==1:
                    if pset[j].lambs>0:
                        self.transfermoney(5,player,pset[j])
                        tx+='Player '+player.name+' has piad £5 to '+pset[j].name+'.\n'
                    else:
                        tx+='Player '+player.name+' has piad £0 to '+pset[j].name+'.\n'
                j+=1
        tx+='Click the Advance button to continue.'
        #set text
        self.settx(gui,tx)
    
    def diceroll(self,gui,var,txdice,txv,pset,player,roll,pay):
        '''m'''
        self.dswitch=1
        if (self.inclickdhc==0 or self.inclickdhc==2 or self.inclickdhc==4 or self.inclickdhc==6 or self.inclickdhc==8):
            #allow roll if player in game
            if pset[int(self.inclickdhc/2)].ingame==1 and pset[int(self.inclickdhc/2)].pid!=player.pid:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[int(self.inclickdhc/2)])
                #set to index for player in pset = click-1
                #self.pnumdhc=self.click-1
                self.pnum=int(self.inclickdhc/2)
                self.inclickdhc+=1
                self.click+=6
            #move onto next player
            else:
                self.inclickdhc+=2
                self.diceroll(gui,var,txdice,txv,pset,player,roll,pay)
        elif (self.inclickdhc==1 or self.inclickdhc==3 or self.inclickdhc==5 or self.inclickdhc==7 or self.inclickdhc==9):
            tx='Player '+player.name+': '+txdice[roll-1]+pset[int((self.inclickdhc-1)/2)].name+'.'
            if txv[roll-1][1]=='money':
                if pay==1:
                    self.transfermoney(txv[roll-1][2]*txv[roll-1][0],player,pset[int((self.inclickdhc-1)/2)])
                elif pay==0:
                    self.transfermoney(txv[roll-1][2]*txv[roll-1][0],pset[int((self.inclickdhc-1)/2)],player)
                else:
                    print('pay er')
            elif txv[roll-1][1]=='option':
                if txv[roll-1][2]==1:
                    self.opsturn=1
                    self.inclickdhc+=9
                else:
                    self.opsturn=0
            else:
                #set money value to 0 and hold it if needed
                a=txv[roll-1][2]
                txv[roll-1][2]=0
                if pay==1:
                    #take stock
                    self.transferstock(txv[roll-1][0],txv[roll-1][2],txv[roll-1][1],player,pset[int((self.inclickdhc-1)/2)])
                    #-ve stock check and correct
                    b=player.guidic[txv[roll-1][1]]['text']
                    if b<0:
                        #costdic={'cows':70,'ewes':6,'sows':35,'horses':50}
                        self.givestock(abs(b),a*abs(b),txv[roll-1][1],player)
                        tx+='\nPlayer '+player.name+' dosen\'t have enough '+txv[roll-1][1]+', so instead has bought the player the stock instead at £'+str(a)+' each.'
                elif pay==0:
                    #take stock
                    self.transferstock(txv[roll-1][0],txv[roll-1][2],txv[roll-1][1],pset[int((self.inclickdhc-1)/2)],player)
                    #-ve stock check and correct
                    b=pset[int((self.inclickdhc-1)/2)].guidic[txv[roll-1][1]]['text']
                    if b<0:
                        self.givestock(abs(b),a*abs(b),txv[roll-1][1],pset[int((self.inclickdhc-1)/2)])
                        tx+='\nPlayer '+pset[int((self.inclickdhc-1)/2)].name+' dosen\'t have enough '+txv[roll-1][1]+', so instead has bought the player the stock instead at £'+str(a)+' each.'
            #set text
            self.settx(gui,tx)
            self.inclickdhc+=1
            self.click-=1
        elif self.inclickdhc==10:
            self.settx(gui,'All Players have rolled for this result.\nClick the Advance button to continue.')
            self.inclickdhc=0
            self.dswitch=0
            #self.click-=6
        elif (self.inclickdhc==11 or self.inclickdhc==13 or self.inclickdhc==15 or self.inclickdhc==17 or self.inclickdhc==19):
            self.pickoptions(gui,self.txops,self.txopresult,pset[int((self.inclickdhc-11)/2)].cows,player,pset[int((self.inclickdhc-11)/2)])
            #gui,txops,txv,stock,pto,pfrom
        #self.click+=6
        else:
            print('er diceroll')
    
    def onleft(self,gui,var,amount,pset,player,pay):
        '''Find player on left and apply result: gui=gui, var=global variable instance amount=money, pset=player instance array, player=player instance, pay=1/0'''
        a=player.pid
        if a==var.pnum:
            a=0
        i=a
        while i<var.pnum:
            if pset[i].ingame==1:
                b=i
                break
            i+=1
            if i==var.pnum:
                i=0
        if pay==1:
            self.transfermoney(amount,player,pset[b])
            tx='Player '+player.name+' has paid £'+str(amount)+' to '+pset[b].name+'.\n'
        elif pay==0:
            self.transfermoney(amount,pset[b],player)
            tx='Player '+player.name+' has received £'+str(amount)+' from '+pset[b].name+'.\n'
        tx+='Click the Advance button to continue.'
        self.settx(gui,tx)
    
    def pickoptions(self,gui,txops,txv,stock,pto,pfrom):
        '''m'''
        #enable options
        if self.inclickdhc2==0:
            #enable
            gui.cbenable(2,1)
            #disable stock option if none
            if stock<1:
                gui.cbenable(1,0)
            #set options text
            gui.settxop(2,txops)
            #multi selection test
            gui.enable(gui.btnadvance,0)
            gui.cb[0].after(200,self.checkcbdhc,gui)
            #set text
            tx='Player '+pfrom.name+' please pick the option you want to apply.'
            self.settx(gui,tx)
            #click change
            self.inclickdhc2+=1
            #self.inclickdhc-=1
            self.click-=1
            self.click+=6
        elif self.inclickdhc2==1:
            #get options
            a=gui.getvalue(gui.opv1)
            b=gui.getvalue(gui.opv2)
            #apply option
            if a==1 and b==0:
                #money option
                self.transfermoney(txv[2],pfrom,pto)
                tx='You have picked to '+txops[0].lower()+'.'
            elif b==1 and a==0:
                #stock option
                self.transferstock(txv[0],0,txv[1],pfrom,pto)
                tx='You have picked to '+txops[1].lower()+'.'
            else:
                print('er dhc option')
            #reset and disable options
            gui.cbenable(2,0)
            gui.resetcb(gui.cb1)
            gui.resetcb(gui.cb2)
            #set text
            self.settx(gui,tx)
            #click change
            self.inclickdhc2=0
            self.opsturn=0
            self.click+=6
            self.click-=1
            self.inclickdhc-=9
            
            
    def checkcbdhc(self,gui):
        if (self.inclickdhc2==1 and (gui.getvalue(gui.opv1)+gui.getvalue(gui.opv2)==1)):
            gui.enable(gui.btnadvance,1)
            gui.cb[0].after(200,self.checkcbdhc,gui)
        elif self.inclickdhc2!=1:
            return
        else:
            gui.enable(gui.btnadvance,0)
            gui.cb[0].after(200,self.checkcbdhc,gui)
            
#    def rundhc(self,gui,player):
#        '''Run dhc options'''
#        pass
        
class SSA1(Cards,SSA):
    '''Special Stock Adjustments 1 random card class'''
    used=0
    title='-SPECIAL STOCK ADJUSTMENT-\nInsert at random'
    cardnum2=55
    cardnum='STOCK ADJUSTMENT'
    pcardnum=0
    cardfontcol='black'
    txmain='Players may buy extra stock, if available, direct from the Auctioneer as follows:-\nCows:\t£45 each.\nEwes:\t£25 for a pen of five.\nSows:\t£20 each.\nHorses:\t£35 each.'
    txoutput=['Players in turn will buy their stock. Click the Advance button to begin.',
              ' please enter the amount of stock you want to buy',
              'All players have bought the stock they wanted. Click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card55 fn'''
        self.values=[45,5,20,35]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
            #store last card num
            #self.pcardnum=var.cardnum
            #set game to this cardnum
            #var.cardnum=self.cardnum
        #set up buying
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set ssa\n')
            #allow roll if player in game
            if pset[int((self.click-1)/2)].ingame==1:
                #set options
                self.setbuyssa(gui,pset[int((self.click-1)/2)])
                self.checkssa(gui,self.click,self.values)
                #set text
                self.settxoutwithtx(gui,1,pset[int((self.click-1)/2)].name,'')
            #move onto next player
            else:
                self.click+=2
                self.run(gui,var,pset,deck,file)
        #take options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('get ssa\n')
            self.getbuyssa(gui,pset[int(self.click/2-1)],self.values)
        #end card
        elif self.click==11:
            file('End ssa\n')
            #set text
            self.settxout(gui,2)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
            print(var.cardnum)
        else:
            print('er card55')
    
class SSA2(Cards,SSA):
    '''Special Stock Adjustments 2 random card class'''
    used=0
    title='-SPECIAL STOCK ADJUSTMENT-\nInsert at random'
    cardnum2=56
    cardnum='STOCK ADJUSTMENT'
    pcardnum=0
    cardfontcol='black'
    txmain='Players may buy extra stock, if available, direct from the Auctioneer as follows:-\nCows:\t£50 each.\nEwes:\t£25 for a pen of five.\nSows:\t£20 each.\nHorses:\t£40 each.'
    txoutput=['Players in turn will buy their stock. Click the Advance button to begin.',
              ' please enter the amount of stock you want to buy',
              'All players have bought the stock they wanted. Click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card56 fn'''
        self.values=[50,5,25,40]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up buying
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set ssa\n')
            #allow roll if player in game
            if pset[int((self.click-1)/2)].ingame==1:
                #set options
                self.setbuyssa(gui,pset[int((self.click-1)/2)])
                self.checkssa(gui,self.click,self.values)
                #set text
                self.settxoutwithtx(gui,1,pset[int((self.click-1)/2)].name,'')
            #move onto next player
            else:
                self.click+=2
                self.run(gui,var,pset,deck,file)
        #take options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('get ssa\n')
            self.getbuyssa(gui,pset[int(self.click/2-1)],self.values)
        #end card
        elif self.click==11:
            file('End ssa\n')
            #set text
            self.settxout(gui,2)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
            print(var.cardnum)
        else:
            print('er card56')
    
class SSA3(Cards,SSA):
    '''Special Stock Adjustments 3 random card class'''
    used=0
    title='-SPECIAL STOCK ADJUSTMENT-\nInsert at random'
    cardnum2=57
    cardnum='STOCK ADJUSTMENT'
    cardfontcol='black'
    txmain='Players may buy extra stock, if available, direct from the Auctioneer as follows:-\nCows:\t£55 each.\nEwes:\t£30 for a pen of five.\nSows:\t£25 each.\nHorses:\t£50 each.'
    txoutput=['Players in turn will buy their stock. Click the Advance button to begin.',
              ' please enter the amount of stock you want to buy',
              'All players have bought the stock they wanted. Click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card57 fn'''
        self.values=[55,6,25,50]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up buying
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set ssa\n')
            #allow roll if player in game
            if pset[int((self.click-1)/2)].ingame==1:
                #set options
                self.setbuyssa(gui,pset[int((self.click-1)/2)])
                self.checkssa(gui,self.click,self.values)
                #set text
                self.settxoutwithtx(gui,1,pset[int((self.click-1)/2)].name,'')
            #move onto next player
            else:
                self.click+=2
                self.run(gui,var,pset,deck,file)
        #take options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('get ssa\n')
            self.getbuyssa(gui,pset[int(self.click/2-1)],self.values)
        #end card
        elif self.click==11:
            file('End ssa\n')
            #set text
            self.settxout(gui,2)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
            print(var.cardnum)
        else:
            print('er card57')
    
class SSA4(Cards,SSA):
    '''Special Stock Adjustments 4 random card class'''
    used=0
    title='-SPECIAL STOCK ADJUSTMENT-\nInsert at random'
    cardnum2=58
    cardnum='STOCK ADJUSTMENT'
    pcardnum=0
    cardfontcol='black'
    txmain='Players may buy extra stock, if available, direct from the Auctioneer as follows:-\nCows:\t£60 each.\nEwes:\t£40 for a pen of five.\nSows:\t£30 each.\nHorses:\t£45 each.'
    txoutput=['Players in turn will buy their stock. Click the Advance button to begin.',
              ' please enter the amount of stock you want to buy',
              'All players have bought the stock they wanted. Click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card58 fn'''
        self.values=[60,8,30,45]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up buying
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set ssa\n')
            #allow roll if player in game
            if pset[int((self.click-1)/2)].ingame==1:
                #set options
                self.setbuyssa(gui,pset[int((self.click-1)/2)])
                self.checkssa(gui,self.click,self.values)
                #set text
                self.settxoutwithtx(gui,1,pset[int((self.click-1)/2)].name,'')
            #move onto next player
            else:
                self.click+=2
                self.run(gui,var,pset,deck,file)
        #take options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('get ssa\n')
            self.getbuyssa(gui,pset[int(self.click/2-1)],self.values)
        #end card
        elif self.click==11:
            file('End ssa\n')
            #set text
            self.settxout(gui,2)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
            print(var.cardnum)
        else:
            print('er card58')
    
class DHC1(Cards,Dice):
    '''Double Hazard 1 random card class'''
    used=0
    title='-DOUBLE HAZARD CARD-\nInsert before Card No.16. (and after Card No.8.)'
    cardnum2=59
    cardnum='CROP ADJUSTMENT'
    pcardnum=0
    cardfontcol='red'
    txmain='1: Increase potato acreage by 10 acres at £250 per 10 acres. Pay the money to the Bank.\n2: Increase barley acreage by 10 acres at £30 per 10 acres. Pay the money to the Bank.\n3: Increase oats acreage by 10 acres at £40 per 10 acres. Pay the money to the Bank.\n4: Increase wheat acreage by 10 acres at £20 per 10 acres. Pay the money to the Bank.\n5: Increase potato and wheat acreage by 10 acres each at a total of £270. Pay the money to the Bank.\n6: Increase barley and oats acreage by 10 acres at a total of £70. Pay the money to the Bank.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
              'There is only 1 player left in the game, therefore this card cannot be played. Click the Next Card button to continue.']
    txdice=['Increase potato acreage by 10 acres at £250 per 10 acres. Pay the money to the Bank.','Increase barley acreage by 10 acres at £30 per 10 acres. Pay the money to the Bank.','Increase oats acreage by 10 acres at £40 per 10 acres. Pay the money to the Bank.','Increase wheat acreage by 10 acres at £20 per 10 acres. Pay the money to the Bank.','Increase potato and wheat acreage by 10 acres each at a total of £270. Pay the money to the Bank.','Increase barley and oats acreage by 10 acres at a total of £70. Pay the money to the Bank.']
    dtype='dhccrops'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card59 fn'''
        self.tx=[[1,'potatoes',250],[1,'barley',30],[1,'oats',40],[1,'wheat',20],[1,'potatoeswheat',270],[1,'barleyoats',70]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            #set text
            self.settxout(gui,1)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
        else:
            print('er card59')
    
    
class DHC2(Cards,Dice,DHC):
    '''Double Hazard 2 random card class'''
    used=0
    title='-DOUBLE HAZARD CARD-\nInsert at random'
    cardnum2=60
    cardnum='ADMINISTRATION'
    pcardnum=0
    cardfontcol='red'
    txmain='1: Your dog has been worrying sheep. Pay £10 compensation to each farmer with more than 40 ewes and an extra £5 compensation if any farmer also has lambs.\n2: During crop spraying, the wind carried the spray in the wrong direction. Each farmer throws the dice. If a 1 or a 6 is thrown, you must pay £10 compensation to the player. No action is necessary if any other number is thrown.\n3: For buying silage from your neighbours during the winter, pay £15 to every farmer with less than 55 cows.\n4: While on the road, your tractor ran into your neighbour\'s dairy herd. Each farmer throws the dice. If an odd number is thrown, you give the player 1 of your cows. If an even number is thrown, you give the player 2 cows.\n5: You pay each farmer £5 for extra straw.\n6: You need extra pasture for your dairy herd. Pay £50 to the farmer on your left.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
              'There is only 1 player left in the game, therefore this card cannot be played. Click the Next Card button to continue.']
    txdice=['Your dog has been worrying sheep. Pay £10 compensation to each farmer with more than 40 ewes and an extra £5 compensation if any farmer also has lambs.','During crop spraying, the wind carried the spray in the wrong direction. Each farmer throws the dice. If a 1 or a 6 is thrown, you must pay £10 compensation to the player. No action is necessary if any other number is thrown.','For buying silage from your neighbours during the winter, pay £15 to every farmer with less than 55 cows.','While on the road, your tractor ran into your neighbour\'s dairy herd. Each farmer throws the dice. If an odd number is thrown, you give the player 1 of your cows. If an even number is thrown, you give the player 2 cows.','You pay each farmer £5 for extra straw.','You need extra pasture for your dairy herd. Pay £50 to the farmer on your left.']
    dtype='dhc'
    pnum=0 #required for dice roll
    drolldhc=0
    drolldhc2=0
    dswitch=0
    pay=1
    
    def run(self,gui,var,pset,deck,file):
        '''Run card60 fn'''
        print('dhc',self.click)
        self.tx=[[5,'money',10],[0,'money',10],[0,'money',15],[2,'cows',1],[0,'money',5],[0,'money',50]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            if self.click==1:
                #test if can play card
                count=0
                i=0
                while i<var.pnum:
                    if pset[i].ingame==1:
                        count+=1
                    i+=1
                if count==0:
                    self.settxout(gui,2)
                    #correct cardnum
                    var.cardnum=self.pcardnum-1
                    var.cardinplay=0
                    #deck[self.pcardnum].click=-1
                    self.used=1
                    #button swap
                    gui.btnswap(1)
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            #set text
            self.settxout(gui,1)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
        #multi roll
        elif self.click>6 and self.click<12:
            file('Multi roll\n')
            if self.drolldhc==1:
                sk=[pset[0].ewes,pset[1].ewes,pset[2].ewes,pset[3].ewes,pset[4].ewes]
                self.condition(gui,var,sk,40,10,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==2:
                self.txdice2=['Pay £10 to ','No further action involving ','No further action involving ','No further action involving ','No further action involving ','Pay £10 to ']
                self.tx2=[[1,'money',10],[0,'money',0],[0,'money',0],[0,'money',0],[0,'money',0],[1,'money',10]]
                self.diceroll(gui,var,self.txdice2,self.tx2,pset,pset[self.click-1-6],self.drolldhc2,self.pay)
            elif self.drolldhc==3:
                #-ve in both to change to less than '<'
                sk=[-pset[0].cows,-pset[1].cows,-pset[2].cows,-pset[3].cows,-pset[4].cows]
                self.condition(gui,var,sk,-55,15,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==4:
                self.txdice2=['Give 1 cow to ','Give 2 cows to ','Give 1 cow to ','Give 2 cows to ','Give 1 cow to ','Give 2 cows to ']
                self.tx2=[[1,'cows',70],[2,'cows',70],[1,'cows',70],[2,'cows',70],[1,'cows',70],[2,'cows',70]]
                self.diceroll(gui,var,self.txdice2,self.tx2,pset,pset[self.click-1-6],self.drolldhc2,self.pay)
            elif self.drolldhc==5:
                sk=[pset[0].money,pset[1].money,pset[2].money,pset[3].money,pset[4].money]
                self.condition(gui,var,sk,-500,5,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==6:
                self.onleft(gui,var,50,pset,pset[self.click-1-6],self.pay)
            else:
                print('er drolldhc')
            #correct click
            self.click-=6
        else:
            print('er card60')
    
class DHC3(Cards,Dice,DHC):
    '''Double Hazard 3 random card class'''
    used=0
    title='-DOUBLE HAZARD CARD-\nInsert at random'
    cardnum2=61
    cardnum='ADMINISTRATION'
    pcardnum=0
    cardfontcol='red'
    txmain='1: Your neighbours\' stock have damaged some of your crops. Collect £20 compensation from each farmer.\n2: You lent 1 of your tractors to a neighbour. Each farmer throws the dice and if a 4 is thrown, that player must pay you £80 rental. No action is taken with any other number.\n3: You have organised a joint stand at the local Agricultural Show. Collect £10 from each farmer.\n4: Last year you sold some hay to 1 of your neighbours. Each farmer throws a dice and if a 3 or 5 is thrown, the player can either pay you £70 or 1 Cow. No action is taken with any other number.\n5: If you have 2 or more horses, each farmer pays you £15 to cover its loan during wet weather.\n6: Your neighbours\' stock have caused extensive damage to 1 of your fences. Collect £60 from the player on your left.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
              'There is only 1 player left in the game, therefore this card cannot be played. Click the Next Card button to continue.']
    txdice=['Your neighbours\' stock have damaged some of your crops. Collect £20 compensation from each farmer.','You lent 1 of your tractors to a neighbour. Each farmer throws the dice and if a 4 is thrown, that player must pay you £80 rental. No action is taken with any other number.','You have organised a joint stand at the local Agricultural Show. Collect £10 from each farmer.','Last year you sold some hay to 1 of your neighbours. Each farmer throws a dice and if a 3 or 5 is thrown, the player can either pay you £70 or 1 Cow. No action is taken with any other number.','If you have 2 or more horses, each farmer pays you £15 to cover its loan during wet weather.','Your neighbours\' stock have caused extensive damage to 1 of your fences. Collect £60 from the player on your left.']
    dtype='dhc'
    pnum=0 #required for dice roll
    drolldhc=0
    drolldhc2=0
    dswitch=0
    pay=0
    opsturn=0
    
    def run(self,gui,var,pset,deck,file):
        '''Run card61 fn'''
        self.tx=[[0,'money',20],[0,'money',80],[0,'money',10],[1,'cows',70],[0,'money',15],[0,'money',60]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            if self.click==1:
                #test if can play card
                count=0
                i=0
                while i<var.pnum:
                    if pset[i].ingame==1:
                        count+=1
                    i+=1
                if count==0:
                    self.settxout(gui,2)
                    #correct cardnum
                    var.cardnum=self.pcardnum-1
                    var.cardinplay=0
                    #deck[self.pcardnum].click=-1
                    self.used=1
                    #button swap
                    gui.btnswap(1)
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            #set text
            self.settxout(gui,1)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
        #multi roll
        elif self.click>6 and self.click<12:
            file('Multi roll\n')
            if self.drolldhc==1:
                sk=[pset[0].money,pset[1].money,pset[2].money,pset[3].money,pset[4].money]
                self.condition(gui,var,sk,-500,20,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==2:
                self.txdice2=['No further action involving ','No further action involving ','No further action involving ','Receive £80 from ','No further action involving ','No further action involving ']
                self.tx2=[[0,'money',0],[0,'money',0],[0,'money',0],[1,'money',80],[0,'money',0],[0,'money',0]]
                self.diceroll(gui,var,self.txdice2,self.tx2,pset,pset[self.click-1-6],self.drolldhc2,self.pay)
            elif self.drolldhc==3:
                sk=[pset[0].money,pset[1].money,pset[2].money,pset[3].money,pset[4].money]
                self.condition(gui,var,sk,-500,10,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==4:
                self.txdice2=['No further action involving ','No further action involving ','Receive 1 cow or £70 from ','No further action involving ','Receive 1 cow or £70 from ','No further action involving ']
                self.tx2=[[0,'option',0],[0,'option',0],[0,'option',1],[0,'option',0],[0,'option',1],[0,'option',0]]
                self.txops=['Pay £70','Give 1 cow']
                self.txopresult=[1,'cows',70]
                self.diceroll(gui,var,self.txdice2,self.tx2,pset,pset[self.click-1-6],self.drolldhc2,self.pay)
                
            elif self.drolldhc==5:
                sk=[pset[self.click-1-6].horses,pset[self.click-1-6].horses,pset[self.click-1-6].horses,pset[self.click-1-6].horses,pset[self.click-1-6].horses]
                #2 or more use >1
                self.condition(gui,var,sk,1,15,pset,pset[self.click-1-6],self.pay)
            elif self.drolldhc==6:
                self.onleft(gui,var,60,pset,pset[self.click-1-6],self.pay)
            else:
                print('er drolldhc')
            #correct click
            self.click-=6
        else:
            print('er card61')
    
class DHC4(Cards,Dice):
    '''Double Hazard 4 random card class'''
    used=0
    title='-DOUBLE HAZARD CARD-\nInsert at random'
    cardnum2=62
    cardnum='CASH ADJUSTMENT'
    pcardnum=0
    cardfontcol='red'
    txmain='1: Income Tax Demand - Pay £200 to the Bank.\n2: Bank Interest - Pay £250 to the Bank.\n3: Rent on extra pasture - Pay £175 to the Bank.\n4: Grant agreed on drainage - Receive £250 from the Bank.\n5: Bank error in your favour - Receive £200 from the Bank.\n6: Insurance payment - Receive £150 from the Bank.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
              'There is only 1 player left in the game, therefore this card cannot be played. Click the Next Card button to continue.']
    txdice=['Income Tax Demand - Pay £200 to the Bank.','Bank Interest - Pay £250 to the Bank.','Rent on extra pasture - Pay £175 to the Bank.','Grant agreed on drainage - Receive £250 from the Bank.','Bank error in your favour - Receive £200 from the Bank.','Insurance payment - Receive £150 from the Bank.']
    dtype='dhcmoney'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card62 fn'''
        self.tx=[[1,'money',200],[1,'money',250],[1,'money',175],[1,'money',-250],[1,'money',-200],[1,'money',-150]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            #set text
            self.settxout(gui,1)
            #correct cardnum
            var.cardnum=self.pcardnum-1
            var.cardinplay=0
            #deck[self.pcardnum].click=-1
            self.used=1
            #button swap
            gui.btnswap(1)
        else:
            print('er card62')
        
class Card0(Dops,Randops,ARops):
    '''Card0 class'''
    title='GAME OPTIONS'
    cardnum=0
    cardfontcol='black'
    txmain='To start the game players must descide their name for game.\nPlayers must also decide whether to use the game dice or to use their own dice and whether or not to place the 8 random cards within hte deck of cards.'
    txoutput=['Players, please enter your names in the corresponding players boxes and then click the Advance button.',
              'Do players want to use a dice or to use the random dice on the computer? If you want to use the computer dice select \'yes\' below, if you want to use your own dice select \'no\', if no option or both options are selected it is assumed you are using your own dice. After selecting your option click the Advance button.',
              'Do players want to use the 8 additional cards to test your skill\'s more and do you want them to be entered randomly, placed as default by the game or to place them yourself? Select \'fully random\' for the cards to be added randomly, \'game placed\' to play with the cards placed as default by the game, \'players placed\' for the players to decide where the random cards go and \'no additional\' to not use the additional cards. If no or multiple options are selected they will not be used. After selecting your option click the Advance button.',
              'Do players want to use the Risk feature? (This is the white column attached to each player. It will highlight red if the player is at risk of debt and yellow if it\'s possible. It will remain green if there is no risk of debt). This function will take some time to run.',
              'Click the Next Card button to start the game.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run fn for card0'''
        #set inital text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #disable player names box, set names and enable dice options
        elif self.click==1:
            #write file
            file('Get player names, dice option set\n')
            #disable player entry
            i=0
            while i<var.pnum:
                pset[i].enable(pset[i].txname,0)
                i+=1
            #set player names
            for x in pset:
                x.setname()
            #set pops list
            self.setpops(gui,pset)
            self.settxout(gui,self.click)
            #enable dice options
            self.opsetd(gui)
        #get dice options and set random card options
        elif self.click==2:
            file('Get dice option, random text\n')
            #get dice options
            txout=self.opgetd(gui,var)
            self.settxoutwithtx(gui,self.click,txout,'\n')
            #enable random card options
            self.opsetr(gui)
        #get random card options
        elif self.click==3:
            file('Get random option\n')
            txout='Q'
            #can be multiple click fn
            if self.inclickrad==0:
                txout=self.opgetr(gui,var)
                self.settxoutwithtx(gui,self.click,txout,'\n')
            #set random cards
            c,txout2=self.setrandcards(gui,var,deck,txout)
            if self.inclickrad==3:
                self.settxoutwithtx(gui,self.click,txout2,'\n')
            #chance click value if required
            self.click+=c
            #set at risk options only if inclickrad complete
            if self.click==3:
                #self.settxout(gui,self.click)
                self.opsetar(gui)
        #get at risk option and end card
        elif self.click==4:
            file('Get at risk option\n')
            #get at risk option
            txout=self.opgetar(gui,var)
            self.settxoutwithtx(gui,self.click,txout,'\n')
            #end car
            gui.btnswap(1)
            
class Card1(Cards,PickCrops):
    title='STARTING STOCK AND CASH AND CROPPING RETURN'
    cardnum=1
    cardfontcol='black'
    txmain='Each farmer receives 60 cows, 50 ewes, 16 sows and 2 horses, and £1,500 in money, and the remainder of stock and cash is put in the auction and the bank.\nEach farmer receives a card representing 100 acres of roots, hay and pasture, and in turn chooses their crops for the remaining 10 fields of 10 acres each that they are farming, and obtains cards for them from the Auction Ring.'
    txoutput=['Click the Advance button to begin picking your crops.',
              'please pick the amount of Wheat, Barley, Oats, Potatoes and Ley (only enter the ley you definalty want as any unassigned fields will be ley) you want for the year and then click Advance.',
              'has selected more than 10x10 acres. Please re-enter your values.',
              'Players have picked their crops.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card1 fn'''
        #set inital text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #for each in game player ask for crop choice
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set pick crops\n')
            #ingame test
            if pset[int((self.click+1)/2-1)].ingame==0:
                #skip next player if not in game
                self.click+=2
                self.run(gui,var,pset,deck,file)
            else:
                #set text for chossing
                tx=pset[int((self.click+1)/2-1)].name
                self.settxoutwithtx(gui,1,tx,' ')
                #pick crops
                self.pickcrops(gui)
                self.checkcrops(gui,self.click)
        #get player crop choice and check legal
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('Get player crops\n')
            #get player name
            tx=pset[int(self.click/2-1)].name
            #check slection is legal
            c=self.croplegal(gui,pset[int(self.click/2-1)])
            self.click+=c
            #not legal- set text
            if (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
                self.settxoutwithtx(gui,2,tx,' ')
            #legal- get crops and move onto next
            else:
                self.getcrops(gui,pset[int(self.click/2-1)])
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #state choices and end card
        elif self.click==11:
            file('Set crop chioces\n')
            #text loop
            tx=''
            i=0
            while i<5:
                if pset[i].ingame==1:
                    tx=tx+pset[i].name+' has selected '+str(pset[i].wheat)+'x10 acres of wheat, '+str(pset[i].barley)+'x10 acres of barley, '+str(pset[i].oats)+'x10 acres of oats, '+str(pset[i].potatoes)+'x10 acres of pototatoes and '+str(pset[i].ley)+'x10 acres of ley.\n'
                i+=1
            #display text, button swap
            self.settxoutwithtx2(gui,3,tx,'\n')
            gui.btnswap(1)
        else:
            print('er card1')
    
class Card2(Cards,PaySeeds):
    title='SEED AND FARMYARD MANURE'
    cardnum=2
    cardfontcol='black'
    txmain='Seed. Purchase seeds for your clover leys on 30 acres for £100, which you pay to the bank. Purchase your seed potatoes at a cost of £15 for each acres which you are planting, and pay the money to the bank.\nFarmyard Manure. You require £10 worth of "F.Y.M." for each acre of root and potatoes that you are growing this year. Purchase this from the outgoing farmer, and pay the money to the bank.'
    txoutput=['Click the Advance button to pay your seed.',
              'Players have paid their seed:',
              'Click the Advance button to pay your farmyard manure costs.',
              'Players have paid their farmyard manure costs:',
              'Click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card2 fn'''
        #set inital text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pay seeds costs
        elif self.click==1:
            file('Pay seeds\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    #take costs
                    delta=pset[i].money
                    self.payseeds(pset[i],p=150)
                    self.takemoney(100,pset[i])
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £100 for seeds for clover leys and £'+str(delta-100)+' for seed potatoes.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #pay fym costs
        elif self.click==2:
            file('Pay fmy\n')
            tx=''
            i=0
            while i<var.pnum:
                if pset[i].ingame==1:
                    delta=pset[i].money
                    self.payseeds(pset[i],p=100)
                    self.takemoney(100,pset[i])
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for F.Y.M..\n'
                i+=1
            self.settxoutwithtx4(gui,3,tx,'\n','',4)
            #button swap
            gui.btnswap(1)
        else:
            print('er card2')

class Card3(Cards,AuctionSell,AuctionBuy):
    title='SPRING AUCTION'
    cardnum=3
    cardfontcol='black'
    txmain='Dealers are offering high prices for 1st-class dairy cattle. Farmers can each sell up to 5 cows if they want to for £65 each.\n\nSale of Stock, by Auction with Reserve:\n\t1: 1 cow, with reserve £65.\n\t2: 1 sow, with reserve £35.\n\t3: 2 cows, with reserve £130.\n\t4: 1 horse, with reserve £40.\n\t5: 1 cow, with reserve £65.'
    txoutput=['Click the Advance button to start the auction.',
              'The auction has ended, click the Advance button to start the next auction.',
              'The auction has ended and there is no more stock to sell. Click the Next Card button to continue.']
    tx=['up to 5','cows','£65 each']
    tx2=[[1,'cow',65],[1,'sow',35],[2,'cows',130],[1,'horse',40],[1,'cow',65]]
    
    def run(self,gui,var,pset,deck,file):
        '''Run card3 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up auction
        elif self.click==1:
            file('Set auction sell\n')
            skset=[pset[0].cows,pset[1].cows,pset[2].cows,pset[3].cows,pset[4].cows]
            self.setauctionsell(gui,self.tx,pset,skset,maxv=5)
        #get auction options
        elif self.click==2:
            file('Get auction sell\n')
            self.getauctionsell(gui,65,'cows',pset,0,self.tx)
        #auction end and start next 
        elif self.click==3:
            file('End auction sell\n')
            self.settxout(gui,1)
        #set up auction
        elif (self.click==4 or self.click==6 or self.click==8 or self.click==10 or self.click==12):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx2[int(self.click/2-2)],pset)
        #take auction options
        elif (self.click==5 or self.click==7 or self.click==9 or self.click==11 or self.click==13):
            file('Get auction buy\n')
            #a=self.tx2[int((self.click-1)/2-2)][1]
#            if a[-1]!='s':
#                a+='s'
                #self.tx2[int((self.click-1)/2-2)][1]=a
            self.getauctionbuy(gui,self.tx2[int((self.click-1)/2-2)][1],pset,self.tx2[int((self.click-1)/2-2)])
        #end auction
        elif self.click==14:
            file('End auction buy\n')
            self.settxout(gui,2)
            gui.btnswap(1)
        else:
            print('er card3')

class Card4(Cards,Dice):
    title='HAZARD: STOCK'
    cardnum=4
    cardfontcol='red'
    txmain='1: Sell 2 old cows for £70.\n2: Sell 2 fat cows for £80.\n3: Sell 1 old cow for £15.\n4: You lose a horse and get £1 for the carcase.\n5: You lose a sow with milk fever.\n6: Sell 1 barren heifer for £35.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Sell 2 old cow for £70.','Sell 2 fat cows for £80.','Sell 1 old cow for £15.','You lose a horse and get £1 for the carcase.','You lose a sow with milk fever.','Sell 1 barren heifer for £35.']
    dtype='stock'
    #num=[2,2,1,1,1,1]
    #money=[70,80,15,1,0,35]
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card4 fn'''
        self.tx=[[2,'cows',70],[2,'cows',80],[1,'cows',15],[1,'horses',1],[1,'sows',0],[1,'cows',35]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card4')
        
            
class Card5(Cards,Bills):
    title='PAY SUNDRY BILLS FOR JANUARY'
    cardnum=5
    cardfontcol='black'
    txmain='Wages and Sundries\nfor January ... £125'
    txoutput=['Click the Advance button to continue.',
              'Players have paid their bills for January, click the Next Card button to continue.']
    amount=125
    
    def run(self,gui,var,pset,deck,file):
        '''Run card5 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills and end card
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card5')
            
class Card6(Cards,Dice):
    title='HAZARD: SEVERE BLIZZARD AND FLOODS'
    cardnum=6
    cardfontcol='red'
    txmain='1: Floods sweep stacks away. To replace, pay £100.\n2: Floods sweep goods away. To replace, pay £60.\n3: Blizzard causes damage. To repair, pay £40.\n4: Blizzard causes damage. To repair, pay £30.\n5: Roads blocked. To clear, pay extra labour £20.\n6: Roads blocked. Pay for extra labour £10.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Floods sweep stacks away. To replace, pay £100.','Floods sweep goods away. To replace, pay £60.','Blizzard causes damage. To repair, pay £40.','Blizzard causes damage. To repair, pay £30.',' Roads blocked. To clear, pay extra labour £20.','Roads blocked. Pay for extra labour £10.']
    dtype='money'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card6 fn'''
        self.tx=[[1,'money',100],[1,'money',60],[1,'money',40],[1,'money',30],[1,'money',20],[1,'money',10]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card6')

class Card7(Cards,Dice):
    title='HAZARD: STOCK'
    cardnum=7
    cardfontcol='red'
    txmain='1: Sell 3 barren cows for £110.\n2: Sell 2 fat cows for £70.\n3: Sell 2 barren cow for £65.\n4: Sell 1 old cow for £10.\n5: You lose a horse with colic and get £1 for the carcase.\n6: You lose 1 sow.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Sell 3 barren cows for £110.','Sell 2 fat cows for £70.','Sell 2 barren cow for £65.','Sell 1 old cow for £10.','You lose a horse with colic and get £1 for the carcase.','You lose 1 sow.']
    dtype='stock'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card7 fn'''
        self.tx=[[3,'cows',110],[2,'cows',70],[2,'cows',65],[1,'cows',10],[1,'horses',1],[1,'sows',0]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card7')

class Card8(Cards,Milk,PaySeeds):
    title='JANUARY MILK: SEEDS'
    cardnum=8
    cardfontcol='black'
    txmain='January Milk. You receive from the Milk Marketing Board a payment for your January milk, which works out at £6 for each cow you own at this date.\n\nSeeds. Purchase the seed you require for the year for your wheat, oats, barley and root crops by paying £2 for each acre that you are sowing.'
    txoutput=['Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Advance button to buy your seeds.',
              'Players have paid for their seeds.',
              'Click the Next Card button to continue.']
    percow=6
    
    def run(self,gui,var,pset,deck,file):
        '''Run card8 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #pay seeds cost
        elif self.click==2:
            file('Pay Seeds\n')
            tx=''
            i=0
            while i<var.pnum:
                if pset[i].ingame==1:
                    delta=pset[i].money
                    self.payseeds(pset[i],w=20,b=20,o=20)
                    self.takemoney(20,pset[i])
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for seeds.\n'
                i+=1
            self.settxoutwithtx4(gui,3,tx,'\n','',4)
            #button swap
            gui.btnswap(1)
        else:
            print('er card8')

class Card9(Cards,Bills,AuctionBuy):
    title='FEBRUARY BILLS AND FARM STOCK SALE'
    cardnum=9
    cardfontcol='black'
    txmain='Pay Sundry Bills for February:\nWages and Sundries for February... £125\nLadybird Smallholding: Sale of Stock by Auction with Reserve.\n\t1: 2 cows, reserve price £135.\n\t2: 3 cows, reserve price £190.\n\t3: 1 sow, reserve price £35.\n\t4: 2 sows, reserve price £70.\n\t5: 1 horse, reserve price £35.'
    txoutput=['Click the Advance button to pay your bills.',
          'Players have paid their bills for February, click the Advance button to start the auction.',
          'The auction has ended and there is no more stock to sell. Click the Next Card button to continue.']
    amount=125
    
    def run(self,gui,var,pset,deck,file):
        '''Run card9 fn'''
        self.tx=[[2,'cows',135],[3,'cows',190],[1,'sow',35],[2,'sows',70],[1,'horse',35]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
        #set up auction
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx[int(self.click/2-1)],pset)
        #take auction options
        elif (self.click==3 or self.click==5 or self.click==7 or self.click==9 or self.click==11):
            file('Get auction buy\n')
            self.getauctionbuy(gui,self.tx[int((self.click-1)/2-1)][1],pset,self.tx[int((self.click-1)/2-1)])
        #end auction
        elif self.click==12:
            file('End auction buy\n')
            self.settxout(gui,2)
            gui.btnswap(1)
        else:
            print('er card9')

class Card10(Cards,Dice):
    title='HAZARD: SOWS\' SPRING FARROWING'
    cardnum=10
    cardfontcol='red'
    txmain='1: Neglect at farrowing results in yield of only 4 pigs per sow.\n2: Your sows have averaged 5 pigs each.\n3: Your sows have averaged 6 pigs each.\n4: Your sows have averaged 6 pigs each.\n5: Your sows have averaged 7 pigs each.\n6: Your average yield is 8 pigs per sow.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
           ' has no sows, click Advance to continue.']
    txdice=['Neglect at farrowing results in yield of only 4 pigs per sow.','Your sows have averaged 5 pigs each.','Your sows have averaged 6 pigs each.','Your sows have averaged 6 pigs each.','Your sows have averaged 7 pigs each.','Your average yield is 8 pigs per sow.']
    dtype='births'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card10 fn'''
        self.tx=[[4,'spigs',0],[5,'spigs',0],[6,'spigs',0],[6,'spigs',0],[7,'spigs',0],[8,'spigs',0]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice store pigs\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #player has 0 sows skip and state
                if pset[self.click-1].sows==0:
                    #set text
                    tx='Player '+pset[self.click-1].name
                    self.settxoutwithtx(gui,2,tx,' ')
                else:
                    #set up dice and take to dice roll
                    self.setdice(gui,var,pset[self.click-1])
                    #set to index for player in pset = click-1
                    self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card10')

class Card11(Cards,Milk,AuctionSell):
    title='FEBRUARY MILK: WEEKLY AUCTION'
    cardnum=11
    cardfontcol='black'
    txmain='February Milk. You receive from the Milk Marketing Board a payment for your February Milk which works out at £6 for each cow you own at this date.\nWeekly Auction. You can sell any of your piglets upon weaning for £3 each.'
    txoutput=['Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Advance button to start the auction.',
              'The auction has ended, click the Next Card button to continue.']
    percow=6
    tx=['any','store pigs','£3 each']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card11 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #set up auction
        elif self.click==2:
            file('Set auction sell\n')
            skset=[pset[0].spigs,pset[1].spigs,pset[2].spigs,pset[3].spigs,pset[4].spigs]
            self.setauctionsell(gui,self.tx,pset,skset,maxv=max(skset))
        #take auction options
        elif self.click==3:
            file('Get auction sell\n')
            self.getauctionsell(gui,3,'spigs',pset,0,self.tx)
        #auction end and start next 
        elif self.click==4:
            file('End auction sell\n')
            self.settxout(gui,3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card11')
    
class Card12(Cards,Dice):
    title='HAZARD: EWES LAMBING'
    cardnum=12
    cardfontcol='red'
    txmain='On average each of your ewes have 1 lamb each plus the following (excluding fractions):\n1: 1 in every 10 of your ewes have twins, and you lose 5 ewes.\n2: 1 in every 5 of your ewes have twins, and you lose 5 ewes.\n3: 3 in every 10 of your ewes have twins, and you lose 5 ewes.\n4: 2 in every 5 of your ewes have twins, and you lose 5 ewes.\n5: 2 in every 5 of your ewes have twins, without any loss.\n6: Half your ewes have twins, without any loss.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.','All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',' has no ewes, click Advance to continue.']
    txdice=['1 in every 10 of your ewes have twins, and you lose 5 ewes.','1 in every 5 of your ewes have twins, and you lose 5 ewes.','3 in every 10 of your ewes have twins, and you lose 5 ewes.','2 in every 5 of your ewes have twins, and you lose 5 ewes.','2 in every 5 of your ewes have twins, without any loss.','Half your ewes have twins, without any loss.']
    dtype='births'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card12 fn'''
        self.tx=[[1.1,'lambs',5],[1.2,'lambs',5],[1.3,'lambs',5],[1.4,'lambs',5],[1.4,'lambs',0],[1.5,'lambs',0]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice lambs\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #player has 0 sows skip and state
                if pset[self.click-1].ewes==0:
                    #set text
                    tx='Player '+pset[self.click-1].name
                    self.settxoutwithtx(gui,2,tx,' ')
                else:
                    #set up dice and take to dice roll
                    self.setdice(gui,var,pset[self.click-1])
                    #set to index for player in pset = click-1
                    self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card12')

class Card13(Cards,Bills,Milk):
    title='MARCH BILLS AND MILK YIELD'
    cardnum=13
    cardfontcol='black'
    txmain='Wages and Sundries for March... £250\n\nReceive from the Milk Marketing Board a payment for your March milk at £6 a cow and pay a corn bill of £3 a cow, which results in your receiving £3 nett for each cow you own at this date.'
    txoutput=['Click the Advance button to pay your bills.',
              'Players have paid their bills for March, click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Next Card button to continue.']
    amount=250
    percow=3
    
    def run(self,gui,var,pset,deck,file):
        '''Run card13 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills and end card
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
        #milk payment
        elif self.click==2:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,2,tx,'\n','',3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card13')

class Card14(Cards,Dice):
    title='HAZARD: DAIRY HERD'
    cardnum=14
    cardfontcol='red'
    txmain='1: Sell 3 old cows for £80.\n2: Sell 3 barren cows for £100.\n3: Sell 3 fat cows for £115.\n4: Sell 2 barren cows for £70.\n5: Sell 2 fat cows for £80.\n6: Sell 1 old cow for £20.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Sell 3 old cows for £80.','Sell 3 barren cows for £100.','Sell 3 fat cows for £115.','Sell 2 barren cows for £70.','Sell 2 fat cows for £80.','Sell 1 old cow for £20.']
    dtype='stock'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card14 fn'''
        self.tx=[[3,'cows',80],[3,'cows',100],[3,'cows',115],[2,'cows',70],[2,'cows',80],[1,'cows',20]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card14')

class Card15(Cards,Dice):
    title='HAZARD: ADMINISTRATION'
    cardnum=15
    cardfontcol='red'
    txmain='1: Tractor gets damaged. Repairs cost £80.\n2: Tractor overhaul. Pay £70.\n3: Purchase replacement implements for £60.\n4: Gale takes roof off greenhouse. Replacement costs £50.\n5: Replacement sheep troughs cost £40.\n6: Replacement sheep racks cost £30.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Tractor gets damaged. Repairs cost £80.','Tractor overhaul. Pay £70.','Purchase replacement implements for £60.','Gale takes roof off greenhouse. Replacement costs £50.','Replacement sheep troughs cost £40.','Replacement sheep racks cost £30.']
    dtype='money'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card15 fn'''
        self.tx=[[1,'money',80],[1,'money',70],[1,'money',60],[1,'money',50],[1,'money',40],[1,'money',30]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card15')

class Card16(Cards,AuctionBuy):
    title='TREE TOPS FARM SALE'
    cardnum=16
    cardfontcol='black'
    txmain='Stock sold by auction with reserve\n\t1: 2 cows, reserve price £120.\n\t2: 1 horse, reserve price £40.\n\t3: 2 sows, reserve price £40.\n\t4: 3 cows, reserve price £185.\n\t5: 10 store pigs, reserve price £30.'
    txoutput=['Click the Advance button to start the auction.',
              'The auction has ended and there is no more stock to buy, click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card16 fn'''
        self.tx=[[2,'cows',120],[1,'horse',40],[2,'sows',40],[3,'cows',185],[10,'store pigs',30]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up auction
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx[int((self.click-1)/2)],pset)
        #take auction options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('Get auction buy\n')
            self.getauctionbuy(gui,self.tx[int(self.click/2-1)][1],pset,self.tx[int(self.click/2-1)])
        #end auction
        elif self.click==11:
            file('End auction buy\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card16')

class Card17(Cards,Bills,CornBills):
    title='APRIL BILLS: QUARTER\'S BILLS'
    cardnum=17
    cardfontcol='black'
    txmain='Pay your April Bills:\nWages and Sundries for April... £150.\n\nPay your corn bills for the 1st quarter of the year, computated as follows:\n£3 for each store pig you own and £1 for each horse, sow and ewe you own.'
    txoutput=['Click the Advance button to pay your bills.',
              'Players have paid their bills for April, click the Advance button to pay your corn bills.',
              'Players have paid their corn bills.',
              'Click the Next Card button to continue.']
    amount=150
    
    def run(self,gui,var,pset,deck,file):
        '''Run card17 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
        #corn bills
        elif self.click==2:
            file('Corn bills\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #corn bill payment
                    delta=pset[i].money
                    self.cornbills(pset[i],sp=3,h=1,s=1,e=1)
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for their corn bills.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,2,tx,'\n','',3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card17')

class Card18(Cards,Dice):
    title='HAZARD: SPRING CALVES'
    cardnum=18
    cardfontcol='red'
    txmain='Your herd has now had all its spring calves and the number of cows calving is just half your herd (excluding fractions). You loose the following number of calves and then apply the corresponding result (exculde fractions from the final result).\n1: You loose 4 calves. You have half minus 1 of your calves as heifer calves and the rest are bull claves.\n2: You loose 3 calves. You have half minus 0.5 of your calves as heifer calves and the rest are bull calves.\n3: You loose 0 calves. You have half of your calves as heifer calves and the rest are bull calves.\n4: You loose 0 calves. You have half of your calves as bull calves and the rest are heifer calves.\n5: You loose 1 calf. You have half minus 0.5 of your calves as bull calves and the rest are heifer calves.\n6: You loose 2 calves. You have half minus 1 of your calves as bull calves and the rest are heifer calves.'
    #'Half your calves are heifer calves +/- the following result and the rest are bull calves.\n1: Minus 2 heifer calves to the result.   2: Minus 1 heifer calves to the result.   3: No modification to the result.\n4: No modification to the result.\t5: Plus 1 heifer calves to the result.\t6: Plus 2 heifer calves to the result.\nRoll the dice to determine calves losses.\n1: You lose 4 calves.\t2: You lose 3 calves.\t3: You lose 2 claves.\n4: You lose 1 calf.\t5: You lose no calves.\t6: You lose no calves.\nRoll the dice (if required) to see which calves are loss. (Round results accordingly).\n1: You lose all bull calves.\t2: You lose 25% bull calves and the rest heifer calves.\n3: You lose 50% bull calves and the rest are heifer calves.\t4: You lose 50% heifer calves the rest are bull claves.\n5: You lose 75% bull calves and the rest are heifer calves.\t6: You lose all heifer calves.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
           ' has no cows, click Advance to continue.']
    txdice=['You loose 4 calves. You have half minus 1 of your calves as heifer calves and the rest are bull claves.','You loose 3 calves. You have half minus 0.5 of your calves as heifer calves and the rest are bull calves.','You loose 0 calves. You have half of your calves as heifer calves and the rest are bull calves.','You loose 0 calves. You have half of your calves as bull calves and the rest are heifer calves.','You loose 1 calf. You have half minus 0.5 of your calves as bull calves and the rest are heifer calves.','You loose 2 calves. You have half minus 1 of your calves as bull calves and the rest are heifer calves.']
    dtype='births'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card18 fn'''
        self.tx=[[1,'hcalves',4],[0.5,'hcalves',3],[0,'hcalves',0],[0,'hcalves',0],[0.5,'hcalves',1],[1,'hcalves',2]]
    #self.tx2=[[1.1,'bcalves',5],[1.2,'bcalves',5],[1.3,'bcalves',5],[1.4,'bcalves',5],[1.4,'bcalves',0],[1.5,'bcalves',0]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice calves\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #player has 0 cows skip and state
                if pset[self.click-1].cows==0:
                    #set text
                    tx='Player '+pset[self.click-1].name
                    self.settxoutwithtx(gui,2,tx,' ')
                else:
                    #set up dice and take to dice roll
                    self.setdice(gui,var,pset[self.click-1])
                    #set to index for player in pset = click-1
                    self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card18')

class Card19(Cards,Dice):
    title='HAZARD: GROWING CROPS'
    cardnum=19
    cardfontcol='red'
    txmain='1: Drought. Resowing roots and seeds costs £80.\n2: Drought. Resowing corn crops costs £70.\n3: Extra labour required for fruit and potato crops. Pay £60.\n4: Resowing poor corn crops costs £50.\n5: Turnip fly attacks roots. Resowing costs £40.\n6: Extra basic slag for poor pastures costs £30.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.','All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Drought. Resowing roots and seeds costs £80.','Drought. Resowing corn crops costs £70.','Extra labour required for fruit and potato crops. Pay £60.','Resowing poor corn crops costs £50.','Turnip fly attacks roots. Resowing costs £40.','Extra basic slag for poor pastures costs £30.']
    dtype='money'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card19 fn'''
        self.tx=[[1,'money',80],[1,'money',70],[1,'money',60],[1,'money',50],[1,'money',40],[1,'money',30]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card19')

class Card20(Cards,Milk,Wool):
    title='APRIL MILK YIELD: WOOL CLIP'
    cardnum=20
    cardfontcol='black'
    txmain='You receive from the Milk Marketing Board a payment for your April milk, which works out at £6 for each cow that you own at this date.\n\nWool Clip. You receive £6 for every 5 ewes, for your flock\'s wool clip.'
    txoutput=['Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Advance button to receive your wool clip payment.',
              'Players have received their money from their flock\'s wool.',
              'Click the Next Card button to continue']
    percow=6
    
    def run(self,gui,var,pset,deck,file):
        '''Run card20 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #wool
        elif self.click==2:
            #wool payment
            tx2=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #wool payment
                    delta2=pset[i].money
                    self.paywool(pset[i],pset[i].ewes)
                    delta2=pset[i].money-delta2
                    tx2=tx2+'Player '+pset[i].name+' has recieved £'+str(delta2)+' for their wool.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,3,tx2,'\n','',4)
            #button swap
            gui.btnswap(1)
        else:
            print('er card20')

class Card21(Cards,AuctionSell):
    title='STOCK AUCTION'
    cardnum=21
    cardfontcol='black'
    txmain='Prices for store stock are keen and if you want to:-\n\tYou can sell 12 bull calves for £40.\n\tYou can sell 10 heifer calves for £50.\n\tYou can sell store pigs for £7 each.\n\tYou can sell 10 poor doing ewes with their 15 lambs for £85.'
    txoutput=['Click the Advance button to start the auction.',
              'The auction has ended, click the Next Card button to continue.']
    tx=['12','bull calves','£40']
    tx2=['10','heifer calves','£50']
    tx3=['any','store pigs','£7 each']
    tx4=['10 and 15','ewes and lambs respectfully','£85']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card21 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up auction
        elif self.click==1:
            file('Set auction sell\n')
            skset=[pset[0].bcalves,pset[1].bcalves,pset[2].bcalves,pset[3].bcalves,pset[4].bcalves]
            self.setauctionsell(gui,self.tx,pset,skset,maxv=12,inc=12)
        #take auction options
        elif self.click==2:
            file('Get auction sell\n')
            self.getauctionsell(gui,40,'bcalves',pset,1,self.tx)
        #set up auction
        elif self.click==3:
            file('Set auction sell\n')
            skset=[pset[0].hcalves,pset[1].hcalves,pset[2].hcalves,pset[3].hcalves,pset[4].hcalves]
            self.setauctionsell(gui,self.tx2,pset,skset,maxv=10,inc=10)
        #take auction options
        elif self.click==4:
            file('Get auction sell\n')
            self.getauctionsell(gui,50,'hcalves',pset,1,self.tx2)
        #set up auction
        elif self.click==5:
            file('Set auction sell\n')
            skset=[pset[0].spigs,pset[1].spigs,pset[2].spigs,pset[3].spigs,pset[4].spigs]
            self.setauctionsell(gui,self.tx3,pset,skset,maxv=160,inc=1)
        #take auction options
        elif self.click==6:
            file('Get auction sell\n')
            self.getauctionsell(gui,7,'spigs',pset,0,self.tx3)
        #set up auction
        elif self.click==7:
            file('Set auction sell\n')
            skset=self.auctionsellmulti(var,pset,'ewes','lambs',10,15)
            self.setauctionsell(gui,self.tx4,pset,skset,maxv=35,inc=35)
        #take auction options
        elif self.click==8:
            file('Get auction sell\n')
            self.getauctionsell(gui,85,'multi1',pset,1,self.tx4)
        #auction end
        elif self.click==9:
            file('End auction sell\n')
            self.settxout(gui,1)
            #button swap
            gui.btnswap(1)
        else:
            print('er card21')
    

class Card22(Cards,Bills):
    title='PAY SUNDRY BILLS FOR MAY'
    cardnum=22
    cardfontcol='black'
    txmain='Wages and Sundries\nfor May ... £175'
    txoutput=['Click the Advance button to continue.',
              'Players have paid their bills for May, click the Next Card button to continue.']
    amount=175
    
    def run(self,gui,var,pset,deck,file):
        '''Run card22 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills and end card
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card22')

class Card23(Cards,Dice):
    title='HAZARD: STOCK'
    cardnum=23
    cardfontcol='red'
    txmain='1: Sell 4 fat cows for £140.\n2: Sell 3 barren cows for £90.\n3: Sell 3 fat cows for £110.\n4: Sell 2 fat cows for £65.\n5: You lose 1 cow and receive £1 for the carcase.\n6: If you have less than 2 horses, buy a prize gelding for £100.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Sell 4 fat cows for £140.','Sell 3 barren cows for £90.','Sell 3 fat cows for £110.','Sell 2 fat cows for £65.','You lose 1 cow and receive £1 for the carcase.','If you have less than 2 horses, buy a prize gelding for £100.']
    dtype='stock'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card23 fn'''
        self.tx=[[4,'cows',140],[3,'cows',90],[3,'cows',110],[2,'cows',65],[1,'cows',1],[0,'moneyhorse',-100]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card23')

class Card24(Cards,Milk):
    title='MAY MILK YIELD'
    cardnum=24
    cardfontcol='black'
    txmain='You receive from the Milk Marketing Board a payment for your May milk, which works out at £4 for each cow that you own at this date, less a deduction of £3 for every calf you own at this date, because if you use milk to rear calves you have that much less to sell to the Milk Board.'
    txoutput=['Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Next Card button to continue']
    percow=4
    percalf=3
    
    def run(self,gui,var,pset,deck,file):
        '''Run card24 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows,self.percalf,pset[i].bcalves,pset[i].hcalves)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
            #button swap
            gui.btnswap(1)
        else:
            print('er card24')

class Card25(Cards,Dice):
    title='HAZARD: HAY HARVEST'
    cardnum=25
    cardfontcol='red'
    txmain='1: Weather spoils 20 acres of hay. Buy 20 tonnes of hay to replace it for £200.\n2: Bad weather spoils hay. Replacement costs £125.\n3: Bad weather spoils hay. Replacement costs £90.\n4: Poor weather causes extra haymaking. Pay £75.\n5: Poor weather causes extra haymaking. Pay £60.\n6: Well got harvest. Pay overtime £40.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Weather spoils 20 acres of hay. Buy 20 tonnes of hay to replace it for £200.','Bad weather spoils hay. Replacement costs £125.','Bad weather spoils hay. Replacement costs £90.','Poor weather causes extra haymaking. Pay £75.','Poor weather causes extra haymaking. Pay £60.','Well got harvest. Pay overtime £40.']
    dtype='money'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card25 fn'''
        self.tx=[[1,'money',200],[1,'money',125],[1,'money',90],[1,'money',75],[1,'money',60],[1,'money',40]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card25')

class Card26(Cards,Dice):
    title='HAZARD: SICKNESS IN STOCK'
    cardnum=26
    cardfontcol='red'
    txmain='1: You lose 2 cows with fever and get £2 for the carcases.\n2: You lose 2 cows with pneumonia and get £2 for the carcases.\n3: You have 2 cows with garget, and they sell for £30 the pair.\n4: You lose a cow with milk fever and get £1 for the carcase.\n5: You lose a horse with fever and get £1 for the carcase.\n6: Your calves are developing ringworm so sell them all for £5 each.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['You lose 2 cows with fever and get £2 for the carcases.','You lose 2 cows with pneumonia and get £2 for the carcases.','You have 2 cows with garget, and they sell for £30 the pair.','You lose a cow with milk fever and get £1 for the carcase.','You lose a horse with fever and get £1 for the carcase.','Your calves are developing ringworm so sell them all for £5 each.']
    dtype='stock'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card26 fn'''
        self.tx=[[2,'cows',2],[2,'cows',2],[2,'cows',30],[1,'cows',1],[1,'horses',1],[0,'calves',5]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #add hcavles
                self.tx[5][0]=pset[self.click-1].hcalves
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card26')

class Card27(Cards,Bills,CornBills):
    title='JUNE BILLS AND QUARTER\'S BILLS'
    cardnum=27
    cardfontcol='black'
    txmain='Pay Wages and Sundries\nfor June... £200\n\nPay your Corn Bills for the 2nd quarter of the year computated as follows:-\n£2 for each store pig you own, and £1 for each sow you own.'
    txoutput=['Click the Advance button to pay your bills.',
           'Players have paid their bills for June, click the Advance button to pay your corn bills.',
           'Players have paid their corn bills.',
           'Click the Next Card button to continue.']
    amount=200
    
    def run(self,gui,var,pset,deck,file):
        '''Run card27 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
        #corn bills
        elif self.click==2:
            file('Corn bills\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #corn bill payment
                    delta=pset[i].money
                    self.cornbills(pset[i],sp=2,s=1)
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for their corn bills.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,2,tx,'\n','',3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card27')

class Card28(Cards,AuctionBuy):
    title='BUTTERMILK FARM SALE'
    cardnum=28
    cardfontcol='black'
    txmain='Stock sold by Auction with reserve\n\t1: 2 sows, reserve price £50.\n\t2: 2 cows, reserve price £125.\n\t3: 10 ewes, reserve price £35.\n\t4: 3 cows, reserve price £185.\n\t5: 10 bulls calves, reserve price £45.'
    txoutput=['Click the Advance button to start the auction.',
              'The auction has ended and there is no more stock to buy, click the Next Card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card28 fn'''
        self.tx=[[2,'sows',50],[2,'cows',125],[10,'ewes',35],[3,'cows',185],[10,'bull calves',45]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up auction
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx[int((self.click-1)/2)],pset)
        #take auction options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('Get auction buy\n')
            self.getauctionbuy(gui,self.tx[int(self.click/2-1)][1],pset,self.tx[int(self.click/2-1)])
        #end auction
        elif self.click==11:
            file('End auction buy\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card28')

class Card29(Cards,Milk,Bills):
    title='JUNE MILK: JULY BILLS'
    cardnum=29
    cardfontcol='black'
    txmain='You receive from the Milk Marketing Board a payment for your June Milk, which works out at £4 a cow, and you pay a corn bill of £1 per cow, which results in you receiving £3 nett for each cow that you own at this date.\n\nPay Wages and Sundries for July... £200'
    txoutput=['Click the Advance button to receive your milk payment.',
           'Players have been paid by the Milk Marketing Board.',
           'Click the Advance button to pay your bills.',
           'Players have paid their bills for July, click the Next Card button to continue.']
    amount=200
    percow=3
    
    def run(self,gui,var,pset,deck,file):
        '''Run card29 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #pays bills and end card
        elif self.click==2:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card29')

class Card30(Cards,Dice,Milk):
    title='HAZARD: HARVEST, & JULY MILK'
    cardnum=30
    cardfontcol='red'
    txmain='1: Tractor damaged. Repairs cost £100.\n2: Exchange your baler for a newer one. Pay £90.\n3: Tractor seizes up. Repairs cost £75.\n4: Buy new trailer for £60.\n5: A horse dies. You get £1 for the carcase.\n6: If you have less than 2 horses rent another tractor for £200.\n\nYou receive from the Milk Marketing Board a payment for your July milk which works out at £4 for each cow that you own at this date.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Next Card button to continue.']
    txdice=['Tractor damaged. Repairs cost £100.','Exchange your baler for a newer one. Pay £90.','Tractor seizes up. Repairs cost £75.','Buy new trailer for £60.','A horse dies. You get £1 for the carcase.','If you have less than 2 horses rent another tractor for £200.']
    dtype='stock'
    pnum=0 #required for dice roll
    percow=4
    
    def run(self,gui,var,pset,deck,file):
        '''Run card30 fn'''
        self.tx=[[1,'money',100],[1,'money',90],[1,'money',75],[1,'money',60],[1,'horses',1],[0,'moneyhorse',-200]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end dice
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
        #milk payment
        elif self.click==7:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,2,tx,'\n','',3)
            #end card
        #elif self.click==8:
            gui.btnswap(1)
        else:
            print('er card30')

class Card31(Cards,Sale,AuctionSell):
    title='FLOCK CONSERVANCY: SUMMER AUCTION'
    cardnum=31
    cardfontcol='black'
    txmain='You must sell your 20 poorest ewes to make room for replacements to keep your flock up to standard. You receive up to £60 for them.\n\nSell all your heifer calves for £10 each.\nSell all your bull calves for £7 each.\nSell any lambs you like at £16 for a pen of 5.\nSell any horses you like for £35 each.'
    txoutput=['Click the Advance button to sell your ewes.',
           'Players have sold their ewes.',
           'Click the Advance button to sell your heifer calves.',
           'Players have sold their heifer calves.',
           'Click the Advance button to sell your bull calves.',
           'Players have sold their bull calves.',
           'Click the Advance button to continue.',
           'The auction has ended, click the Next Card button to continue.']
    tx=['pens of 5','lambs','£16 each']
    tx2=['any','horses','£35']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card31 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #sell stock- ewes
        elif self.click==1:
            file('Comp sale\n')
            i=0
            tx=''
            while i<var.pnum:
                if pset[i].ingame==1:
                    self.compsale(20,60,'ewes',pset[i],1)
                    tx=tx+self.zerostock(20,60,'ewes',pset[i])
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'','\n',2)
        #sell hc
        elif self.click==2:
            file('Comp sale\n')
            i=0
            tx=''
            while i<var.pnum:
                if pset[i].ingame==1:
                    delta=pset[i].money
                    self.compsale(pset[i].hcalves,10,'hcalves',pset[i],0)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their heifer calves.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,3,tx,'\n','',4)
        #sell bc
        elif self.click==3:
            file('Comp sale\n')
            i=0
            tx=''
            while i<var.pnum:
                if pset[i].ingame==1:
                    delta=pset[i].money
                    self.compsale(pset[i].bcalves,7,'bcalves',pset[i],0)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their bull calves.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,5,tx,'\n','',6)
        #set up auction
        elif self.click==4:
            file('Set auction sell')
            skset=[pset[0].lambs,pset[1].lambs,pset[2].lambs,pset[3].lambs,pset[4].lambs]
            self.setauctionsell(gui,self.tx,pset,skset,maxv=90,inc=5)
        #take auction options
        elif self.click==5:
            file('Get auction sell')
            self.getauctionsell(gui,16/5,'lambs',pset,0,self.tx)
        #set up auction
        elif self.click==6:
            file('Set auction sell')
            skset=[pset[0].horses,pset[1].horses,pset[2].horses,pset[3].horses,pset[4].horses]
            self.setauctionsell(gui,self.tx2,pset,skset,maxv=4,inc=1)
        #take auction options
        elif self.click==7:
            file('Get auction sell')
            self.getauctionsell(gui,35,'horses',pset,0,self.tx2)
        #auction end
        elif self.click==8:
            file('End auction sell\n')
            self.settxout(gui,7)
            #button swap
            gui.btnswap(1)
        else:
            print('er card31')
    

class Card32(Cards,Drought):
    title='DROUGHT'
    cardnum=32
    cardfontcol='black'
    txmain='Severe drought leaves your pastures bare and they cannot carry their usual amount of stock. Take 1 acre for each horse and cow you own, and take 1/2 an acre for each ewe and lamb you own. Should the total exceed 90 acres, rent an autumn ley of 10 acres for £50; and if the total exceeds 100 acres, rent an autumn ley of 20 for £100 instead.'
    txoutput=['Click the Advance button to continue',
             'Players have experianced drought:',
           'Click the Next card button to continue.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card32 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #drought
        elif self.click==1:
            file('Drought\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    #delta=pset[i].money
                    tot,txout=self.drought(pset[i].cows,pset[i].horses,pset[i].ewes,pset[i].lambs,pset[i])
                    #delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' needs '+str(tot)+txout
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
            #button swap
            gui.btnswap(1)
        else:
            print('er card32')

class Card33(Cards,Bills,AuctionBuy):
    title='AUGUST BILLS: SUMMER AUCTION'
    cardnum=33
    cardfontcol='black'
    txmain='Pay your bills for August:\nWages and Sundries for August... £200\n\nAuction. Sale of stock with reserve:\n\t1: 2 cows, reserve price £120.\n\t2: 2 sows, reserve price £55.\n\t3: 3 cows, reserve price £185.\n\t4: 2 cows, reserve price £125.'
    txoutput=['Click the Advance button to pay your bills.',
              'Players have paid their bills for August, click the Advance button to start the auction.',
              'The auction has ended and there is no more stock to sell. Click the Next Card button to continue.']
    amount=200
    
    def run(self,gui,var,pset,deck,file):
        '''Run card33 fn'''
        self.tx=[[2,'cows',120],[2,'sows',55],[3,'cows',185],[2,'cows',125]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pays bills
        elif self.click==1:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,1)
        #set up auction
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx[int(self.click/2-1)],pset)
        #take auction options
        elif (self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Get auction buy\n')
            self.getauctionbuy(gui,self.tx[int((self.click-1)/2-1)][1],pset,self.tx[int((self.click-1)/2-1)])
        #end auction
        elif self.click==10:
            file('End auction buy\n')
            self.settxout(gui,2)
            gui.btnswap(1)
        else:
            print('er card33')

class Card34(Cards,Dice):
    title='HAZARD: SOFT FRUIT YIELD'
    cardnum=34
    cardfontcol='red'
    txmain='1: Poor crops. Picking costs exceeds yield. Pay £10.\n2: Poor crops owing to late frosts, Receive £10.\n3: Good crops with poor prices. Receive £25.\n4: Glut of fruit. Poor prices yield £30.\n5: Poor crop. High prices yield £50.\n6: Moderate crop with high prices yields £100.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['Poor crops. Picking costs exceeds yield. Pay £10.','Poor crops owing to late frosts, Receive £10.','Good crops with poor prices. Receive £25.','Glut of fruit. Poor prices yield £30.','Poor crop. High prices yield £50.','Moderate crop with high prices yields £100.']
    dtype='crops'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card34 fn'''
        self.tx=[[1,'money',-10],[1,'money',10],[1,'money',25],[1,'money',30],[1,'money',50],[1,'money',100]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card34')

class Card35(Cards,Dice):
    title='HAZARD: CORN HARVEST'
    cardnum=35
    cardfontcol='red'
    txmain='1: 1 of your fields of corn is spoilt by continual rain. Hand in a card representing a 10 acre field of corn (oats, wheat or barley).\n2: Baler breaks down. Purchase a replacement for £150.\n3: Corn beaten down by rain, results in slow harvest and extra overtime. Pay £100.\n4: Bad weather results in costly, slow harvest. Pay £75.\n5: Good harvest. Pay overtime £50.\n6: Fine weather result in excellent harvest. Pay overtime £25.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.']
    txdice=['1 of your fields of corn is spoilt by continual rain. Hand in a card representing a 10 acre field of corn (oats, wheat or barley).','Baler breaks down. Purchase a replacement for £150.','Corn beaten down by rain, results in slow harvest and extra overtime. Pay £100.','Bad weather results in costly, slow harvest. Pay £75.','Good harvest. Pay overtime £50.','Fine weather result in excellent harvest. Pay overtime £25.']
    txdice2=['Please pick the corn crop you want to lose.',
              ' has no crops so cannot lose 10 acres of corn.\nClick the Advance button to continue.',
              ' you\'ve lost 10 acres of wheat.\nClick the Advance button to continue.',
              ' you\'ve lost 10 acres of barley.\nClick the Advance button to continue.',
              ' you\'ve lost 10 acres of oats.\nClick the Advance button to continue.',
              'Invalid entry, please re-enter your value.']
    dtype='money'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card35 fn'''
        self.tx=[[1,'cropm',0],[1,'money',150],[1,'money',100],[1,'money',75],[1,'money',50],[1,'money',25]]
        self.tx2=[[1,'crop',0],[0,'crop',0]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #set up dice and take to dice roll
                self.setdice(gui,var,pset[self.click-1])
                #set to index for player in pset = click-1
                self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        #roll choice- pick crop to loose
        elif self.click>6 and self.click<12:
            file('Roll choice\n')
            self.rollchoice(gui,var,self.txdice2,self.tx2,pset,self.click-7,file)
        else:
            print('er card35')

class Card36(Cards,Milk,Bills,CornBills):
    title='AUGUST MILK YIELD: SEPTEMBER BILLS AND CORN BILLS'
    cardnum=36
    cardfontcol='black'
    txmain='You receive from the Milk Marketing Board a payment for your August milk, which works out at £5 for each cow that you own at this date.\nPay your September bills:\nWages and Sundries for September... £350\nPay your corn bills for the quarter, computated as follow:-\n£3 for each store pigs you own, and £1 for each sow and lamb you own.'
    txoutput=['Click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Advance button to pay your bills.',
              'Players have paid their bills for September, click the Advance button to pay your corn bills.',
              'Players have paid their corn bills.',
              'Click the Next Card button to continue.']
    amount=350
    percow=5
    
    def run(self,gui,var,pset,deck,file):
        '''Run card36 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #milk payment
        elif self.click==1:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #pays bills
        elif self.click==2:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,3)
        #corn bills
        elif self.click==3:
            file('Corn bills\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #corn bill payment
                    delta=pset[i].money
                    self.cornbills(pset[i],sp=3,s=1,l=1)
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for their corn bills.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,4,tx,'\n','',5)
            #button swap
            gui.btnswap(1)
        else:
            print('er card36')

class Card37(Cards,AuctionBuy,Milk):
    title='SHEEP SALE: SEPTEMBER MILK'
    cardnum=37
    cardfontcol='black'
    txmain='Sold by auction with reserve:\n\t1: 10 ewes, reserve price £35.\n\t2: 20 ewes, reserve price £65.\n\t3: 10 ewes, reserve price £35.\n\t4: 20 ewes, reserve price £65.\n\t5: 10 ewes, reserve price £30.\n\nYou receive from the Milk Marketing Board a payment for your September milk which works out at £5 per cow and you pay a corn bill of £1 per cow, which results in you receiving a nett payment of £4 for each cow that you own at this date.'
    txoutput=['Click the Advance button to start the auction.',
              'The auction has ended and there is no more stock to buy, click the Advance button to receive your milk payment.',
              'Players have been paid by the Milk Marketing Board.',
              'Click the Next Card button to continue']
    percow=4
    
    def run(self,gui,var,pset,deck,file):
        '''Run card37 fn'''
        self.tx=[[10,'ewes',35],[20,'ewes',65],[10,'ewes',35],[20,'ewes',65],[10,'ewes',30]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set up auction
        elif (self.click==1 or self.click==3 or self.click==5 or self.click==7 or self.click==9):
            file('Set auction buy\n')
            self.setauctionbuy(gui,self.tx[int((self.click-1)/2)],pset)
        #take auction options
        elif (self.click==2 or self.click==4 or self.click==6 or self.click==8 or self.click==10):
            file('Get auction buy\n')
            self.getauctionbuy(gui,self.tx[int(self.click/2-1)][1],pset,self.tx[int(self.click/2-1)])
        #end auction
        elif self.click==11:
            file('End auction buy\n')
            self.settxout(gui,1)
            
        #milk payment
        elif self.click==12:
            file('Milk\n')
            #loop for each player
            tx=''
            i=0
            while i<var.pnum:
                #only if player in game
                if pset[i].ingame==1:
                    #milk payment
                    delta=pset[i].money
                    self.milk(pset[i],self.percow,pset[i].cows)
                    delta=pset[i].money-delta
                    tx=tx+'Player '+pset[i].name+' has recieved £'+str(delta)+' for their milk.\n'
                i+=1
            #set text
            self.settxoutwithtx4(gui,2,tx,'\n','',3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card37')

class Card38(Cards,Dice):
    title='HAZARD: WHEAT CROP RESULT'
    cardnum=38
    cardfontcol='red'
    txmain='Your wheat has now been harvested and sells at £1 per 50kg and the straw sells at £2 per acre, this result is calculated below.\n\n1: 865kg to the acre. Receive £190 for each 10 acre field of wheat.\n2: 865kg to the acre. Receive £190 for each 10 acre field of wheat.\n3: 900kg to the acre. Receive £200 for each 10 acre field of wheat.\n4: 900kg to the acre. Receive £200 for each 10 acre field of wheat.\n5: 950kg to the acre. Receive £210 for each 10 acre field of wheat.\n6: 1000kg to the acre. Receive £220 for each 10 acre field of wheat.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
              'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
              ' has no wheat, click Advance to continue.']
    txdice=['865kg to the acre. Receive £190 for each 10 acre field of wheat.','865kg to the acre. Receive £190 for each 10 acre field of wheat.','900kg to the acre. Receive £200 for each 10 acre field of wheat.','900kg to the acre. Receive £200 for each 10 acre field of wheat.','950kg to the acre. Receive £210 for each 10 acre field of wheat.','1000kg to the acre. Receive £220 for each 10 acre field of wheat.']
    dtype='crops'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card38 fn'''
        self.tx=[[0,'wheat',190],[0,'wheat',190],[0,'wheat',200],[0,'wheat',200],[0,'wheat',210],[0,'wheat',220]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #test for wheat
                if pset[self.click-1].wheat==0:
                    self.settxoutwithtx(gui,2,pset[self.click-1].name,'')
                else:
                    #add wheat
                    i=0
                    while i<6:
                        self.tx[i][0]=pset[self.click-1].wheat
                        i+=1
                    #set up dice and take to dice roll
                    self.setdice(gui,var,pset[self.click-1])
                    #set to index for player in pset = click-1
                    self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card38')

class Card39(Cards,PaySeeds,Bills):
    title='POTATO PICKING: OCTOBER BILLS'
    cardnum=39
    cardfontcol='black'
    txmain='Pay extra labour for potato picking, computated at £50 for each 10 acre field that you have to harvest.\n\nPay your October bills as follows:\nWages and Sundries for October... £600'
    txoutput=['Click the Advance button to pay your potato picking costs.',
              'Players have paid their potato picking.',
              'Click the Advance button to pay your bills.',
              'Players have paid their bills for October, click the Next Card button to continue.']
    amount=600
    
    def run(self,gui,var,pset,deck,file):
        '''Run card39 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #pay seeds cost
        elif self.click==1:
            file('Pay Seeds\n')
            tx=''
            i=0
            while i<var.pnum:
                if pset[i].ingame==1:
                    delta=pset[i].money
                    self.payseeds(pset[i],p=50)
                    delta=delta-pset[i].money
                    tx=tx+'Player '+pset[i].name+' has paid £'+str(delta)+' for potato picking.\n'
                i+=1
            self.settxoutwithtx4(gui,1,tx,'\n','',2)
        #pays bills and end card
        elif self.click==2:
            file('Pay bills\n')
            #bills
            i=0
            while i<var.pnum:
                #take only if player in game
                if pset[i].ingame==1:
                    self.paybills(pset[i],self.amount)
                i+=1
            #set text
            self.settxout(gui,3)
            #button swap
            gui.btnswap(1)
        else:
            print('er card39')

class Card40(Cards,Dice):
    title='HAZARD: OATS CROP RESULT'
    cardnum=40
    cardfontcol='red'
    txmain='Your oats have now been harvested and sell at £16 per tonne. You keep the straw for fodder, this result is calculated below.\n\n1: 1250kg to the acre. Receive £200 for each 10 acre field of oats.\n2: 1300kg to the acre. Receive £210 for each 10 acre field of oats.\n3: 1350kg to the acre. Receive £220 for each 10 acre field of oats.\n4: 1400kg to the acre. Receive £225 for each 10 acre field of oats.\n5: 1450kg to the acre. Receive £230 for each 10 acre field of oats.\n6: 1500kg to the acre. Receive £240 for each 10 acre field of oats.'
    txoutput=['Players in turn must roll the dice and apply the corresponding result. Click the Advance button to begin.',
           'All Players have rolled the dice and the results have been applied. Click the Next Card button to continue.',
           ' has no oats, click Advance to continue.']
    txdice=['1250kg to the acre. Receive £200 for each 10 acre field of oats.','1300kg to the acre. Receive £210 for each 10 acre field of oats.','1350kg to the acre. Receive £220 for each 10 acre field of oats.','1400kg to the acre. Receive £225 for each 10 acre field of oats.','1450kg to the acre. Receive £230 for each 10 acre field of oats.','1500kg to the acre. Receive £240 for each 10 acre field of oats.']
    dtype='crops'
    pnum=0 #required for dice roll
    
    def run(self,gui,var,pset,deck,file):
        '''Run card40 fn'''
        self.tx=[[0,'oats',200],[0,'oats',210],[0,'oats',220],[0,'oats',225],[0,'oats',230],[0,'oats',240]]
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #set dice up (roll is via button- outside this fn)
        elif self.click>0 and self.click<6:
            file('Set dice\n')
            #allow roll if player in game
            if pset[self.click-1].ingame==1:
                #test for oats
                if pset[self.click-1].oats==0:
                    self.settxoutwithtx(gui,2,pset[self.click-1].name,'')
                else:
                    #add oats
                    i=0
                    while i<6:
                        self.tx[i][0]=pset[self.click-1].oats
                        i+=1
                    #set up dice and take to dice roll
                    self.setdice(gui,var,pset[self.click-1])
                    #set to index for player in pset = click-1
                    self.pnum=self.click-1
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #end card
        elif self.click==6:
            file('End dice\n')
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card40')

#cards41-51 obmitted
class Card41:
    a=1

class Card42:
    a=1
    
class Card43:
    a=1
    
class Card44:
    a=1
    
class Card45:
    a=1
    
class Card46:
    a=1

class Card47:
    a=1
    
class Card48:
    a=1
    
class Card49:
    a=1
    
class Card50:
    a=1
    
class Card51:
    a=1

class Card52(Cards,StockEqu):
    title='STOCK EQUALISATION'
    cardnum=52
    cardfontcol='black'
    txmain='(Cards 41 to 51 obmitted.)\nSell any stock necessary to reduce your herds to 60 cows, 50 ewes, 16 sows and 2 horses.\nYou receive for cow £50, ewes £5, sows £20 and horses £40.\nBuy any stock you need to bring your stock up to 60 cows, 50 ewes, 16 sows and 2 horses.\nYou pay for cows £60, ewes £6, sows £30 and horses £50.\nYou have now the same stock that you started the game with. All cash you hold above £1500 is your profit. The farmer with the largest profit has won the game.'
    txoutput=['Click the Advance button to continue.',
              'Players have returned their initial £1500. All money remaining now is profit.\nClick the Next Card button for the results.']
    
    def run(self,gui,var,pset,deck,file):
        '''Run card52 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
        #adjust stock- extra
        elif (self.click>0 and self.click<6):
            file('Positive stock\n')
            #allow if player in game
            if pset[self.click-1].ingame==1:
                #adjustment
                self.postivestock(gui,pset[self.click-1].cows,pset[self.click-1].ewes,pset[self.click-1].sows,pset[self.click-1].horses,pset[self.click-1])
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #adjust stock- extra
        elif (self.click>5 and self.click<11):
            file('Positive stock\n')
            #allow if player in game
            if pset[self.click-1-5].ingame==1:
                #adjustment
                self.negativestock(gui,pset[self.click-1-5].cows,pset[self.click-1-5].ewes,pset[self.click-1-5].sows,pset[self.click-1-5].horses,pset[self.click-1-5])
            #move onto next player
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #profit
        elif self.click==11:
            i=0
            while i<var.pnum:
                if pset[i].ingame==1:
                    #print(pset[i].money)
                    self.profit(pset[i])
                    #print(pset[i].money)
                i+=1
            #set text
            self.settxout(gui,1)
            gui.btnswap(1)
        else:
            print('er card52')

class Card53(Cards,Winner,GraphPlot):
    title='SCORING'
    cardnum=53
    cardfontcol='black'
    txmain='All the cards have been played. The winner is the player that has made the most profit.'
    txoutput=['Click the Advance button to find out.',
           'Players that went bankrupt are: ',
           'This is the 1st game, there is no high score.\nNew high score!',
           'Corrupt file.\nThe data will be reset as fresh.',
           'Click the Advance button to continue.',
           'New high score!',
           'No new high score',
           'Equalled high score! (You score has been taken.)',
           'Game Over!\nClick the Advance button to plot the graph.\n(Warning that after clicking the Advance button it may take a while to load the next text.)'
           ,'Thank you for playing\nClose the window to view the graph.\n(It also has been saved as an image to file.)']
    pnarray=[]
    pmarray=[]
    pmarraysorted=[]
    wimmer='name'
    
    def run(self,gui,var,pset,deck,file):
        '''Run card53 fn'''
        #set initail text
        if self.click==0:
            self.settxinit(gui,var,self.cardfontcol)
            file('Set text\n')
            #self.pmarray=[]
            #self.pmarraysorted=[]
        #pays bills and end card
        elif self.click==1:
            file('Who\'s out\n')
            #add players to scoring array
            #find out 
            i=0
            tx=''
            while i<var.pnum:
                #find who's not in game
                if pset[i].ingame==0:
                    tx+=pset[i].name+'\n'
                else:
                    self.pnarray.append(pset[i].name)
                    self.pmarray.append(pset[i].money)
                    self.pmarraysorted.append(pset[i].money)
                i+=1
            #set text
            self.settxout(gui,1)
            #dealing with draws
            j=0
            while j<len(self.pmarray):
                a=float(random()*0.1)
                self.pmarray[j]+=a
                self.pmarraysorted[j]+=a
                j+=1
            #sort order
            self.pmarraysorted=self.sortvalues(self.pmarraysorted)
            #print(self.pmarraysorted,self.pmarray)
        #display results- 5th
        elif self.click==2:
            #check if 5 in players
            if len(self.pnarray)==5:
                #find player
                fith=self.findplayername(self.pmarraysorted,self.pmarray,self.pnarray)
                #display result
                self.settx(gui,'5th place is: '+fith)
                #remove from array
                #self.pnarray.remove(fith)
                #self.pmarray.remove()
            #if not
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #display results- 4th
        elif self.click==3:
            #check if 4 in players
            if len(self.pnarray)==4:
                #find player
                fourth=self.findplayername(self.pmarraysorted,self.pmarray,self.pnarray)
                #display result
                self.settx(gui,'4th place is: '+fourth)
            #if not
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #display results- 3rd
        elif self.click==4:
            #check if 3 in players
            if len(self.pnarray)==3:
                #find player
                third=self.findplayername(self.pmarraysorted,self.pmarray,self.pnarray)
                #display result
                self.settx(gui,'3rd place is: '+third)
            #if not
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #display results- 2nd
        elif self.click==5:
            #check if 2 in players
            if len(self.pnarray)==2:
                #find player
                second=self.findplayername(self.pmarraysorted,self.pmarray,self.pnarray)
                #display result
                self.settx(gui,'2nd place is: '+second)
            #if not
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #display results- 1st
        elif self.click==6:
            #check if 1 in players
            if len(self.pnarray)==1:
                #find player
                first=self.findplayername(self.pmarraysorted,self.pmarray,self.pnarray)
                #display result
                self.settx(gui,'1st place is: '+first)
                #re-display money players and find winner instance
                i=0
                while i<var.pnum:
                    if pset[i].ingame==1:
                        pset[i].settxvalue(pset[i].txm,pset[i].money)
                        if first==pset[i].name:
                            self.winner=pset[i]
                    i+=1
            #if not
            else:
                self.click+=1
                self.run(gui,var,pset,deck,file)
        #high score
        elif self.click==7:
            #open high score file if one, otherwise makes one
            try:
                f=open('farmingscore19.txt','r')
                yes=1
            except Exception:
                self.settxout(gui,2)
                #vars0.inthold=1
                yes=0
            if yes==0:
                #witing high score file
                f=open('farmingscore19.txt','w')
                txf='Name\tMoney\tWheat\tBarley\tOats\tPotatoes\n'
                f.write(txf)
            elif yes==1:
                try:
                    #read high score file- remove header
                    header=f.readline()
                    #find position at header end- for writing start
                    fpos=f.tell()
                    #cycle through line and get infomation
                    score=[]
                    for line in f:
                        line=line.strip()
                        col=line.split()
                        score.append(str(col[0])) #name
                        score.append(int(col[1])) #money
                        score.append(int(col[2])) #wheat
                        score.append(int(col[3])) #barley
                        score.append(int(col[4])) #oats
                        score.append(int(col[5])) #potatoes
                    tx='The current high score is £'+str(score[1])+' with '+str(score[2])+' wheat, '+str(score[3])+' barley, '+str(score[4])+' oats and '+str(score[5])+' potatoes.'
                    #set text
                    self.settxoutwithtx(gui,4,tx,'\n')
                    #holding read values
                    self.score=score
                    self.fpos=fpos
                except Exception:
                    self.settxout(gui,3)
                    yes=0
                    #write data
                    f=open('farmingscore19.txt','w')
                    txf='Name\tMoney\tWheat\tBarley\tOats\tPotatoes\n'
                    f.write(txf)
            else:
                print('er file find')
            self.yes=yes
            #close file
            f.close()
        elif self.click==8:
            #open file to read+write
            f=open('farmingscore19.txt','r+')
            #new high score- 1st game played
            if self.yes==0:
                tx='The new high score by player '+self.winner.name+' is: £'+str(self.winner.money)+' with '+str(self.winner.wheat)+' wheat, '+str(self.winner.barley)+' barley, '+str(self.winner.oats)+' oats and '+str(self.winner.potatoes)+' potatoes.'
                f.seek(0,2) #move to file end
                txw=str(self.winner.name+'\t'+str(self.winner.money)+'\t'+str(self.winner.wheat)+'\t'+str(self.winner.barley)+'\t'+str(self.winner.oats)+'\t'+str(self.winner.potatoes))
                f.write(txw)
                f.close()
                #set text
                self.settxoutwithtx2(gui,5,tx,'\n')
            #if new high score
            elif self.yes==1:
                f.seek(self.fpos) #seek to after header
                tx='The current high score is: £'+str(self.score[1])+'.\n'
                tx2=str(self.winner.name)+' score is: £'+str(self.winner.money)+'.\n'
                #see if new high score and write if so
                if self.winner.money>self.score[1]:
                    tx3=5
                    txw=str(self.winner.name+'\t'+str(self.winner.money)+'\t'+str(self.winner.wheat)+'\t'+str(self.winner.barley)+'\t'+str(self.winner.oats)+'\t'+str(self.winner.potatoes))
                    f.write(txw)
                elif self.winner.money<self.score[1]:
                    tx3=6
                else: 
                    tx3=7
                    txw=str(self.winner.name+'\t'+str(self.winner.money)+'\t'+str(self.winner.wheat)+'\t'+str(self.winner.barley)+'\t'+str(self.winner.oats)+'\t'+str(self.winner.potatoes))
                    f.write(txw)
                f.close()
                #gui.txoutput.configure(text=tx+tx2+tx3+cset[vars0.card].cardo[6])
                #set text
                self.settxoutwithtx(gui,tx3,tx+tx2,'')
        #end game
        elif self.click==9:#8
            #set text
            self.settxout(gui,8)
        #plot graphs
        elif self.click==10:#9
            #set text
            self.settxout(gui,9)
            #plot graphs
            self.plotmain(gui,var,pset)
            self.plotstock(gui,var,pset)
            self.plotdice(gui,var,pset)
            self.plotdice2(gui,var,pset)
            self.plotatrisk(gui,var,pset)
            #disable buttons
            gui.enable(gui.btnadvance,0)
        else:
            print('er card53')            
## end ##
            
#        if self.var.cardnum==0:
#                self.card0.run()
#            elif vars0.card==1:
#                Card01()
#            elif vars0.card==2:
#                Card02()
#            elif vars0.card==3:
#                Card03()
#            elif vars0.card==4:
#                Card04()
#            elif vars0.card==5:
#                Card05()
#            elif vars0.card==6:
#                Card06()
#            elif vars0.card==7:
#                Card07()
#            elif vars0.card==8:
#                Card08()
#            elif vars0.card==9:
#                Card09()
#            elif vars0.card==10:
#                Card10()
#            elif vars0.card==11:
#                Card11()
#            elif vars0.card==12:
#                Card12()
#            elif vars0.card==13:
#                Card13()
#            elif vars0.card==14:
#                Card14()
#            elif vars0.card==15:
#                Card15()
#            elif vars0.card==16:
#                Card16()
#            elif vars0.card==17:
#                Card17()
#            elif vars0.card==18:
#                Card18()
#            elif vars0.card==19:
#                Card19()
#            elif vars0.card==20:
#                Card20()
#            elif vars0.card==21:
#                Card21()
#            elif vars0.card==22:
#                Card22()
#            elif vars0.card==23:
#                Card23()
#            elif vars0.card==24:
#                Card24()
#            elif vars0.card==25:
#                Card25()
#            elif vars0.card==26:
#                Card26()
#            elif vars0.card==27:
#                Card27()
#            elif vars0.card==28:
#                Card28()
#            elif vars0.card==29:
#                Card29()
#            elif vars0.card==30:
#                Card30()
#            elif vars0.card==31:
#                Card31()
#            elif vars0.card==32:
#                Card32()
#            elif vars0.card==33:
#                Card33()
#            elif vars0.card==34:
#                Card34()
#            elif vars0.card==35:
#                Card35()
#            elif vars0.card==36:
#                Card36()
#            elif vars0.card==37:
#                Card37()
#            elif vars0.card==38:
#                Card38()
#            elif vars0.card==39:
#                Card39()
#            elif vars0.card==40:
#                Card40()
#            elif vars0.card==41:
#                Card41()
#            elif vars0.card==42:
#                Card42()
#            elif vars0.card==43:
#                Card43()
#            elif vars0.card==44:
#                Card44()
#            elif vars0.card==45:
#                Card45()
#            elif vars0.card==46:
#                Card46()
#            elif vars0.card==47:
#                Card47()
#            elif vars0.card==48:
#                Card48()
#            elif vars0.card==49:
#                Card49()
#            elif vars0.card==50:
#                Card50()
#            elif vars0.card==51:
#                Card51()
#            elif vars0.card==52:
#                Card52()
#            elif vars0.card==53:
#                Card53()
#            else:
#                print('card er')