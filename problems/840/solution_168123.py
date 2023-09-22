'''retorna quantidade de ingredientes necessariosnpara dois bolos'''
'''a=farinha; b=ovos; c=leite'''
def bolos(A,B,C):
    far= A // 2
    ovos= B // 3
    leite= C // 5
    return min(far,ovos,leite)