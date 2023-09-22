def filtra_pares( tupla ):
    '''retorna apenas os pares da tupla
    tuple -> tuple'''
    a,b,c,d = tuplade4elementosinteiros
   lista = []

    for n in tupla:
        if n % 2 == 0:
            lista.append(n)

    return lista