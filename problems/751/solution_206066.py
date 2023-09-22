def contagem (frase):
    ''' Faça uma funcao que dada uma frase, retorne o numero de palavras da frase. 
    Considere que a frase pode ter espacos no inicio e no final.'''
    #str > str
    frase = str.split(frase)
    return len(frase)