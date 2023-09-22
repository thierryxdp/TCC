def carros(p,c):
    """Calcula a quantidade de carros necessária para transportar um total de p pessoas com c pessoas em cada carro;
    int,int->int"""
    if p%c==0:
        return p//c
    else:
        return p//c+1