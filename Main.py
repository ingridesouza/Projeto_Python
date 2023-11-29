import tkinter as tk
from tkinter import ttk
from Banco import *
from tkcalendar import DateEntry
from datetime import datetime
import os 

database = RoomDB()

def saveDates():
    with open('dates.txt', 'a') as f:
        checkin1 = checkin_date.get_date()
        f.write("{}".format(checkin1))
        f.close()

def openDates():
    with open('dates.txt', 'r') as f:
        for linha in f.readlines():
            checkin = linha.strip("\n")
            f.close
            return checkin
            

# Dicionário com a quantidade de mesa
mesas_consumo = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}

# Dicionário com os preços dos pratos
precos_pratos = {
    "Massa Carbonara": 20.0,
    "Frango Grelhado": 15.0,
    "Pizza Margherita": 18.0,
}

# Dicionário com os preços das bebidas
precos_bebidas = {
    "Água Mineral": 3.0,
    "Refrigerante": 5.0,
    "Suco Natural": 6.0,
}

def criar_registro():
    #função para criar o registro das pessoas nas mesas
    #variavel com o numero da mesa
    numero_mesa = int(mesa_entry.get())
    #variavel com  o nome do cliente
    nome_cliente = cliente_entry.get()
    #variavel do prato principal
    prato_principal = prato_principal_var.get()
    #variavel da bebida
    bebida = bebida_var.get()
    #variavel com preco do prato
    preco_prato = precos_pratos.get(prato_principal, 0.0)
    #variavel com o preco da bebida
    preco_bebida = precos_bebidas.get(bebida, 0.0)
    #variavel do valor consumido
    valor_consumido = preco_prato + preco_bebida

    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if nome_cliente in mesas_consumo[numero_mesa]:
                mesas_consumo[numero_mesa][nome_cliente] += valor_consumido
                    #insere o valor ocnsumido no banco 
                
            else:
                #check_in = checkin_date.get_date()
                saveDates()
                data_check_in = openDates()
                database.inserir_data(data_check_in)
                os.remove("dates.txt")

                mesas_consumo[numero_mesa][nome_cliente] = valor_consumido
                
                result_label.config(text=f"Registro de {nome_cliente} na mesa {numero_mesa} criado com sucesso!")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def ler_registros():
    #essa função retorna a conta da mesa, tanto de cada pessoa, quanto o total de cada mesa
    #variavel com o numero da mesa
    numero_mesa = int(mesa_entry.get())
    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if mesas_consumo[numero_mesa]:
                result_label.config(text=f"Consumo na mesa {numero_mesa}:\n")
                for cliente, valor in mesas_consumo[numero_mesa].items():
                    result_label.config(text=result_label.cget("text") + f"{cliente}: R${valor:.2f}\n")
                total_consumo = calcular_total_consumo(numero_mesa)
                result_label.config(text=result_label.cget("text") + f"Total de consumo na mesa {numero_mesa}: R${total_consumo:.2f}")
            else:
                result_label.config(text=f"Não há registros de consumo disponíveis para a mesa {numero_mesa}.")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def calcular_total_consumo(numero_mesa):
    #função que calcula o total do consumo
    if numero_mesa in mesas_consumo:
        total = sum(mesas_consumo[numero_mesa].values())
        return total
    else:
        return 0.0
    

