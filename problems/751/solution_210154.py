def quant_palavras(frase):
    '''Função que dada uma frase, retorna o número de palavras da frase, considerando que a frase pode ter espaços no início e no final; strig -> string'''
    return str.count(str.split(frase))