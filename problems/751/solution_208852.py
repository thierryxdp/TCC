def quant_palavras(frase):
    '''tem como entrada uma frase no formato string que 
    retorna a contagem dos caracteres dessa entrada.
    str -> int'''
	
    ret = sum(str.split(frase))
    
    return ret