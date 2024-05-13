import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import gtts
import speech_recognition as sr
from win32com.client import Dispatch


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.configure(background='white')
        self.resizable(width=False, height=False)
        self.geometry("480x568+450+90")
        
        self.calc_frame = tk.Frame(self)
        self.calc_frame.grid()

        self.calc = Calc(self.calc_frame)

class Calc:
    def __init__(self, master):
        self.master = master
        self.total = 0
        self.current = ''
        self.input_value = True  
        self.check_sum = False
        self.op = ''
        self.result = False

        self.create_widgets()

    def create_widgets(self):
        self.txtDisplay = tk.Entry(self.master, font=('Helvetica', 20, 'bold'),bg='black', fg='white',bd=30, width=28, justify=tk.RIGHT)
        self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
        self.txtDisplay.insert(0, "0")

        numberpad = "789456123"
        i = 0
        self.btn = []
        for j in range(2, 5):
            for k in range(3):
                self.btn.append(tk.Button(self.master, width=6, height=2,bg='black', fg='white',font=('Helvetica', 20, 'bold'),bd=4, text=numberpad[i]))
                self.btn[i].grid(row=j, column=k, pady=1)
                self.btn[i]["command"] = lambda x=numberpad[i]: self.numberEnter(x)
                i += 1

        self.btnClear = tk.Button(self.master, text=chr(67), width=6,height=2, bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=self.Clear_Entry)
        self.btnClear.grid(row=1, column=0, pady=1)

        self.btnAllClear = tk.Button(self.master, text=chr(67) + chr(69),width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4,command=self.All_Clear_Entry)
        self.btnAllClear.grid(row=1, column=1, pady=1)

        self.btnsq = tk.Button(self.master, text="\u221A", width=6, height=2,bg='powder blue', font=('Helvetica',20, 'bold'),bd=4, command=self.squared)
        self.btnsq.grid(row=1, column=2, pady=1)

        self.btnAdd = tk.Button(self.master, text="+", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.operation("add"))
        self.btnAdd.grid(row=1, column=3, pady=1)

        self.btnSub = tk.Button(self.master, text="-", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.operation("sub"))
        self.btnSub.grid(row=2, column=3, pady=1)

        self.btnMul = tk.Button(self.master, text="x", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.operation("multi"))
        self.btnMul.grid(row=3, column=3, pady=1)

        self.btnDiv = tk.Button(self.master, text="/", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.operation("divide"))
        self.btnDiv.grid(row=4, column=3, pady=1)

        self.btnZero = tk.Button(self.master, text="0", width=6, height=2,bg='black', fg='white',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.numberEnter(0))
        self.btnZero.grid(row=5, column=0, pady=1)

        self.btnDot = tk.Button(self.master, text=".", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=lambda: self.numberEnter("."))
        self.btnDot.grid(row=5, column=1, pady=1)

        self.btnPM = tk.Button(self.master, text=chr(177), width=6, height=2,bg='powder blue', font=('Helvetica', 20, 'bold'),bd=4, command=self.mathPM)
        self.btnPM.grid(row=5, column=2, pady=1)

        self.btnEquals = tk.Button(self.master, text="=", width=6, height=2,bg='powder blue',font=('Helvetica', 20, 'bold'),bd=4, command=self.sum_of_total)
        self.btnEquals.grid(row=5, column=3, pady=1)


    def numberEnter(self, num):
        self.result = False
        firstnum = self.txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(self.txtDisplay.get())

    def display(self, value):
        self.txtDisplay.delete(0, tk.END)
        self.txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(self.txtDisplay.get()))
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(self.txtDisplay.get()))
        self.display(self.current)


