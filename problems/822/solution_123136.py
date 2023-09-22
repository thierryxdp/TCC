def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    l = []
    descarte = []
    for i in lista:
        if lista[lista.index(i)] == lista[lista.index(i)-1]:
            descarte.append(i)
        else:
            l.append(i)
    return len(lista) - len(l)