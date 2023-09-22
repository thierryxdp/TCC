def retira_pontuacao (frase):
    '''Função substitui todas as pontuações por espaço.
    str -> str'''
    pontofinal = str.replace (frase, '.', ' ')
    exclamacao = str.replace (pontofinal, '!', ' ')
    interrogacao = str.replace (exclamacao, '?', ' ')
    travessao = str.replace (interrogacao, '-', ' ')
    virgula = str.replace (travessao, ',',' ')
    doispontos = str.replace (virgula, ':', ' ')
    pontovirgula = str.replace (doispontos, ';', ' ')
    return pontovirgula