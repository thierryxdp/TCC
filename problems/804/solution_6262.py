def filtra_pares(tupla):
    """funcao que recebe uma tupla com quatro elementos, e retorna uma nova  tupla
    contendo apenas elementos pares da tupla original. tupla->tupla"""
    filtragem= ()
    if tupla[0] % 2==0:
        filtragem=filtragem + (tupla[0],)
    if tupla[1] % 2 ==0:
        filtragem=filtragem + (tupla[1],)
    if tupla[2] % 2 ==0:
        filtragem=filtragem + (tupla[2],)
    if tupla[3] % 2 ==0:
        filtragem=filtragem + (tupla[3],)
    return filtragem