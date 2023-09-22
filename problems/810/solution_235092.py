def retira_pontuacao (frase):
    '''Função substitui todas as pontuações por espaço.
    str -> str'''
    pontoFinal = str.replace (frase, '.', ' ')
    exclamacao = str.replace (pontoFinal, '!', ' ')
    interrogacao = str.replace (exclamacao, '?', ' ')
    travessao = str.replace (interrogacao, '-', ' ')
    virgula = str.replace (travessao, ',', ' ')
    doisPontos = str.replace (virgula, ':', ' ')
    pontoVirgula = str.replace (doisPontos, ';', ' ')
    return pontoVirgula
def inverte (frase):
    '''Função inverte a ordem das palavras da frase (de tras pra frente), sem letras maisculas e sem pontuação.
    str -> str'''
    fraseMinuscula = str.lower(frase)
    fraseNova = retira_pontuacao (fraseMinuscula)
    listaPalavra = str.split (fraseNova)
    invertida = listaPalavra [::-1]
    return str.join (' ', invertida)