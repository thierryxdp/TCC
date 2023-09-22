def repetidos (ln):
    '''
    funcao que dada uma lista de numeros retorna o numero de vezes que um elemeno da lista e igual ao elemento anterior.
    list->int.
    '''
    i=0
    s =0
    while i < len(ln)-1:
        if ln[i] == ln[i+1]:
            s = s +1
        i = i+1
    return s