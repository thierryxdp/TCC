def filtra_pares (tupla):
    filtra_pares = (n for n in tupla if n %2 ==0)
    return [n for n in tupla if n %2 ==0]