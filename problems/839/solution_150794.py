def carros(p,c=5):
    #quantidade de carros p uma viagem dado o numero de pessoas e a capacidade do carro(se não for 5).
    x = p%c
    y = p/c
    z = abs(y)
    if x== 0:
        print (z)
    else:
        print (z + 1)