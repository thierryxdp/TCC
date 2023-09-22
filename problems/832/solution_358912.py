def eh_quadrada(matriz):
    """função que dada uma matriz de enrada, retorna se ela é quadrada ou não;list-->bool"""
    x=[]
    y=[]
    for i in matriz:
        if len(matriz)==0:
            return True
        if x==y:
            return False
    else:
        return False