from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    # overrde the acelera method
    def acelera(self):
        self.velocidade += 5
        print("Aceleração de corrida! A velocidade aumento em 5 km/h")
