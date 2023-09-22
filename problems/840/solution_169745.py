def bolos(farinha,ovos,leite):
    '''função que calcula quantos bolos joaozinho pode fazer dados a quantidade de ingredientes
    que possui.
    int, int, int -> int'''
    return min(farinha//2, ovos//3, leite//5)