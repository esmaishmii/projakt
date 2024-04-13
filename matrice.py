import tkinter as tk
import numpy as np

# Definisanje globalnih varijabli za matrice
matrica1 = None
matrica2 = None

def kreiraj_matricu1():
    global matrica1
    matrica1 = []
    unos_elementi = entry_elementi.get().split()
    for i in range(int(entry_vrste.get())):
        red = []
        for j in range(int(entry_kolone.get())):
            element = int(unos_elementi[i * int(entry_kolone.get()) + j])
            red.append(element)
        matrica1.append(red)
    
    prikazi_matricu(matrica1)

def kreiraj_matricu2():
    global matrica2
    matrica2 = []
    unos_elementi = entry_elementi.get().split()
    for i in range(int(entry_vrste.get())):
        red = []
        for j in range(int(entry_kolone.get())):
            element = int(unos_elementi[i * int(entry_kolone.get()) + j])
            red.append(element)
        matrica2.append(red)
    
    prikazi_matricu(matrica2)

def saberi_i_prikazi():
    global matrica1, matrica2
    if matrica1 is not None and matrica2 is not None:
        rezultat = saberi_matrice(matrica1, matrica2)
        if rezultat is not None:
            prikazi_matricu(rezultat)
    else:
        print("Nisu unesene obje matrice!")

def oduzmi_matrice(matrica1, matrica2):
    if len(matrica1) != len(matrica2) or len(matrica1[0]) != len(matrica2[0]):
        print("Matrice moraju biti istih dimenzija za oduzimanje!")
        return None
    
    rezultat = []
    for i in range(len(matrica1)):
        red = []
        for j in range(len(matrica1[0])):
            red.append(matrica1[i][j] - matrica2[i][j])
        rezultat.append(red)
    
    return rezultat

def oduzmi_i_prikazi():
    global matrica1, matrica2
    if matrica1 is not None and matrica2 is not None:
        rezultat = oduzmi_matrice(matrica1, matrica2)
        if rezultat is not None:
            prikazi_matricu(rezultat)
    else:
        print("Nisu unesene obje matrice!")

def pomnozi_matrice():
    global matrica1, matrica2
    if matrica1 is not None and matrica2 is not None:
        rezultat = np.dot(matrica1, matrica2)
        prikazi_matricu(rezultat)
    else:
        print("Nisu unesene obje matrice!")

def saberi_matrice(matrica1, matrica2):
    if len(matrica1) != len(matrica2) or len(matrica1[0]) != len(matrica2[0]):
        print("Matrice moraju biti istih dimenzija za sabiranje!")
        return None
    
    rezultat = []
    for i in range(len(matrica1)):
        red = []
        for j in range(len(matrica1[0])):
            red.append(matrica1[i][j] + matrica2[i][j])
        rezultat.append(red)
    
    return rezultat

def prikazi_matricu(matrica):
    top = tk.Toplevel()
    top.title("Matrica")
    
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            label = tk.Label(top, text=str(matrica[i][j]), borderwidth=0, width=10, height=3, font=("Helvetica", 12))
            label.grid(row=i, column=j)

def transponuj_i_prikazi(matrica):
    transponovana_matrica = np.transpose(matrica)
    prikazi_matricu(transponovana_matrica)

root = tk.Tk()
root.title("Kreiranje i Operacije sa Matricama")
root.geometry("400x300")

label_vrste = tk.Label(root, text="Unesite broj vrsta:")
label_vrste.grid(row=0, column=0)
entry_vrste = tk.Entry(root)
entry_vrste.grid(row=0, column=1)

label_kolone = tk.Label(root, text="Unesite broj kolona:")
label_kolone.grid(row=1, column=0)
entry_kolone = tk.Entry(root)
entry_kolone.grid(row=1, column=1)

label_elementi = tk.Label(root, text="Unesite elemente redom po vrsti \n (razdvojene sa space):")
label_elementi.grid(row=2, column=0)
entry_elementi = tk.Entry(root)
entry_elementi.grid(row=2, column=1)

kreiraj_button1 = tk.Button(root, text="Kreiraj Prvu Matricu", command=kreiraj_matricu1)
kreiraj_button1.grid(row=3, columnspan=2)

kreiraj_button2 = tk.Button(root, text="Kreiraj Drugu Matricu", command=kreiraj_matricu2)
kreiraj_button2.grid(row=4, columnspan=2)

saberi_button = tk.Button(root, text="Saberi Matrice", command=saberi_i_prikazi)
saberi_button.grid(row=5, columnspan=2)

oduzmi_button = tk.Button(root, text="Oduzmi Matrice", command=oduzmi_i_prikazi)
oduzmi_button.grid(row=6, columnspan=2)

pomnozi_button = tk.Button(root, text="Pomnoži Matrice", command=pomnozi_matrice)
pomnozi_button.grid(row=7, columnspan=2)

transponuj_button = tk.Button(root, text="Transponuj Prvu Matricu", command=lambda: transponuj_i_prikazi(matrica1))
transponuj_button.grid(row=8, columnspan=2)

root.mainloop()