def excluir_registro():
    #função que exclui o registro do cliente na mesa e tbm o registro da mesa no sistema
    #variavel com o numero da mesa
    numero_mesa = int(mesa_entry.get())
    #variavel com  o nome do cliente
    nome_cliente = cliente_entry.get()
    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if nome_cliente in mesas_consumo[numero_mesa]:
                del mesas_consumo[numero_mesa][nome_cliente]
                result_label.config(text=f"Registro de {nome_cliente} na mesa {numero_mesa} excluído com sucesso!")
            else:
                result_label.config(text=f"Cliente {nome_cliente} não encontrado na mesa {numero_mesa}.")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def adicionar_valor():
    #função de adicionar valor, para fazer um "novo pedido", ele vai somar com o valor q ja tem no registro
    #variavel com o numero da mesa
    numero_mesa = int(mesa_entry.get())
      #variavel com  o nome do cliente
    nome_cliente = cliente_entry.get()
    #variavel do valor adicional
    valor_adicional = float(valor_entry.get())
    
    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if nome_cliente in mesas_consumo[numero_mesa]:
                mesas_consumo[numero_mesa][nome_cliente] += valor_adicional
                result_label.config(text=f"Valor adicionado para {nome_cliente} na mesa {numero_mesa} com sucesso!")
            else:
                result_label.config(text=f"Cliente {nome_cliente} não encontrado na mesa {numero_mesa}.")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def sair():
    master.destroy()
    #para fechar a janela

master = tk.Tk()
master.title("Sistema de Controle de Consumo de Restaurante")
master.geometry("400x480")

titulo_label = tk.Label(master, text="Sistema de Controle de Consumo", font=("Helvetica", 16, "bold"), background='#E0E0E0')
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

mesa_label = tk.Label(master, text="Número da mesa (1-6):")
mesa_label.grid(row=1, column=0)

mesa_entry = tk.Entry(master)
mesa_entry.grid(row=1, column=1)

cliente_label = tk.Label(master, text="Nome do cliente:")
cliente_label.grid(row=2, column=0)

cliente_entry = tk.Entry(master)
cliente_entry.grid(row=2, column=1)

pratos_principais_options = ["Massa Carbonara", "Frango Grelhado", "Pizza Margherita"]
bebidas_options = ["Água Mineral", "Refrigerante", "Suco Natural"]

prato_principal_var = tk.StringVar(master)
prato_principal_var.set(pratos_principais_options[0])

bebida_var = tk.StringVar(master)
bebida_var.set(bebidas_options[0])

prato_principal_label = tk.Label(master, text="Pratos Principal:")
prato_principal_label.grid(row=4, column=0)

prato_principal_combobox = ttk.Combobox(master, textvariable=prato_principal_var, values=pratos_principais_options)
prato_principal_combobox.grid(row=4, column=1)

bebida_label = tk.Label(master, text="Bebidas:")
bebida_label.grid(row=5, column=0)

bebida_combobox = ttk.Combobox(master, textvariable=bebida_var, values=bebidas_options)
bebida_combobox.grid(row=5, column=1, pady=10)

valor_label = tk.Label(master, text="Outro valor?")
valor_label.grid(row=6, column=0, pady=2)

valor_entry = tk.Entry(master)
valor_entry.grid(row=6, column=1, pady=2)

criar_button = tk.Button(master, width=17, height=1, text="Criar Registro", command=criar_registro, background="white")
criar_button.grid(row=7, column=0)

adicionar_valor_button = tk.Button(master, width=17, height=1, text="Adicionar Valor", command=adicionar_valor, background="white")
adicionar_valor_button.grid(row=7, column=1)

ler_button = tk.Button(master, width=17, height=1, text="Fechar conta", command=ler_registros, background="white")
ler_button.grid(row=9, column=0, padx=(0, 5))  # Adiciona um espaço à direita do botão "Fechar conta"

# Botão "Excluir Registro"
excluir_button = tk.Button(master, width=17, height=1, text="Excluir Registro", command=excluir_registro, background="white")
excluir_button.grid(row=9, column=1)

# Botão "Sair"
sair_button = tk.Button(master, width=17, height=1, text="Sair", command=sair, background="white")
sair_button.grid(row=10, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(master, text="")
result_label.grid(row=11, column=0, columnspan=2)

checkin_date = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
checkin_date.grid(row=12, column=0, columnspan=2)
#checkin_date.place(x=100,y=150)

master.mainloop()
