def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    punct = frase.punctuation
    for c in punct:
        frase = frase.replace(c, ' ')