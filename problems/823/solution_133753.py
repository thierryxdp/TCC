def faltante(lista:list) -> int:
    """comentário"""
    i = 0
    N = lista[-1]
    n = 0
    lista_dois = list(range(1,N+1))
    while i < len(lista_dois):
        if lista_dois[i] not in lista:
            n = n+lista_dois[i]
        i+=1
    
    
    return n