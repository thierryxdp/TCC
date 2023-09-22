def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    virgula = ','
    travessao = '-'
    dois_pontos = ':'
    ponto = '.'
    ponto_e_virgula = ';'
    interrogacao = '?'
    exclamacao = '!'
    
    if virgula in frase:
        return frase.replace(virgula, ' ')
    elif ponto in frase:
        return frase.replace(ponto, ' ')