def carros(p,c=5):
    """calcula o número de carros necessários para levar p pessoas em carros com c capacidade
    int,int->float"""
    return p//c + 1*(p%c)