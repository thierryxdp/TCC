def carros(p,c=5):
    #quantidade de carros p uma viagem dado o numero de pessoas e a capacidade do carro(se não for 5).
    x = p%c
    y = p/c
    if x== 0:
        print (y)
    else:
        print (y+ 1)