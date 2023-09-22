def quant_palavras(frase):
    '''
    função que recebe uma frase e retorna a quantidade de 
    palavras contidas nela
    '''
    
    frase_separada = str.split(frase)
    
    return len(frase_separada)