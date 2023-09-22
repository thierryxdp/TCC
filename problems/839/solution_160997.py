def carros (p, c=5):
    """ calcule e retorne a quantidade de carros necessaria para que um grupo de amigos de quantidade p de pessoas possa ir viajar de carro, caso a capacidade do carro seja diferente de 5 pessoas, declare essa quantidade"""
    import math
    C= math.ceil p/c 
    return C