class MatrixWindow(tk.Toplevel): 
    def __init__(self, master):
        super().__init__(master)
        self.title("Matrix Operations")
        self.config(background="powder blue")
        self.resizable(width=False, height=False)
        self.geometry("480x568+450+90")
        self.create_widgets()

        self.matrica1 = None
        self.matrica2 = None

    def create_widgets(self):
        label_vrste = tk.Label(self, text="Unesite broj vrsta:",font=('Helvetica', 15, 'bold'),background="powder blue",fg="black")
        label_vrste.grid(row=0, column=0)
        self.entry_vrste = tk.Entry(self,background="dark gray",font=('Helvetica', 10, 'bold'))
        self.entry_vrste.grid(row=0, column=1)

        label_kolone = tk.Label(self, text="Unesite broj kolona:",font=('Helvetica', 15, 'bold'),background="powder blue",fg="black")
        label_kolone.grid(row=1, column=0)
        self.entry_kolone = tk.Entry(self,background="dark gray",font=('Helvetica', 10, 'bold'))
        self.entry_kolone.grid(row=1, column=1)

        label_elementi = tk.Label(self, text="Unesite elemente redom po vrsti \n (razdvojene sa space):",font=('Helvetica', 15, 'bold'),background="powder blue",fg="black")
        label_elementi.grid(row=2, column=0)
        self.entry_elementi = tk.Entry(self,background="dark gray",font=('Helvetica', 10, 'bold'))
        self.entry_elementi.grid(row=2, column=1)

        kreiraj_button1 = tk.Button(self, text="Kreiraj Prvu Matricu", command=self.kreiraj_matricu1,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        kreiraj_button1.grid(row=3, columnspan=2)

        kreiraj_button2 = tk.Button(self, text="Kreiraj Drugu Matricu", command=self.kreiraj_matricu2,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        kreiraj_button2.grid(row=4, columnspan=2)

        saberi_button = tk.Button(self, text="Saberi Matrice", command=self.saberi_i_prikazi,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        saberi_button.grid(row=5, columnspan=2)

        oduzmi_button = tk.Button(self, text="Oduzmi Matrice", command=self.oduzmi_i_prikazi,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        oduzmi_button.grid(row=6, columnspan=2)

        pomnozi_button = tk.Button(self, text="Pomnoži Matrice", command=self.pomnozi_matrice,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        pomnozi_button.grid(row=7, columnspan=2)

        transponuj_button = tk.Button(self, text="Transponuj Prvu Matricu", command=self.transponuj_i_prikazi,font=('Helvetica', 15, 'bold'),background="black",fg="white")
        transponuj_button.grid(row=8, columnspan=2)

    def kreiraj_matricu1(self):
        self.matrica1 = self.kreiraj_matricu()
        self.prikazi_matricu(self.matrica1)

    def kreiraj_matricu2(self):
        self.matrica2 = self.kreiraj_matricu()
        self.prikazi_matricu(self.matrica2)

    def kreiraj_matricu(self):
        vrste = int(self.entry_vrste.get())
        kolone = int(self.entry_kolone.get())
        unos_elementi = list(map(int, self.entry_elementi.get().split()))
        matrica = [unos_elementi[i:i + kolone] for i in range(0, len(unos_elementi), kolone)]
        return matrica

    def saberi_i_prikazi(self):
        if self.matrica1 is not None and self.matrica2 is not None:
            rezultat = self.saberi_matrice(self.matrica1, self.matrica2)
            self.prikazi_matricu(rezultat)
        else:
            print("Nisu unesene obje matrice!")

    def oduzmi_i_prikazi(self):
        if self.matrica1 is not None and self.matrica2 is not None:
            rezultat = self.oduzmi_matrice(self.matrica1, self.matrica2)
            self.prikazi_matricu(rezultat)
        else:
            print("Nisu unesene obje matrice!")

    def pomnozi_matrice(self):
        if self.matrica1 is not None and self.matrica2 is not None:
            rezultat = np.dot(self.matrica1, self.matrica2)
            self.prikazi_matricu(rezultat)
        else:
            print("Nisu unesene obje matrice!")

    def saberi_matrice(self, matrica1, matrica2):
        if len(matrica1) != len(matrica2) or len(matrica1[0]) != len(matrica2[0]):
            print("Matrice moraju biti istih dimenzija za sabiranje!")
            return None
        
        rezultat = [[matrica1[i][j] + matrica2[i][j] for j in range(len(matrica1[0]))] for i in range(len(matrica1))]
        return rezultat

    def oduzmi_matrice(self, matrica1, matrica2):
        if len(matrica1) != len(matrica2) or len(matrica1[0]) != len(matrica2[0]):
            print("Matrice moraju biti istih dimenzija za oduzimanje!")
            return None
        
        rezultat = [[matrica1[i][j] - matrica2[i][j] for j in range(len(matrica1[0]))] for i in range(len(matrica1))]
        return rezultat

    def prikazi_matricu(self, matrica):
        top = tk.Toplevel()
        top.title("Matrica")
        
        for i in range(len(matrica)):
            for j in range(len(matrica[0])):
                label = tk.Label(top, text=str(matrica[i][j]), borderwidth=0, width=10, height=3, font=("Helvetica", 12))
                label.grid(row=i, column=j)

    def transponuj_i_prikazi(self):
        if self.matrica1 is not None:
            transponovana_matrica = np.transpose(self.matrica1)
            self.prikazi_matricu(transponovana_matrica)
        else:
            print("Nije uneta matrica!")

class GeometricCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Geometric Calculator with Voice")
        self.resizable(width=False, height=False)
        self.geometry("480x568+450+90")
        # Varijable za oblik i rezultate
        self.shape_var = tk.StringVar(self)
        self.shape_var.set("cylinder")  # Početni oblik
        self.result_text = tk.StringVar(self)
        
        # Postavljanje UI
        self.create_widgets()

    def create_widgets(self):
        # Izbor oblika
        tk.Label(self, text="Select Shape:",background="powder blue",font=('Helvetica', 20, 'bold')).pack()
        shape_menu = tk.OptionMenu(self, self.shape_var, "cylinder", "sphere", "cone", "prism", "pyramid")
        shape_menu.config(bg="black",fg="white",font=("Helvetica", 12, "bold"))
        shape_menu.pack()

        # Ulazi za podatke
        self.configure(background="powder blue")
        self.create_input_fields()
        
        # Dugme za izračunavanje
        calculate_button = tk.Button(self, text="Calculate", command=self.calculate,background="black",fg="white",font=('Helvetica', 18, 'bold'))
        calculate_button.pack()
        
        # Dugme za glasovne komande
        voice_button = tk.Button(self, text="Use Voice Command", command=self.listen,background="black",fg="white",font=('Helvetica', 18, 'bold'))
        voice_button.pack()

        # Rezultat
        result_label = tk.Label(self, textvariable=self.result_text)
        result_label.pack()

    def create_input_fields(self):
        self.fields = {}
        
        # Polja za unos
        fields_info = [
            ("Radius:", "radius"),
            ("Height:", "height"),
            ("Slant Height (if needed):", "slant_height"),
            ("Base Area (if needed):", "base_area"),
            ("Perimeter (if needed):", "perimeter")]
        
        for label_text, field_name in fields_info:
            tk.Label(self, text=label_text,background="powder blue",font=("Helvetica", 12, "bold")).pack()
            entry = tk.Entry(self)
            entry.config(background="dark gray",font=("Helvetica", 12, "bold"))
            entry.pack()
            self.fields[field_name] = entry

   

    def speak(self, message):
        speaker = Dispatch("SAPI.SpVoice")
        speaker.Speak(message)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Speak now")
            audio = r.listen(source)
            
            try:
                command = r.recognize_google(audio)
                self.speak(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                self.speak("Sorry, I could not understand the command")
                return ""

    def calculate(self):
        shape = self.shape_var.get().lower()
        
        try:
            if shape == "cylinder":
                radius = float(self.fields["radius"].get())
                height = float(self.fields["height"].get())
                lateral_area = 2 * math.pi * radius * height
                surface_area = 2 * math.pi * radius**2 + lateral_area
                volume = math.pi * radius**2 * height
                result = f"Lateral Area: {lateral_area:.2f}, Surface Area: {surface_area:.2f}, Volume: {volume:.2f}"
            
            elif shape == "sphere":
                radius = float(self.fields["radius"].get())
                surface_area = 4 * math.pi * radius**2
                volume = 4/3 * math.pi * radius**3
                result = f"Surface Area: {surface_area:.2f}, Volume: {volume:.2f}"
            
            elif shape == "cone":
                radius = float(self.fields["radius"].get())
                height = float(self.fields["height"].get())
                slant_height = float(self.fields["slant_height"].get())
                lateral_area = math.pi * radius * slant_height
                surface_area = math.pi * radius**2 + lateral_area
                volume = 1/3 * math.pi * radius**2 * height
                result = f"Lateral Area: {lateral_area:.2f}, Surface Area: {surface_area:.2f}, Volume: {volume:.2f}"
            
            elif shape == "prism":
                base_area = float(self.fields["base_area"].get())
                height = float(self.fields["height"].get())
                perimeter = float(self.fields["perimeter"].get())
                lateral_area = perimeter * height
                surface_area = 2 * base_area + lateral_area
                volume = base_area * height
                result = f"Lateral Area: {lateral_area:.2f}, Surface Area: {surface_area:.2f}, Volume: {volume:.2f}"
            
            elif shape == "pyramid":
                base_area = float(self.fields["base_area"].get())
                height = float(self.fields["height"].get())
                slant_height = float(self.fields["slant_height"].get())
                perimeter = float(self.fields["perimeter"].get())
                lateral_area = (perimeter * slant_height) / 2
                surface_area = base_area + lateral_area
                volume = 1/3 * base_area * height
                result = f"Lateral Area: {lateral_area:.2f}, Surface Area: {surface_area:.2f}, Volume: {volume:.2f}"
            
            else:
                raise ValueError("Invalid shape")
            
            self.result_text.set(result)
            self.speak(f"Calculation completed for {shape}. {result}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all required fields.")


class EquationSolverWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Rješavač Linearne Jednačine")
        self.master.configure(bg='#F0F0F0')  # Postavljanje boje pozadine
        self.resizable(width=False, height=False)
        self.geometry("480x568+450+90")

        self.frame = tk.Frame(self.master, padx=10, pady=10, bg='powder blue')  # Dodavanje boje okviru
        self.frame.pack()

        self.label_jednacina = tk.Label(self.frame, text="Unesite jednačinu (npr. 'ax + b = cx + d'):", bg='powder blue', fg='black', font=("Helvetica", 12, "bold"))  # Dodavanje boje labeli
        self.label_jednacina.grid(row=0, column=0, sticky="w")

        self.unos_jednacine = tk.Entry(self.frame, width=30)
        self.unos_jednacine.grid(row=0, column=1)

        self.dugme_rjesi = tk.Button(self.frame, text="Rješi", command=self.rjesi_jednacinu, bg='dark gray', fg='black', font=("Helvetica", 12, "bold"))  # Dodavanje boja dugmetu
        self.dugme_rjesi.grid(row=1, column=1, pady=10)

    def rjesi_jednacinu(self):
        try:
            jednacina = self.unos_jednacine.get()
            if "=" not in jednacina:
                raise ValueError("Nevažeći format jednačine. Molimo koristite formu 'ax + b = cx + d'")
            
            # Razdvajanje jednačine na lijevi i desni dio
            lijevi_dio, desni_dio = jednacina.split("=")
            
            # Parsiranje koeficijenata i konstanti
            a, b = self.parsiraj_stranu(lijevi_dio.strip())
            c, d = self.parsiraj_stranu(desni_dio.strip())
            
            # Rješavanje jednačine
            x = (d - b) / (a - c)
            
            messagebox.showinfo("Rješenje", f"Rješenje je: x = {x}")
        except Exception as e:
            messagebox.showerror("Greška", f"Došlo je do greške: {str(e)}")

    def parsiraj_stranu(self, strana):
        # Parsiranje koeficijenata i konstanti sa strane jednačine
        # Pretpostavka: Imamo linearnu jednačinu u obliku 'ax + b'
        dijelovi = strana.split("x")
        a = int(dijelovi[0].strip()) if dijelovi[0].strip() else 1
        b = int(dijelovi[1].strip()) if dijelovi[1].strip() else 0
        return a, b


class EquationSolverWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Rješavač Linearne Jednačine")
        self.master.configure(bg='#F0F0F0')  # Postavljanje boje pozadine
        

        self.frame = tk.Frame(self.master, padx=10, pady=10, bg='powder blue')  # Dodavanje boje okviru
        self.frame.pack()

        self.label_jednacina = tk.Label(self.frame, text="Unesite jednačinu (npr. 'ax + b = cx + d'):", bg='powder blue', fg='black', font=("Helvetica", 12, "bold"))  # Dodavanje boje labeli
        self.label_jednacina.grid(row=0, column=0, sticky="w")

        self.unos_jednacine = tk.Entry(self.frame, width=30,background="dark gray",font=("Helvetica", 12, "bold"))
        self.unos_jednacine.grid(row=0, column=1)

        self.dugme_rjesi = tk.Button(self.frame, text="Rješi", command=self.rjesi_jednacinu, bg='black', fg='white', font=("Helvetica", 18, "bold"))  # Dodavanje boja dugmetu
        self.dugme_rjesi.grid(row=1, column=1, pady=10)

    def rjesi_jednacinu(self):
        try:
            jednacina = self.unos_jednacine.get()
            if "=" not in jednacina:
                raise ValueError("Nevažeći format jednačine. Molimo koristite formu 'ax + b = cx + d'")
            
            # Razdvajanje jednačine na lijevi i desni dio
            lijevi_dio, desni_dio = jednacina.split("=")
            
            # Parsiranje koeficijenata i konstanti
            a, b = self.parsiraj_stranu(lijevi_dio.strip())
            c, d = self.parsiraj_stranu(desni_dio.strip())
            
            # Rješavanje jednačine
            x = (d - b) / (a - c)
            
            messagebox.showinfo("Rješenje", f"Rješenje je: x = {x}")
        except Exception as e:
            messagebox.showerror("Greška", f"Došlo je do greške: {str(e)}")

    def parsiraj_stranu(self, strana):
        # Parsiranje koeficijenata i konstanti sa strane jednačine
        # Pretpostavka: Imamo linearnu jednačinu u obliku 'ax + b'
        dijelovi = strana.split("x")
        a = int(dijelovi[0].strip()) if dijelovi[0].strip() else 1
        b = int(dijelovi[1].strip()) if dijelovi[1].strip() else 0
        return a, b



class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("480x568+450+90")
        self.configure(background="powder blue")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Odaberite opciju:",background="powder blue",fg="black",font=("Helvetica", 20, "bold")).pack()
        tk.Button(self, text="Kalkulator", command=self.open_calculator,background="black",fg="white",font=("Helvetica", 20, "bold")).pack()
        tk.Button(self, text="Matrice", command=self.open_matrix_operations,background="black",fg="white",font=("Helvetica", 20, "bold")).pack()
        tk.Button(self, text="Geometrija", command=self.open_geometry_calculator,background="black",fg="white",font=("Helvetica", 20, "bold")).pack()
        tk.Button(self, text="Jednacina", command=self.open_equation_solver,background="black",fg="white",font=("Helvetica", 20, "bold")).pack()

    def open_calculator(self):
        calculator_window = Calculator()
       
    def open_matrix_operations(self):
        matrix_window = MatrixWindow(self)

    def open_geometry_calculator(self):
        geometry_window = GeometricCalculator()
    
    def open_equation_solver(self):
        equation_window = tk.Toplevel(self)
        EquationSolverWindow(equation_window)


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()