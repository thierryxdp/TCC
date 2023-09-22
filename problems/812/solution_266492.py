def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    import string
    s = frase
    for c in string.punctuation:
        return s.replace(c, ' ')