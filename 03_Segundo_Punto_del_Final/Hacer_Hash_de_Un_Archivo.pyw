# -*- coding: utf-8 -*-
from os import path as p

pt = print

def cdsp():
    return p.dirname(p.realpath(__file__))

def prtu():
    lra = ""
    try:
         from tkinter import Tk as t,filedialog as fd 
         v = t()
         v.withdraw()
         fta = [('Todos los archivos', '.*'),]
         titulo = 'Por Favor Seleccione el Archivo, al que se le calculara el hash md5'
         cds = cdsp()
         ru = fd.askopenfilename(parent=v,
                                    initialdir=cds,
                                    title=titulo,
                                    filetypes=fta)
         lra = ru
    except Exception as E:
        pt("INICIO---ERROR--------------------------")
        pt(E)
        pt("FIN---ERROR--------------------------")
    finally:
        return lra    

def md5ha(ram5):
    from hashlib import md5 as m
    tth = ""
    gh = m()
    a = open(ram5,"rb")
    bloque = a.read(2048)
    while bloque:
        gh.update(bloque)
        bloque = a.read(2048)
    a.close()    
    return  gh.hexdigest()
    
def hha():
    from tkinter import messagebox as msg                  
    rda = prtu()
    nar = p.basename(p.realpath(rda))
    pt("'"+rda+"'")
    hx = md5ha(rda)
    pt(hx)
    rdh = cdsp()
    rdh += p.sep + nar
    rdh += "__md5sum.txt" 
    pt(rdh)
    a = open(rdh,"w")
    linea = hx + "  " + nar
    a.write(linea)
    a.close()
    msg.showinfo("TERMINE",rdh)
    
def pp():
    hha()
    
if __name__ == "__main__":
    pp()
