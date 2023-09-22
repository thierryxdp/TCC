def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    l = []
    for i in lista:
        if lista[lista.index(i)+1] == lista[lista.index(i)]:
            l.append(i)
    return len(l)