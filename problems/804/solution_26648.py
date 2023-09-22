def filtra_pares(tupla):
    tupla_final =()
    for numero in tupla:
        if numero % 2 == 0:
            tupla_final += (numero)
    return tupla_final