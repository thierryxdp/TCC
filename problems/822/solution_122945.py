def repetidos(lista):
    '''Funcao que retorna o numero de vezes que um elemento e igual ao elemento anterior'''
    nova_lista = []
    i = 0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            nova_lista.append(1)
        i = i + 1
    return len(nova_lista)