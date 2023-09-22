def repetidos (lista):
    '''funcao que retorne quantas vezes um elemento e igual ao anterior'''
    nw_list = []
    for i, elemento in enumerate(lista):
        if not elemento in lista[:i]:
            nw_list.append(elemento)
    return nw_list