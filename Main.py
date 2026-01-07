from Conta import Conta
from Cliente import Cliente


def main():
    # Criação do cliente
    cliente = Cliente(nome="Robinho", telefone="119999-8888")

    # Criação da conta vinculada ao cliente
    conta = Conta(titular=cliente, numero=1222)

    # Operações bancárias
    conta.depositar(100.0)
    conta.sacar(50.0)

    # Exibe extrato
    conta.extrato()


if __name__ == "__main__":
    main()
