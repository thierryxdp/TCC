def carros(p, c):
    """calcula a quantidade de carros necessarios dados o numero de pessoas e a capacidade deles"""
    if (p%c==0):
        return p/2
    else (p%c!=0):
        return (p//c)+1