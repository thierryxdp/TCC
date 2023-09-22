def filtraMultiplos(lista,n):
    """A funcao filtra multiplos de um um numero n e uma lista de numeros dada.
    O retorno sera uma lista de numeros multiplos de n. list,float-->list."""
    contagem = 0
    multiplos = []
    while contagem < len(lista):
        if lista[contagem] % n == 0:
            multiplos = multiplos + [lista[contagem]]
        contagem = contagem + 1
    return multiplos