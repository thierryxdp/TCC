def repetidos(lista):
    """ essa função irá calcular quantas vezes um elemento da lista é igual ao elemento anterior da mesma
    entrada -> lista
    saida -> int """
    repeticao = 0
    i=0
    while i <len(lista):
        if lista[i] == lista[i-1]:
            repeticao = repeticao + 1
        i = i + 1
    return repeticao