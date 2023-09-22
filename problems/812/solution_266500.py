def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    pontuacao = [',', '.', '-']
    
    import string
    for i in pontuacao:
        return frase.replace(c, ' ')