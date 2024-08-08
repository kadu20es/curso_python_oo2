from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindros):
        super().__init__(marca, modelo)
        self.cilindros = cilindros

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"""Modelo: {self.modelo}
        Marca: {self.marca}
        Cilindros: {self.cilindros}
        Status: {status}"""
    