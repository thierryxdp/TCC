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
    
    return ''.join([i for i in frase if i not in frase.punctuation])