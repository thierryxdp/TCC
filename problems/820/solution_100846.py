def posLetra(s,l,n):
    '''recebe,respectivamente, uma string,uma letra e um numero, e retorna 
    a posicao da ocorrencia da letra dada.
    str, str, int --> int'''
    lista_string = list(s)
    lista_letras = []
    i = 0
    while i < len(lista_string):
        if lista_string[i] == l:
            list.append(lista_letras, i)
        i = i + 1
    index = n - 1
    if index >= len(lista_letras):
        return -1
    else:
        return lista_letras[index]