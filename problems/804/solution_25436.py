def filtra_pares(tupla)
# função recebe uma tupla e retorna 
# uma nova tupla apenas com os elementos que são pares
# da tupla original.
# tupla --> tupla
    novaTupla = []
    for n in tupla:
        if n%2 == 0:
            novaTupla.append(n)
            
    return tuple(novaTupla)