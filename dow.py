from tkinter import *

class DOW:

    def __init__(self):
        window = Tk()
        window.title('DOW')
        Label(window,text='',width=1).grid(row=0,column=0)
        Label(window,text='Company').grid(row=0,column=3,sticky=W)
        Label(window,text='Industry').grid(row=3,column=3,sticky=W)
        Label(window,text='Exchange:').grid(row=6,column=4,sticky=E)
        Label(window,text='Growth in 2013:').grid(row=7,column=4,sticky=E)
        Label(window,text='Price/Earnings ratio:').grid(row=8,column=4,sticky=E)

        yscroll = Scrollbar(window, orient=VERTICAL)
        yscroll.grid(row=0,column=2,rowspan=9,pady=5,stick=NS)

        infile=open('DOW.txt','r')
        symbolSet = {line.split(',')[1] for line in infile}
        infile.close()

        symbolList = list(symbolSet)
        symbolList.sort()

        self.conSymbols = StringVar()
        self._lstSymbols = Listbox(window,width=5,listvariable=self.conSymbols,yscrollcommand=yscroll.set)
        self._lstSymbols.grid(row=0,column=1,rowspan=9,pady=5,sticky=E)
        self._lstSymbols.bind('<<ListboxSelect>>',self.facts)
        self.conSymbols.set(tuple(symbolList))  # VarString() içerisine dize(string) yada tuple atılır.

        self.conCompany = StringVar()
        self.entCompany = Entry(window,state='readonly',width=30,textvariable=self.conCompany)
        self.entCompany.grid(row=1,column=3,columnspan=2,padx=5,sticky=W)

        self.conIndustry = StringVar()
        self.entIndustry = Entry(window,state='readonly',width=30,textvariable=self.conIndustry)
        self.entIndustry.grid(row=4,column=3,columnspan=2,padx=5,sticky=W)

        self.conExchange = StringVar()
        self.entExchange = Entry(window,width=8,state='readonly',textvariable=self.conExchange)
        self.entExchange.grid(row=6,column=5,padx=5,sticky=W)

        self.conGrowth = StringVar()
        self.entGrowth = Entry(window,width=8,state='readonly',textvariable=self.conGrowth)
        self.entGrowth.grid(row=7,column=5,padx=5,sticky=W)

        self.conPE = StringVar()
        self.entPE = Entry(window,width=8,state='readonly',textvariable=self.conPE)
        self.entPE.grid(row=8,column=5,padx=5,sticky=W)

        yscroll['command'] = self._lstSymbols.yview

        window.mainloop()

    def facts(self,e):
        symbol = self._lstSymbols.get(self._lstSymbols.curselection())

        infile = open('DOW.txt','r')
        while True:
            line = infile.readline()
            lineList = line.split(',')
            if lineList[1] == symbol:
                break;
        infile.close()

        self.conCompany.set(lineList[0])
        self.conIndustry.set(lineList[3])
        self.conExchange.set(lineList[2])
        increase = (float(lineList[5]) - float(lineList[4])) / float(lineList[4])
        self.conGrowth.set('{0:.2%}'.format(increase))
        priceEarningsRatio = float(lineList[5]) / float(lineList[6])
        self.conPE.set('{0:.2f}'.format(priceEarningsRatio))
DOW()