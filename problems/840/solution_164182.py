def bolos(a,b,c):
    """Função que calcula quantos bolos joão pode fazer"""
    #a = xícaras
    #b = ovos
    #c = leite
    import math
    bolo = ((a//2)+(b//3)+(c//5))//3
    if float(bolo):
        return int(bolo)
    else:
        return bolo