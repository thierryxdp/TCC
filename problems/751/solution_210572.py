def quant_palavras(frase):
    """Funçao que contabiliza a quantidade de palavras de uma frase.
    A entrada é uma frase, e a saída é um número inteiro referente a quantidade de palavras"""
    
	ls=str.split(frase," ") 
    return len(ls)