#-------EXERCICIO 1-----------

def quant_palavras (frase):
    '''conta quantas palavras tem na frase
       str -> int'''
    
    listPalavras = str.split(frase)
    quantasPalavras = len(listPalavras)
    
    return quantasPalavras