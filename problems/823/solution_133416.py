def faltante(lista):
    
    """Dada uma lista com numeros 
    inteiros diferentes, retorna 
    os numeros pertencentes ao 
    intervalo entre 1 e N. list -> int """

    menor = min(lis)
    maior = max(lis)
    faltando = list()
    for c in range(menor, maior + 1):
        if c not in lis:
            faltando.append(c)
    return faltando