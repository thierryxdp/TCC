def conta_palavras(frase):
    """
   	Essa funcao retorna o numero de palavras da frase. 
    Parametros de entrada: list
    Valor de saída: int 
    """
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)