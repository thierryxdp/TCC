def lingua_p(palavra):
    """ """
    saida = ''
    cont = 0
    for i in palavra:
        saida[cont]=i
        if i == 'aeiouAEIOU':
            saida[cont+1] = 'p'
            saida[cont+2] = i
    return saida