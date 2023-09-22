def quant_palavras(frase):
    """retorna a quantidade de palavras de uma frase, string -> int"""
    quant = (str.split(frase)) #Retorna uma lista com as substrings da string
    return len(quant)          #Retorna a quantidade de strings na lista