def quant_palavras(frase):
    '''
    função que dada uma frase retorna o número de palavras da frase, considerando a possibilidade
    de haver espaços na frase
    str--> int
    '''
    return len(frase.split(" "))- len(frase.split("' "))- len(frase.split(" '"))