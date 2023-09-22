def carros (p,nc=5):
    "funcao que calcula o numero exato de carros necessarios para a viagem dado o numero de pessoas n e e o numero de pessoas que cabem no carro nc"
    return max(p/nc)