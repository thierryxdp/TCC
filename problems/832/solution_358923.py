def eh_quadrada(matriz):
    """função que dada uma matriz de enrada, retorna se ela é quadrada ou não;list-->bool"""
    x=[]
    y=[]
    if len(matriz)==0:
        return True
    x=len(matriz)
    y=len(matriz[0])
    if x==y:
        return True
    else:
        return False