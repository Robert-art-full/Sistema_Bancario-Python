class Conta:
    def __init__(self, titular, numero: int, saldo: float = 0.0):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._historico = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            print("❌ O valor do depósito deve ser positivo.")
            return

        self._saldo += valor
        self._historico.append(f"Depósito: R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            print("❌ O valor do saque deve ser positivo.")
            return

        if valor > self._saldo:
            print("❌ Saldo insuficiente.")
            return

        self._saldo -= valor
        self._historico.append(f"Saque: R$ {valor:.2f}")
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

    def transferir(self, valor: float, conta_destino) -> None:
        if valor <= 0:
            print("❌ O valor da transferência deve ser positivo.")
            return

        if valor > self._saldo:
            print("❌ Saldo insuficiente para transferência.")
            return

        self._saldo -= valor
        conta_destino.depositar(valor)
        self._historico.append(
            f"Transferência enviada: R$ {valor:.2f} → Conta {conta_destino._numero}"
        )
        print("✅ Transferência realizada com sucesso.")

    def extrato(self) -> None:
        print("\n📄 EXTRATO BANCÁRIO")
        print(f"Titular: {self._titular}")
        print(f"Conta: {self._numero}")
        print("Movimentações:")

        if not self._historico:
            print("- Nenhuma movimentação registrada.")
        else:
            for item in self._historico:
                print(f"- {item}")

        print(f"Saldo atual: R$ {self._saldo:.2f}\n")
