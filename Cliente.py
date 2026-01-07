class Cliente:
    def __init__(self, nome: str, telefone: str):
        self._nome = nome
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def telefone(self) -> str:
        return self._telefone

    def __str__(self) -> str:
        return f"{self._nome} | Tel: {self._telefone}"
