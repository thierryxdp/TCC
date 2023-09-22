def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    l = []
    for i in lista:
        if not i == l[-1]:
            l.append(i)
    return len(lista)-len(l)