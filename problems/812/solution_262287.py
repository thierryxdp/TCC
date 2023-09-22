def retira_pontuacao (frase):
    '''Retorna a frase dada na entrada, em string, porém
    sem a pontuação
    str --> str'''
    travessao = str.replace(frase, '-', ' ')
    ponto = str.replace(travessao, '.', ' ')
    exclamacao = str.replace(ponto, '!', ' ')
    interrogacao = str.replace(exclamacao, '?', ' ')
    pontovirgula = str.replace(interrogacao, ';', ' ')
    virgula = str.replace(pontovirgula, ',', ' ')
    doispontos = str.replace(virgula, ':', ' ')
    
    return doispontos