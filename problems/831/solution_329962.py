def lingua_p(palavra):
    '''
        recebe uma palavra da lingua portuguesa e traduz para a lingua do "P"
        entrada: string
        saida: string
    '''
    palavraP = ''
    palavra_min = str.lower(palavra)
    for chq in range(len(palavra)):
        if palavra_min[chq] in 'aeiouâêôáéíóúãõ':
            palavraP = palavraP + palavra_min[chq] + 'p' + palavra_min[chq]
        else:
            palavraP = palavraP + palavra_min[chq]
    return palavraP