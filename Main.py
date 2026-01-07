from cliente import Cliente
from conta import Conta


def main():
    cliente1 = Cliente("Robinho", "119999-8888")
    cliente2 = Cliente("Maria", "118888-7777")

    conta1 = Conta(cliente1, 1222)
    conta2 = Conta(cliente2, 1333)

    while True:
        print("===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Transferir")
        print("4 - Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: "))
            conta1.depositar(valor)

        elif opcao == "2":
            valor = float(input("Valor do saque: "))
            conta1.sacar(valor)

        elif opcao == "3":
            valor = float(input("Valor da transferência: "))
            conta1.transferir(valor, conta2)

        elif opcao == "4":
            conta1.extrato()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
