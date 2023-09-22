def filtraMultiplos(lista, m):
    
    """ Dado uma lista de inteiros, testa de um a um se são múltiplos de um número m
    assinatura: lista, int -> lista
    casos de teste:
    filtraMultiplos([1,2,3,4,5,6,7,8], 2) -> [2,4,6,8]
    """
    
    contador = 0
    acumulador = []
    
    while contador < len(lista):
        if lista[contador] % m == 0:
            acumulador = acumulador + [lista[contador]]
            
        contador = contador + 1

    return acumulador