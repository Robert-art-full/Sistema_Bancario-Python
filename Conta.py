class Conta:
    def __init__(self, titular, numero, saldo: float = 0.0):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return

        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return

        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self) -> None:
        print(
            f"Titular: {self._titular} | "
            f"Conta: {self._numero} | "
            f"Saldo: R$ {self._saldo:.2f}"
        )
