def filtra_pares(tupla4elementos):
    ''' essa funcao recebe uma tupla com 4 elementos e retona outra
    com apenas os elementos pares '''
    elem1 = (int(tupla4elementos[0]),)
    elem2 = (int(tupla4elementos[1]),)
    elem3 = (int(tupla4elementos[2]),)
    elem4 = (int(tupla4elementos[3]),)
    tupla_pares = ()
    
    if elem1[0]%2 == 0:
        tupla_pares = tupla_pares + elem1
    if elem2[0]%2 == 0:
        tupla_pares = tupla_pares + elem2
    if elem3[0]%2 == 0:
        tupla_pares = tupla_pares + elem3
    if elem4[0]%2 == 0:
        tupla_pares = tupla_pares + elem4
    return tupla_pares