def filtra_pares(tupla):
    '''Recebe uma tupla (q̶u̶e̶ ̶n̶a̶ ̶v̶e̶r̶d̶a̶d̶e̶ ̶é̶ ̶u̶m̶a̶ ̶l̶i̶s̶t̶a̶) com quatro elementos e retorna uma nova tupla 
    contendo apenas os elementos pares
    tupla -> tupla'''
    pares = []
    for i in tupla:
        if i % 2 == 0:
            pares += [i]
    return tuple(pares)