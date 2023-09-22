def filtra_pares (lista):
    '''recebe uma tupla com quatro elementos inteiros e retorna apenas
    os pares, na ordem que se encontravam'''
    if lista[0]%2 == 0:
        filtroa = (lista[0],)
    else:
        filtroa = ()
    if lista[1]%2 == 0:
        filtrob = (lista[1],)
    else:
        filtrob = ()
    if lista[2]%2 == 0:
        filtroc = (lista[2],)
    else:
        filtroc = ()
    if lista[3]%2 == 0:
        filtrod = (lista[3],)
    else:
        filtrod = ()
    return filtroa + filtrob + filtroc + filtrod