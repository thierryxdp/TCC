def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    s = frase
    punct = string.punctuation
    for c in punct:
        return s.replace(c, ' ')