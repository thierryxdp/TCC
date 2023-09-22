def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    pontuacao = {',', '-', ':', ';', '!', '?', '.'}
    
    return ''.join(c for c in frase if c not in pontuacao)