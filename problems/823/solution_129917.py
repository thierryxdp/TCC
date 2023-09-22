def faltante(lista):
    """funcao que retorna o numero que falta em um intervalo numero de uma lista;
    list -> int"""

    lista.sort()
    i = 0
    n = lista[len(lista)-1]
    
    if lista[0] != 1:
        return 1
    
    if lista == list(range(1,n+1)):
                     
        return n + 1
    
    while i<len(lista)-1: