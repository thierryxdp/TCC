def quant_palavras(frase):
    '''função em que dada uma frase retorne o número de palvras da frase;
    str -> int'''
    frase1=str.strip(frase)
    return (len(str.split(frase1,' ')))