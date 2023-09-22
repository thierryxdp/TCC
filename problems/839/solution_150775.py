def carros(p,c=5):
    #quantidade de carros p uma viagem dado o numero de pessoas e a capacidade do carro(se não for 5).
    x = p/c
    y = math.ceil(x)
    return y