def maiores(lista, numero):
    """Funcao que dada uma lista de numeros inteiros e um numero inteiro retorna outra lista
    que contem todos os valores da lista original maiores que o numero inteiro inserido."""
    filtrados = [x for x in lista if x > numero]
    return filtrados