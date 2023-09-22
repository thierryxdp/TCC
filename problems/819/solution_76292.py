def filtraMultiplos(lista, numero):
    """Dada uma lista de números e um número 'n'
    retorna outra lista dos multiplos desse mesmo número 'n'."""
    indice = 0
    while lista[indice] % numero == 0:
        indice += 1
        return lista[indice]