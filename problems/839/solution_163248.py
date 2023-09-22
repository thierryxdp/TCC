def carros(Pessoas,Capacidade=5):
    "Fução que calcula a quantidade de carros necessários para transportar uma quantidade de passageiros dada a capacidade que cada carro"
    return math.ceil(Pessoas/Capacidade)