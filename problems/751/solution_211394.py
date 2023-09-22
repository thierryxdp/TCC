def quant_palavras(frase):
    """Função que recebe uma frase como argumento e retorna o número de palavras 
    existente na frase"""
   
	n = str.split(frase, " ")
    tamanho = len(n)
    return tamanho