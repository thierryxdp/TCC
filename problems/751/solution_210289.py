def quant_palavras(frase):
    '''
    Funçao que dada uma frase, retorna o numero de palavras da frase
    str -> int
    '''
    nova_frase=str.split(frase)
    return len(nova_frase)