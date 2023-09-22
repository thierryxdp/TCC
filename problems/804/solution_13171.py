def filtra_pares(tupla):
    for n in tupla:
        if n % 2 == 0:
            return tupla - (n % 2 != 0)