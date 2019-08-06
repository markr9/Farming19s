# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:30:45 2019

@author: MR
"""

import Farming19ex_t as f19
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as box
#import pytest

#tests
#internal tests only
#gui
#enable and disable
def test_enable():
    array=[f19.gui.pnum,f19.gui.dice,f19.gui.btnpnum,f19.gui.btndice,f19.gui.btndselect,f19.gui.btnadvance,f19.gui.btnnext,f19.gui.btnquit]#f19.gui.pops,f19.gui.cb1,f19.gui.cb2,f19.gui.cb3,f19.gui.cb4,f19.gui.cb5,f19.gui.op1,f19.gui.op2,f19.gui.op3,f19.gui.op4,f19.gui.op5,f19.gui.op6,
    for x in array:
        #unknown state-enable
        state=x['state']
        f19.gui.enable(x,1)
        state=x['state']
        assert str(state)==NORMAL
        #enable-disable
        f19.gui.enable(x,0)
        state=x['state']
        assert str(state)==DISABLED
        #disable-disable
        f19.gui.enable(x,0)
        state=x['state']
        assert str(state)==DISABLED
        #disable-enable
        f19.gui.enable(x,1)
        state=x['state']
        assert str(state)==NORMAL
        #enable-enable
        f19.gui.enable(x,1)
        state=x['state']
        assert str(state)==NORMAL

def test_takemoney():
    f19.p1.money=10000
    a=10000
    for num in [0,50,100,450,753,1500]:
        f19.card0.takemoney(num,f19.p1)
        a=a-num
        assert a==f19.p1.money
        
def test_givemoney():
    f19.p2.money=10
    a=10
    for num in [0,50,100,450,753,1500]:
        f19.card0.givemoney(num,f19.p2)
        a=a+num
        assert a==f19.p2.money
        
def test_transfermoney():
    f19.p3.money=5000
    f19.p4.money=5000
    a=5000
    b=5000
    for num in [0,50,100,450,753,1500]:
        f19.card0.transfermoney(num,f19.p3,f19.p4)
        a=a-num
        b=b+num
        assert a==f19.p3.money
        assert b==f19.p4.money
        
def test_case():
    f19.p1.cows=60
    f19.p1.ewes=50
    f19.p1.sows=10
    f19.p1.horses=2
    f19.p1.hcalves=20
    f19.p1.bcalves=20
    f19.p1.lambs=20
    f19.p1.spigs=100
    f19.card0.case(f19.p1,'cows',1)
    assert 61==f19.p1.cows
    f19.card0.case(f19.p1,'ewes',5)
    assert 55==f19.p1.ewes
    f19.card0.case(f19.p1,'sows',-3)
    assert 7==f19.p1.sows
    f19.card0.case(f19.p1,'horses',-1)
    assert 1==f19.p1.horses
    f19.card0.case(f19.p1,'hcalves',10)
    assert 30==f19.p1.hcalves
    f19.card0.case(f19.p1,'bcalves',-10)
    assert 10==f19.p1.bcalves
    f19.card0.case(f19.p1,'lambs',1)
    assert 21==f19.p1.lambs
    f19.card0.case(f19.p1,'spigs',-100)
    assert 0==f19.p1.spigs
        
def test_takestock():
    f19.p1.money=10000
    a=10000
    f19.p1.cows=60
    f19.p1.ewes=50
    f19.p1.sows=10
    f19.p1.horses=2
    f19.p1.hcalves=20
    f19.p1.bcalves=20
    f19.p1.lambs=20
    f19.p1.spigs=100
    c=60
    e=50
    s=10
    h=2
    bc=20
    hc=20
    l=20
    sp=100
    #cows
    f19.card1.takestock(1,50,'cows',f19.p1)
    c=c-1
    assert c==f19.p1.cows
    assert a<f19.p1.money
    #ewes and sows
    f19.card1.takestock(5,500,'ewes',f19.p1)
    f19.card1.takestock(3,75,'sows',f19.p1)
    e=e-5
    s=s-3
    assert e==f19.p1.ewes
    assert s==f19.p1.sows
    assert a<f19.p1.money
    #horses
    f19.card1.takestock(1,0,'horses',f19.p1)
    h=h-1
    assert h==f19.p1.horses
    assert a<f19.p1.money
    #bc and hc
    f19.card1.takestock(0,10,'bcalves',f19.p1)
    f19.card1.takestock(10,75,'hcalves',f19.p1)
    bc=bc-0
    hc=hc-10
    assert bc==f19.p1.bcalves
    assert hc==f19.p1.hcalves
    assert a<f19.p1.money
    #lambs
    f19.card1.takestock(20,150,'lambs',f19.p1)
    l=l-20
    assert l==f19.p1.lambs
    assert a<f19.p1.money
    #store pigs
    f19.card1.takestock(100,0,'spigs',f19.p1)
    sp=sp-100
    assert sp==f19.p1.spigs
    assert a<f19.p1.money

def test_givestock():
    f19.p2.money=10000
    a=10000
    f19.p2.cows=60
    f19.p2.ewes=50
    f19.p2.sows=10
    f19.p2.horses=2
    f19.p2.hcalves=20
    f19.p2.bcalves=20
    f19.p2.lambs=20
    f19.p2.spigs=100
    c=60
    e=50
    s=10
    h=2
    bc=20
    hc=20
    l=20
    sp=100
    #cows
    f19.card1.givestock(1,50,'cows',f19.p2)
    c=c+1
    assert c==f19.p2.cows
    assert a>f19.p2.money
    #ewes and sows
    f19.card1.givestock(5,500,'ewes',f19.p2)
    f19.card1.givestock(3,75,'sows',f19.p2)
    e=e+5
    s=s+3
    assert e==f19.p2.ewes
    assert s==f19.p2.sows
    assert a>f19.p2.money
    #horses
    f19.card1.givestock(1,0,'horses',f19.p2)
    h=h+1
    assert h==f19.p2.horses
    assert a>f19.p2.money
    #bc and hc
    f19.card1.givestock(0,10,'bcalves',f19.p2)
    f19.card1.givestock(10,75,'hcalves',f19.p2)
    bc=bc+0
    hc=hc+10
    assert bc==f19.p2.bcalves
    assert hc==f19.p2.hcalves
    assert a>f19.p2.money
    #lambs
    f19.card1.givestock(20,150,'lambs',f19.p2)
    l=l+20
    assert l==f19.p2.lambs
    assert a>f19.p2.money
    #store pigs
    f19.card1.givestock(100,0,'spigs',f19.p2)
    sp=sp+100
    assert sp==f19.p2.spigs
    assert a>f19.p2.money

def test_transferstock():
    f19.p3.cows=c3=60
    f19.p4.cows=c4=60
    f19.p3.lambs=l3=70
    f19.p4.lambs=l4=70
    f19.p3.money=a=100
    f19.p4.money=b=100
    f19.card1.transferstock(1,50,'cows',f19.p3,f19.p4)
    a=a+50
    b=b-50
    c3-=1
    c4+=1
    assert a==f19.p3.money
    assert b==f19.p4.money
    assert c3==f19.p3.cows
    assert c4==f19.p4.cows
    f19.card1.transferstock(9,125,'lambs',f19.p4,f19.p3)
    a=a-125
    b=b+125
    l3+=9
    l4-=9
    assert a==f19.p3.money
    assert b==f19.p4.money
    assert l3==f19.p3.lambs
    assert l4==f19.p4.lambs
        
def test_getcrops():
    f19.gui.op1.setvalues(start=3)
    f19.gui.op2.setvalues(start=1)
    f19.gui.op3.setvalues(start=0)
    f19.gui.op4.setvalues(start=2)
    f19.gui.op5.setvalues(start=0)
    f19.card1.getcrops(f19.gui,f19.p1)
    assert f19.p1.wheat==3
    assert f19.p1.barley==1
    assert f19.p1.oats==0
    assert f19.p1.potatoes==2
    assert f19.p1.ley==4
    
def test_croplegal():
    f19.gui.op1.setvalues(start=3)
    f19.gui.op2.setvalues(start=1)
    f19.gui.op3.setvalues(start=0)
    f19.gui.op4.setvalues(start=2)
    f19.gui.op5.setvalues(start=0)
    #< value 3,1,0,2,0<10
    assert 0==f19.card1.croplegal(f19.gui,f19.p2)
    #== value 3,1,4,2,0=10
    f19.gui.op3.setvalues(start=4)
    assert 0==f19.card1.croplegal(f19.gui,f19.p2)
    #> value -ve ley 3,5,4,2,0>10
    f19.gui.op2.setvalues(start=5)
    assert -1==f19.card1.croplegal(f19.gui,f19.p2)
    #> value both 3,5,4,2,6>10
    f19.gui.op5.setvalues(start=6)
    assert -1==f19.card1.croplegal(f19.gui,f19.p2)
    #< value with ley 3,0,2,2,1<10
    f19.gui.op5.setvalues(start=1)
    f19.gui.op2.setvalues(start=0)
    f19.gui.op3.setvalues(start=2)
    assert 0==f19.card1.croplegal(f19.gui,f19.p2)
    #=value with ley 3,0,2,2,3=10
    f19.gui.op5.setvalues(start=3)
    assert 0==f19.card1.croplegal(f19.gui,f19.p2)
    
def test_payseeds():
    f19.p1.money=5000
    a=5000
    f19.p1.wheat=2
    f19.p1.barley=1
    f19.p1.oats=0
    f19.p1.potatoes=3
    f19.p1.ley=5
    #0 tests
    f19.card2.payseeds(f19.p1,w=0,b=0,o=0,p=0)
    a=a-0*2+0*1+0*0+0*3
    assert a==f19.p1.money
    assert a==5000
    assert 5000==f19.p1.money
    #100, 120,150, 50, 200,50,100 ,175,125,150,225
    f19.card2.payseeds(f19.p1,w=100,b=0,o=0,p=0)
    a=a-(100*2+0*1+0*0+0*3)
    assert a==f19.p1.money
    assert 4800==f19.p1.money
    f19.card2.payseeds(f19.p1,w=120,b=0,o=150,p=0)
    a=a-(120*2+0*1+150*0+0*3)
    assert a==f19.p1.money
    print(a,f19.p1.money)
    f19.card2.payseeds(f19.p1,w=0,b=0,o=0,p=50)
    a=a-(0*2+0*1+0*0+50*3)
    print(a,f19.p1.money)
    assert a==f19.p1.money
    f19.card2.payseeds(f19.p1,w=0,b=200,o=50,p=100)
    a=a-(0*2+200*1+50*0+100*3)
    assert a==f19.p1.money
    f19.card2.payseeds(f19.p1,w=175,b=125,o=150,p=225)
    a=a-(175*2+125*1+150*0+225*3)
    assert a==f19.p1.money
    
def test_getauctionsell():
    f19.p1.money=1000
    f19.p1.cows=60
    f19.p1.sows=20
    f19.p1.hcalves=2
    f19.p1.spigs=120
    tx=['a','b','c']
    f19.gui.op1.value=1
    f19.card3.getauctionsell(f19.gui,50,'cows',f19.game.pset,0,tx)
    assert 59==f19.p1.cows
    assert 1050==f19.p1.money
    f19.gui.op1.value=10
    f19.card3.getauctionsell(f19.gui,150,'sows',f19.game.pset,1,tx)
    assert 10==f19.p1.sows
    assert 1200==f19.p1.money
    f19.gui.op1.value=2
    f19.card3.getauctionsell(f19.gui,10,'hcalves',f19.game.pset,1,tx)
    assert 0==f19.p1.hcalves
    assert 1210==f19.p1.money
    f19.gui.op1.value=90
    f19.card3.getauctionsell(f19.gui,5,'spigs',f19.game.pset,0,tx)
    assert 30==f19.p1.spigs
    assert 1660==f19.p1.money
    
def test_getauctionbuy():
    f19.p1.money=1000
    f19.p1.cows=60
    f19.p1.sows=20
    f19.p1.hcalves=2
    f19.p1.spigs=120
    f19.card3.setpops(f19.gui,f19.game.pset)
    f19.gui.pops.set('Player1')
    f19.p1.name='Player1'
    tx=[1,'b',50]
    f19.gui.mop.setvalues(start=50)
    f19.card3.getauctionbuy(f19.gui,'cows',f19.game.pset,tx)
    assert 61==f19.p1.cows
    assert 950==f19.p1.money
    tx=[10,'b',150]
    f19.gui.pops.set('Player1')
    f19.gui.mop.setvalues(start=150)
    f19.card3.getauctionbuy(f19.gui,'sows',f19.game.pset,tx)
    assert 30==f19.p1.sows
    assert 800==f19.p1.money
    tx=[2,'b',10]
    f19.gui.pops.set('Player1')
    f19.gui.mop.setvalues(start=10)
    f19.card3.getauctionbuy(f19.gui,'hcalves',f19.game.pset,tx)
    assert 4==f19.p1.hcalves
    assert 790==f19.p1.money
    tx=[90,'b',190]
    f19.gui.pops.set('Player1')
    f19.gui.mop.setvalues(start=190)
    f19.card3.getauctionbuy(f19.gui,'spigs',f19.game.pset,tx)
    assert 210==f19.p1.spigs
    assert 600==f19.p1.money
    
#dice tests td
    
def test_end():
    f19.win.destroy()
        
#pytest.main('farming19test.py')
  
#f19.win.mainloop()

#from tkinter.ttk import *
#from tkinter import *
#
#win=Tk()
#win.geometry('200x200')
#win.title('title')
#lab1=Label(win,text='hello')
#lab1.grid(row=1,column=1)
#
#win2=Tk()
#win2.geometry('100x100')
#win2.title('title2')
#lab2=Label(win2,text='hello2u')
#lab2.grid(row=1,column=1)
#
#win2.mainloop()
#
#win.mainloop()