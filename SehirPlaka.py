import tkinter
class Sınıf:
    def __init__(self):
        pencere=tkinter.Tk()
        pencere.title("şehir plaka eşleşmesi.")

        şehirEt=tkinter.Label(pencere,text="şehir")
        şehirEt.grid(row=0,column=0)

        plakaEt=tkinter.Label(pencere,text="plaka")
        plakaEt.grid(row=0,column=1)

        self.şehir=["kırıkkale","ankara","trabzon","izmir","istanbul","adana"]
        self.plaka=["71","06","61","35","34","01"]

        şehirler=tkinter.StringVar()
        şehirler.set(tuple(self.şehir))

        plakaSıralı=list(self.plaka)
        plakaSıralı.sort()
        plakalar=tkinter.StringVar()
        plakalar.set(tuple(plakaSıralı))

        self.sehirKutu = tkinter.Listbox(pencere, height=6, width=20, exportselection=0, listvariable=şehirler)
        self.sehirKutu.grid(row=1, column=0)

        self.plakaKutu=tkinter.Listbox(pencere,height=6,width=4,exportselection=0,listvariable=plakalar)
        self.plakaKutu.grid(row=1,column=1)

        kontrolbuton=tkinter.Button(pencere,text="doğru mu yanlış mı",command=self.kontrol)
        kontrolbuton.grid(row=2,column=1)

        cevapEt=tkinter.Label(pencere,text="cevap")
        cevapEt.grid(row=3,column=0)

        self.cevap=tkinter.StringVar()
        cevapGel=tkinter.Entry(pencere,textvariable=self.cevap)
        cevapGel.grid(row=3,column=1)

        tkinter.mainloop()

    def kontrol(self):
        a=self.şehir.index(self.sehirKutu.get(self.sehirKutu.curselection()))
        b=self.plaka.index(self.plakaKutu.get(self.plakaKutu.curselection()))

        if a==b:
            self.cevap.set("doğru")
        else:
            self.cevap.set("yanlış")
nesnem=Sınıf()