def filtra_pares(tupla1):
    tupla2 = sorted(filter(lambda x: x % 2 == 0, tupla1))
    tupla3 = str(tupla2)
    tupla4 = str(tupla3.replace("[",")"))
    return tupla4.replace("]",")")