def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    contador = 1
    for i in lista:
        if lista[lista.index(i) + 1] == lista[lista.index(i)]:
            contador += 1
    return contador//2