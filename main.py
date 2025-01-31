from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo

if __name__ == "__main__":
    # Testando Carrointeligente
    carro_inteligente = CarroInteligente(10)
    print("Carro Inteligente:")
    carro_inteligente.acelera()
    carro_inteligente.exibe_velocidade()
    carro_inteligente.estaciona()
    print()

    # testando CarroEsportivo
    carro_esportivo = CarroEsportivo(50)
    print("Carro Esportivo:")
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.freia()
    carro_esportivo.exibe_velocidade()
