def faltante(L):
    '''funçao que dada uma lista com uma sequencia de numeros
    retorna o numero que esta faltando'''
    contador = 1
    while contador < len(L):
        if L[contador-1] == contador:
            return contador-1
        contador +=1
    return contador