def retira_pontuacao (frase):
    '''Funcao que, dada uma frase, retorna a frase onde todos os caracteres de pontuacao sao substituidos por espaco'''
    ''' str -> str'''
    
    for c in ".,:;-!?":
        frase = frase.replace (c, ' ')
    return frase