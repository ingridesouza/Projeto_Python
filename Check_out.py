import tkinter as tk
from tkinter import *

class CheckOut:
    def __init__(self):
        self.consumo_clientes = {}

    def adicionar_consumo(self, nome_cliente, valor_unitario, quantidade_pessoas, dia_pagamento):
        valor_total = valor_unitario / quantidade_pessoas

        if nome_cliente in self.consumo_clientes:
            self.consumo_clientes[nome_cliente]['valor'] += valor_total
        else:
            self.consumo_clientes[nome_cliente] = {'valor': valor_total, 'dia_pagamento': dia_pagamento}

    def tela_pagamento(self):
        master = tk.Tk()
        master.title("Sistema de Controle de Consumo de Restaurante")
        master.geometry("200x480")

        titulo_tela_um1 = Label(master, text="Valor total a ser pago", font=(20), bg="dark blue", fg="white",)
        titulo_tela_um1.pack()
        titulo_tela_um1.place(x=70, y=30)

        name_entry = Entry(master, width=22, font=(15))
        name_entry.pack()
        name_entry.place(x=70, y=50)

        valor_pago_label = tk.Label(master, text="Valor por pessoa: ")
        valor_pago_label.grid(row=2, column=0)

        def adicionar_consumo_callback():
            nome_cliente = name_entry.get()
            valor_unitario = 50  
            quantidade_pessoas = 1  
            dia_pagamento = "01/01/2023"  
            
            self.adicionar_consumo(nome_cliente, valor_unitario, quantidade_pessoas, dia_pagamento)

            
            valor_pago_label.config(text=f"Valor por pessoa: {self.consumo_clientes[nome_cliente]['valor']}")

        
        adicionar_consumo_button = Button(master, text="Adicionar Consumo", command=adicionar_consumo_callback)
        adicionar_consumo_button.pack()
        adicionar_consumo_button.place(x=70, y=80)

        master.mainloop()


check_out = CheckOut()


check_out.tela_pagamento()

