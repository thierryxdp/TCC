from math import*
def carros (p,y=5):
    """função que calcula o número exato de carros necessarios para realizar uma viagem com grupo com p pessoas; espera-se que com parametros inteiros o resultado será tambem inteiro"""
    return ceil (p/y)