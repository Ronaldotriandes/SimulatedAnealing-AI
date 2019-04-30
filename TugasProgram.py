from random import uniform
import numpy as np
from math import exp

#RONALDO TRIANDES
#1301154108


x1 = uniform (-10,10)
x2 = uniform (-10,10) #menginisialisasi x1 dan x2 dengan batas antara -10 sampai 10

def fungsi(x1,x2):
    f = - np.absolute(np.sin(x1) * np.cos(x2) + 4/6 * np.exp((1- (np.sqrt(x1**2 + x2**2) ))))
    return f #memasukan function yang sudah ditentukan di tupro 1
Best = fungsi(x1, x2)
tmpt = 1000000 
coolingrate = 0.999 
t_minimum = 1  #memasukan temprtur dan colingrate serta tempertr akhr sesuai ketentuannya



while (tmpt > t_minimum): #melakukan perbandingan kika tmprtur lebih besar dari tmin maka akan ditampung ke variable x1 dan x2 dengan random
    x1 = uniform(-10, 10) 
    x2 = uniform(-10, 10) #melakukan generate kembali x1 dan x2
    fbaru =  fungsi(x1,x2)
    if (Best > fbaru): #melakukan perbandungan antara fungsi lama dan bru
        Best = fbaru   
    else:
        AE = (Best -  fbaru)/tmpt
        if (exp(AE)) > uniform(0,1): #mamasukan rumus probabilitas
            Best = fbaru
    tmpt = tmpt * coolingrate #melakukan anealing schedule
print(Best) #menampilkan hasil dari best 
def Selesai():
    print("selesai, dan terima kasih")
Selesai()