#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:26:47 2022

@author: kristianberg
"""

from datetime import datetime

class Avtale:
    def __init__(self, tittel, sted, dato, varighet):
        self.tittel=tittel      #str
        self.sted=sted          #str
        self.dato=dato          #datetime.datetime
        self.varighet=varighet  #int
        
    def __str__(self): 
        return f"{self.tittel}, {self.sted}, {self.dato}, {self.varighet}"


liste_avtale=[]

def nyavtale():
   tittel=input("Tittel til avtale: ")
   sted=input("Sted: ")
   dato=input("Kode for datoen: ")
   varighet=int(input("Varighet: "))
   liste_avtale.append(nyavtale)
   return f"{tittel}, {sted}, {dato}, {varighet}"

avtale="{tittel}, {sted}, {dato}, {varighet}"


def avtaleliste(avtale):
    with open ("avtale.txt", "w") as fil:
        for avtale in liste_avtale:
            input(avtale)
            fil.write(str(Avtale) +"\n")
            liste_avtale.append(Avtale)
            
print (liste_avtale)

def leseavtale():
    with open ("avtale.txt", "r") as fil2:
        for avtale in fil2:
            print(fil2)
            
def avtaledato(tittel,l): 
    with open ("avtale.txt", "r") :
        l=input("Hvilken dato?")
        return l(tittel)
    
            
def finneavtale(listeavtale, k): 
    with open ("avtale.txt,", "r") as fil3: 
        k=input("hva leter du etter?")
        for avtalen in fil3 : 
            if avtalen==k : 
                print (avtalen)
            if avtalen !=k : 
                continue
               
#def søke (liste_avtale, r):
 #   r=input("søkeord")
  #  return (liste_avtale(r))
#print (liste_avtale(søke))
    


      


