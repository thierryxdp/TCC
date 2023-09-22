def filtraMultiplos(numeros, n):
    """ Dada uma lista de números e um número n,
    itera por meio da lista de números, achando os números que são múltimos do número n,
    e adicionando a uma lista de números múltiplos.
    list, int -> list
    """
    i = 0
    numerosMultiplos = []
    quantidadeNumeros = len(numeros)
    while i < quantidadeNumeros:
        if(numeros[i] % n == 0):
            numerosMultiplos.append(numeros[i])
        i += 1
    return numerosMultiplos