def lingua_p(palavra):
    """ """
    saida = ''
    for i in palavra:
        saida.append(i)
        if i == 'aeiouAEIOU':
            saida.append('p')
            saida.append(i)
    return saida