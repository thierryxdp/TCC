import math
def bolos(farinha,ovos,leite):
    """define o numero de bolos que se pode fazer com os ingredientes fornecidos dividindo a quantidade fornecida pelo necessario para fazer o bolo limitando a quantidade de bolos a serem feitos pelo menor numro; int, int, int->int"""
    nfarinha = (farina //2)
    novos = (ovos//3)
    nleite = (leite//5)
    nbolos = min(nfarinha,novos,nleite)
    return nbolos