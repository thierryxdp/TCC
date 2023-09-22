def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
    l_frases += [frases]
    pontos_finais = []
    virgulas = []
    total = []

    if '.'in frases:
        separa_ponto = frases.index('.')
        add_ponto = frases[0:separa_ponto]
        pontos_finais += [add_ponto]
        total += pontos_finais


    if ',' in frases:
        separa_virgula = frases.rindex(',')
        ponto = frases.index('.')
        add_interrogacao = frases[ponto:separa_virgula]
        virgulas += [add_interrogacao]
        total += virgulas
    return(len(total))