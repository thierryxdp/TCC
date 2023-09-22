def faltante(lista):
    '''função que retorna o valor faltante 
    numa lista:
    valor de entrada: list
    valor de saída: int'''
    lista2=lista.sort()
    n=len(lista2)+1
    while n > len(L):
        if n not in L:
            return n
        n=n-1