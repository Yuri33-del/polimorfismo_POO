class Carro:
    def __int__(self, velocidade_inicial):
        self.velocidade = velocidade_inicial

    def acelera(self):
        self.velocidade += 1

    def freia(self):
        self.velocidade -= 1

    def exibe_velocidade(self):
        print(f"velocidade atual: {self.velocidade} km/h")
