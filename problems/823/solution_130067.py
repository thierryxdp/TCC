def faltante(lista):
    """Funcao que, dado uma lista to tamanho N-1 contendo os números de 1 a N, descobre qual número esta faltando
    lista-->int"""
    i=1
    numerofaltante=0
    auxiliar=list(range(1,lista[-1]+1))
    if lista[0]!=1:
        return  1
    elif lista==auxiliar:
        reuturn lista[-1]+1
    while i<len(lista):
        if lista[i]-lista[i-1]!=1:
            numerofaltante=numerofaltante+lista[i]-1
        i=i+1
    return numerofaltante