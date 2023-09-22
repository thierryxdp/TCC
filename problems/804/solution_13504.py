def filtra_pares(tupla):
    """funcao que dado de entrada um tupla com 4 elementos
    inteiros, retorna uma nova tupla contendo somente os 
    elementos pares da tupla original;
    tuple -> tuple"""
    E1 = tupla[0]
    E2 = tupla[1]
    E3 = tupla[2]
    E4 = tupla[3]
    lista = (E1, E2, E3, E4)
    tpl = [()]
    for e in lista:
        if e%2 == 0:
            tpl.append(e)
    return tpl