def carros(pessoa,carro=5):
    if pessoa/carro == 0:
        return pessoa/carro
    elif pessoa/carro > 0:
        return (pessoa/carro)+1
    else:
        return 0