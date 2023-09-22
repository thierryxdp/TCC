def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    string.punctuation = [',', '.', '-']
    
    import string
    for c in string.punctuation:
        return frase.replace(c, ' ')