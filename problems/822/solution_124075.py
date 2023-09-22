def repetidos(lista):
    " " "Recebe como entrada uma lista e retorna o numero de vezes que um elemento da lista é igaul ao elemento anterior;list, -> int, " " "
    i = 0
    n = 0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            n = n + 1
        i = i + 1
    return n