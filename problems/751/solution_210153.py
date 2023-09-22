def quant_palavras(frase):
    """ funcao que dada uma string equivalente a uma frase como parâmetro de entrada retorne o número de palavras que dessa frase 
        str --> int """
    
    divide_frase = str.split(frase)
    quantidade_palavras = len(divide_frase)
    
    return quantidade_palavras