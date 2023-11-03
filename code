mesas_consumo = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}

def criar_registro(numero_mesa, nome_cliente, valor_consumido):
    if numero_mesa in mesas_consumo:
        if nome_cliente in mesas_consumo[numero_mesa]:
            mesas_consumo[numero_mesa][nome_cliente] += valor_consumido
        else:
            mesas_consumo[numero_mesa][nome_cliente] = valor_consumido
        print(f"Registro de {nome_cliente} na mesa {numero_mesa} criado com sucesso!")
    else:
        print(f"Mesa {numero_mesa} não encontrada.")

def calcular_total_consumo(numero_mesa):
    if numero_mesa in mesas_consumo:
        total = sum(mesas_consumo[numero_mesa].values())
        return total
    else:
        return 0.0

def ler_registros(numero_mesa):
    if numero_mesa in mesas_consumo:
        if mesas_consumo[numero_mesa]:
            print(f"Consumo na mesa {numero_mesa}:")
            for cliente, valor in mesas_consumo[numero_mesa].items():
                print(f"{cliente}: R${valor:.2f}")
            total_consumo = calcular_total_consumo(numero_mesa)
            print(f"Total de consumo na mesa {numero_mesa}: R${total_consumo:.2f}")
        else:
            print(f"Não há registros de consumo disponíveis para a mesa {numero_mesa}.")
    else:
        print(f"Mesa {numero_mesa} não encontrada.")

def atualizar_registro(numero_mesa, nome_cliente, novo_valor):
    if numero_mesa in mesas_consumo:
        if nome_cliente in mesas_consumo[numero_mesa]:
            mesas_consumo[numero_mesa][nome_cliente] = novo_valor
            print(f"Registro de {nome_cliente} na mesa {numero_mesa} atualizado com sucesso!")
        else:
            print(f"Cliente {nome_cliente} não encontrado na mesa {numero_mesa}.")
    else:
        print(f"Mesa {numero_mesa} não encontrada.")

def excluir_registro(numero_mesa, nome_cliente):
    if numero_mesa in mesas_consumo:
        if nome_cliente in mesas_consumo[numero_mesa]:
            del mesas_consumo[numero_mesa][nome_cliente]
            print(f"Registro de {nome_cliente} na mesa {numero_mesa} excluído com sucesso!")
        else:
            print(f"Cliente {nome_cliente} não encontrado na mesa {numero_mesa}.")
    else:
        print(f"Mesa {numero_mesa} não encontrada.")

def main():
    while True:
        print("\nSistema de Controle de Consumo de Restaurante")
        print("1. Criar Registro")
        print("2. Ler Registros")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "1":
            numero_mesa = int(input("Número da mesa (1-6): "))
            if numero_mesa >= 1 and numero_mesa <= 6:
                nome_cliente = input("Nome do cliente: ")
                valor_consumido = float(input("Valor consumido: "))
                criar_registro(numero_mesa, nome_cliente, valor_consumido)
            else:
                print("Mesa inválida. Escolha uma mesa de 1 a 6.")
        elif escolha == "2":
            numero_mesa = int(input("Número da mesa (1-6): "))
            if numero_mesa >= 1 and numero_mesa <= 6:
                ler_registros(numero_mesa)
            else:
                print("Mesa inválida. Escolha uma mesa de 1 a 6.")
        elif escolha == "3":
            numero_mesa = int(input("Número da mesa (1-6): "))
            if numero_mesa >= 1 and numero_mesa <= 6:
                nome_cliente = input("Nome do cliente a ser atualizado: ")
                novo_valor = float(input("Novo valor consumido: "))
                atualizar_registro(numero_mesa, nome_cliente, novo_valor)
            else:
                print("Mesa inválida. Escolha uma mesa de 1 a 6.")
        elif escolha == "4":
            numero_mesa = int(input("Número da mesa (1-6): "))
            if numero_mesa >= 1 and numero_mesa <= 6:
                nome_cliente = input("Nome do cliente a ser excluído: ")
                excluir_registro(numero_mesa, nome_cliente)
            else:
                print("Mesa inválida. Escolha uma mesa de 1 a 6.")
        elif escolha == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
