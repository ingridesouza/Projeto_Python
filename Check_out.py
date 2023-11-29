import tkinter as tk 
from tkinter import *

class check_out:
    def tela_pagamento():
        master = tk.Tk()
        master.title("Sistema de Controle de Consumo de Restaurante")
        master.geometry("200x480")

        tituloTelaUm1 = Label(master, text="Valor total a ser pago", font=(20), bg="dark blue", fg="white",)
        tituloTelaUm1.pack()
        tituloTelaUm1.place(x=70, y=30)

        nameEntry = Entry(master, width=22, font=( 15))
        nameEntry.pack()
        nameEntry.place(x=70, y=50)

        valor_pago_label = tk.Label(master, text="Valor por pessoa: ")
        valor_pago_label.grid(row=2, column=0)

        master.mainloop()
