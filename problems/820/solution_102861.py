def posLetra(str_, letra, n):
    '''
    	A função recebe uma string, letra (string cotendo apenas uma letra) e um 
        número n, com isso, ela retorna o índice da nésima ocorrência da letra na 
        string. Caso n exceda o números de ocorrência da letra na string o código
        retornará -1.
        str_ -> str
        letra -> str (contém apenas um intém, uma letra)
        n -> int
        str, str int -> int
    '''
    i = 0
    l_indices = []
    while i < len(str_):
        if str_[i] == letra:
            l_indices += [i]
        i += 1
    if len(l_indices) => n:
        return l_indices[n]
    else:
        return -1