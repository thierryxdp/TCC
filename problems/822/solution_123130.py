def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    posicao = 0
    for i in lista:
        if i not in l:
            l.append(i)
    return len(lista)-len(l)