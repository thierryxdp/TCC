def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    posicao = 0
    contador = 0
    while len(lista) >= contador:
        if lista[posicao + 1] == lista[posicao]:
            contador += 1
    return contador