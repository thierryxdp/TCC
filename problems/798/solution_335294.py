def freq_palavras(frase):
    '''Retorna um dicionário em que cada chave corresponde
       a cada palavra da frase de entrada e cada valor 
       equivale ao núemro de vezes que suas respectivas 
       palavras nela aparecem;
       str -> dict'''
    lPalavras=frase.split(' ')
    dictRetorno={}
    for el in lPalavras:
        dictRetorno[el]=lPalavras.count(el)
    return dictRetorno