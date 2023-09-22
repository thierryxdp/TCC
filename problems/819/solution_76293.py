def filtraMultiplos(lista):
    """Dada uma lista de números e um número 'n'
    retorna outra lista dos multiplos desse mesmo número 'n'."""
    indice = 0
    while lista[1][indice] % lista[2] == 0:
        indice += 1
        return lista[indice]