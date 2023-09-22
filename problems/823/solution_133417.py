def faltante(lista):
    
    """Dada uma lista com numeros 
    inteiros diferentes, retorna 
    os numeros pertencentes ao 
    intervalo entre 1 e N. list -> int """

    menor = min(lista)
    maior = max(lista)
    faltando = list()
    for c in range(menor, maior + 1):
        if c not in lista:
            faltando.append(c)
    return faltando