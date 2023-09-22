def quant_palavras(frase):
    
    '''Função que dada uma frase, retorna o número
    de palavras da mesma, sem contar os espaços.
    
    :param frase: str
    :return: int'''
   
    tamanho=str.split(str(frase),' ')
    
    return len(tamanho)