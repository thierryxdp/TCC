def lingua_p(palavra):
    '''Retorna a palavra na lingua do p.
    str -> str'''
    cont = 0
    lis_palavra = list(palavra)
    acumul = lis_palavra[:]
    ind_corretor = 1
    while cont < len(lis_palavra):
        if str.lower(lis_palavra[cont]) in 'aeiouáéíóúâêîôûàèìòùãõ':
            list.insert(acumul, cont+ind_corretor, 'p' + lis_palavra[cont])
            ind_corretor += 1
        cont = cont+ 1
    return str.join('',acumul)