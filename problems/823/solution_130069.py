def faltante(lista):
    """dada uma lista com N − 1 inteiros numerados de 1 a N, função retorna
qual numero inteiro deste intervalo esta faltando. lista -> int """
    elemento = []
    i = 0
    lista.sort()
    while i < len(lista) - 1:
        if lista[0] != 1:
            elemento.append(1)
            return elemento
        if lista[i + 1] != lista[i] + 1 :
            elemento.append(lista[i] + 1)
        i = i + 1 
    return elemento