def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    virgula = ','
    ponto = '.'
    ponto_virgula = '.'
    exclamacao = '!'
    interrogacao = '?'
    dois_pontos = '.'
    travessao = '-'
    
    if virgula in frase:
        return frase.replace(virgula, ' ')
    elif ponto in frase:
        return frase.replace(ponto, ' ')
    elif ponto_virgula in frase:
        return frase.replace(ponto_virgula, ' ')
    elif exclamacao in frase:
        return frase.replace(exclamacao, ' ')