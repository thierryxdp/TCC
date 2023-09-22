def repetidos(numeros):
    """ Dada uma lista de números, itera por meio dessa lista e
    verifica se o número em questão é igual ao número anterior da lista,
    se for, adiciona +1 ao contador, ao final da iteração, retorna esse contador.
    list -> int
    """
    i = 1
    contador = 0
    tamanhoNumeros = len(numeros)
    while i < tamanhoNumeros:
        if(numeros[i] == numeros[i-1]):
            contador += 1
        i += 1
    return contador