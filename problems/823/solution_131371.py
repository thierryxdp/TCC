def faltante(L):
    '''funçao que dada uma lista com uma sequencia de numeros
    retorna o numero que esta faltando'''
    L.sort()
    contador = 0
    while contador < len(L):
        if L[contador] == contador+1:
            return contador+1
        contador +=1
    return contador+1