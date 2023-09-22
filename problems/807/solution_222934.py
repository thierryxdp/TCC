conta_frases(texto):
    '''Ao receber um texto, retorna a quantidade de frases
    str -> int'''
    #substituindo todas as pontuações por '.':
    exclamacao_ponto = str.replace(texto,'!','.')
    interrogacao_ponto = str.replace(exclamacao_ponto,'?','.')
    reticencias_ponto = str.replace(interrogacao_ponto,'...','.')
    #cada frase tem uma pontuação
    frases = str.count(reticencias_ponto,'.')
    return frases