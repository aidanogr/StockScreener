import datetime as dt
from datetime import date as da
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from tkinter import *
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import requests
import webbrowser as wb


#Pulling top 20 stocks of the day 

stcks = []
lstcks = []
cryptoName = []
co = []


r = requests.get("https://finance.yahoo.com/gainers")
f = requests.get("https://finance.yahoo.com/losers")
c = requests.get("https://finance.yahoo.com/cryptocurrencies")
fbc = requests.get("https://www.facebook.com/marketplace/107513042612019/search/?query=couches")
#Convert to object

soup = bs(r.content)
soap = bs(f.content)
captainPrice = bs(c.content)
coPrice = bs(fbc.content)

#find the "a" tags with stock names
price = soup.find_all("a", attrs={"class":"Fw(600) C($linkColor)"})
loss = soap.find_all("a", attrs={"class":"Fw(600) C($linkColor)"})
cryp = captainPrice.find_all("a", attrs={"class":"Fw(600) C($linkColor)"})

#find couch price (span)

couchPrice = coPrice.find_all("span", attrs={"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id"})

#for ce in couchPrice:
#    co.append(ce.text)
for a in price:
    stcks.append(a.text)
for b in loss:
    lstcks.append(b.text)
for d in cryp:
    cryptoName.append(d.text)
    
###StockData
style.use('ggplot')
today = da.today()
datee = dt.datetime.strptime(str(today), "%Y-%m-%d")


start = dt.datetime(datee.year, int(datee.month)-3, int(datee.day))
end = today


###GUI

root = Tk()
root.geometry("")

def newBack():
    global frame
    try:
        selFrame.destroy()
    except err:
        fcFrame.destroy()
    except err:
        frame.destroy()
    finally:
        pass
    frame = LabelFrame(root, text="Finance", padx=200, pady=100)
    frame.grid(row=0, column=0)
    myButton1 = Button(frame, text="Stock Prices", command=selec, padx=50, pady=2)
    myButton1.grid(row=0, column=0)
    #cButton1 = Button(frame, text="CPU Prices")
    freelanc = Button(frame, text="Miscellaneous Freelancing", command=flc, padx=50, pady=2)
    freelanc.grid(row=1, column=0)
def flc():
    global fcFrame
    frame.destroy()
    fcFrame = LabelFrame(root, text="Freelancing", padx=200, pady=100)
    fcFrame.grid(row=0, column=0)
    global bbButton
    bbButton = Button(fcFrame, text="Back", command=newBack, padx=50, pady=2)
    bbButton.grid()
    fbButton = Button(fcFrame, text="Facebook Marketplace", command=fbb, padx=50, pady=2)
    fbButton.grid(row=1, column=0)
    
def fbb():
    wb.open('https://www.facebook.com/marketplace/107513042612019/search/?query=couches')

def selec():
    
    global selFrame
    frame.destroy()
    selFrame = LabelFrame(root, text="Select Your Mode", padx=200, pady=100)
    selFrame.grid(row=0, column=0)
    babButton = Button(selFrame, text="Back", command=newBack, padx=50, pady=2)
    babButton.grid(row=0, column=0)
    fButton1 = Button(selFrame, text="Rising Stocks", command=sClick, padx=50, pady=2).grid(row=1, column=0)
    lButton1 = Button(selFrame, text="Losing Stocks", command=lClick, padx=48, pady=2).grid(row=2, column=0)
    btcButton = Button(selFrame, text="Cryptocurrencies", command=cryp, padx=39, pady=2)
    btcButton.grid(row=3, column=0)

def cryp():
    selFrame.destroy()
    try:
        frame.destroy()
    except:
        pass
    global btcFrame
    btcFrame = LabelFrame(root, text="Crypto Prices", padx=200, pady=100)
    btcFrame.grid(row=0, column=0)
    backButton = Button(btcFrame, text="Back", command= lambda: back_button(3)).grid(row=0, column=0)
    j=1
    for n in cryptoName:
        j = j+1
        Button(btcFrame, text=n, command = lambda crt = n: cryptoc(crt)).grid(row=j, column=0)
def cryptoc(crt):
    p = web.DataReader(crt, 'yahoo', start, end)
    p['High'].plot()
    plt.title(crt)
    plt.show()
def lClick():
        selFrame.destroy()
        try:
            frame.destroy()
        except:
            pass
        global lossFrame
        lossFrame = LabelFrame(root, text="Stock Prices", padx=200, pady=100)
        lossFrame.grid(row=0,column=0)
        en=1
        backButton = Button(lossFrame, text="Back", command= lambda: back_button(1)).grid(row=0, column=0)  
        for z in lstcks:
            en=en+1
            Button(lossFrame, text=z, width=20, command = lambda losss=z: lossSt(losss)).grid(row=en, column=0)
            
def lossSt(losss):
    ef = web.DataReader(losss, 'yahoo', start, end)
    ef['High'].plot()
    plt.title(losss)
    plt.show()
def tsla(newN):
    df = web.DataReader(newN, 'yahoo', start, end)
  #  f = Figure(figsize=(5,5), dpi=100)
    df['High'].plot()
    plt.title(newN)
    plt.show()
    
def sClick():
    global newF
    selFrame.destroy()
    frame.destroy()
    newF = LabelFrame(root, text ="Stock Prices", padx=200, pady=100)
    newF.grid(row=0, column=0)
    backButton = Button(newF, text="Back", command= lambda: back_button(2)).grid(row=0, column=0)  
    y=1
    for nm in stcks:
        y=y+1
        Button(newF, text=nm, width=20, command = lambda newN=nm: tsla(newN)).grid(row=y, column=0)
    
    
def back_button(intt):
    if intt == 2:
        
        newF.destroy()
        selFrame.destroy()
    elif intt == 1:
        lossFrame.destroy()
    elif intt ==3:
        btcFrame.destroy()
    else:
        pass
    global frame
    frame = LabelFrame(root, text="Select Your Mode", padx=200, pady=100)
    frame.grid(row=0, column=0)
    myButton1 = Button(frame, text="Rising Stocks", command=sClick, padx=50, pady=2)
    myButton1.grid(row=1, column=0)
    lButton1 = Button(frame, text="Losing Stocks", command=lClick, padx=50, pady=2).grid(row=2, column=0)
    btcButton = Button(frame, text="Cryptocurrencies", command=cryp, padx=39, pady=2)
    btcButton.grid(row=3, column=0)
    babButton = Button(frame, text="Back", command=newBack, padx=50, pady=2)
    babButton.grid(row=0, column=0)

global frame
frame = LabelFrame(root, text="Finance", padx=200, pady=100)
frame.grid(row=0, column=0)
myButton1 = Button(frame, text="Stock Prices", command=selec, padx=50, pady=2)
myButton1.grid(row=0, column=0)
#cButton1 = Button(frame, text="CPU Prices")
freelanc = Button(frame, text="Miscellaneous Freelancing", command=flc, padx=50, pady=2)
freelanc.grid(row=1, column=0)
root.mainloop()
