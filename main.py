
import tkinter as tk

mesas_consumo = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}

def criar_registro():
    numero_mesa = int(mesa_entry.get())
    nome_cliente = cliente_entry.get()
    valor_consumido = float(valor_entry.get())
    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if nome_cliente in mesas_consumo[numero_mesa]:
                mesas_consumo[numero_mesa][nome_cliente] += valor_consumido
            else:
                mesas_consumo[numero_mesa][nome_cliente] = valor_consumido
            result_label.config(text=f"Registro de {nome_cliente} na mesa {numero_mesa} criado com sucesso!")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def ler_registros():
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
    if numero_mesa in mesas_consumo:
        total = sum(mesas_consumo[numero_mesa].values())
        return total
    else:
        return 0.0

def atualizar_registro():
    numero_mesa = int(mesa_entry.get())
    nome_cliente = cliente_entry.get()
    novo_valor = float(valor_entry.get())
    if numero_mesa >= 1 and numero_mesa <= 6:
        if numero_mesa in mesas_consumo:
            if nome_cliente in mesas_consumo[numero_mesa]:
                mesas_consumo[numero_mesa][nome_cliente] = novo_valor
                result_label.config(text=f"Registro de {nome_cliente} na mesa {numero_mesa} atualizado com sucesso!")
            else:
                result_label.config(text=f"Cliente {nome_cliente} não encontrado na mesa {numero_mesa}.")
        else:
            result_label.config(text=f"Mesa {numero_mesa} não encontrada.")
    else:
        result_label.config(text="Mesa inválida. Escolha uma mesa de 1 a 6.")

def excluir_registro():
    numero_mesa = int(mesa_entry.get())
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

def sair():
    root.destroy()

root = tk.Tk()
root.title("Sistema de Controle de Consumo de Restaurante")


mesa_label = tk.Label(root, text="Número da mesa (1-6):")
mesa_label.pack()

mesa_entry = tk.Entry(root)
mesa_entry_entry = tk.Entry(width=18)
mesa_entry.pack()

cliente_label = tk.Label(root, text="Nome do cliente:")
cliente_label.pack()


cliente_entry = tk.Entry(root)
cliente_entry = tk.Entry(width=18)
cliente_entry.pack()

valor_label = tk.Label(root, text="Valor consumido:")
valor_label.pack()

valor_entry = tk.Entry(root)
valor_label = tk.Entry(width=18)
valor_entry.pack()

criar_button = tk.Button(root, width = 17, height = 2, text="Criar Comanda", command=criar_registro, background="white")
criar_button.pack()

atualizar_button = tk.Button(root, width = 17, height = 2, text="Adicionar Registro", command=atualizar_registro, background="white")
atualizar_button.pack()

ler_button = tk.Button(root, width = 17, height = 2, text="Valor total da mesa", command=ler_registros, background="white")
ler_button.pack()

excluir_button = tk.Button(root, width = 17, height = 2, text="Excluir Registro", command=excluir_registro, background="white")
excluir_button.pack()

sair_button = tk.Button(root, width = 17, height = 2, text="Sair", command=sair, background="white")
sair_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()