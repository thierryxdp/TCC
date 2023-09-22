def quant_palavras(frase):
    ''' Função que recebe uma frase e retorna o número de 
    palavras que há nela
    str -> int '''
    
    Palavras = str.split(frase)
    return len(Palavras)