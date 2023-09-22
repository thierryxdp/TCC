def quant_palavras(frase):
    """Funcao que recebe o valor de uma string e retorna a quantidades de palavras nessa string 
        Paramentro:
            Entradas:
                frase: str
                    Valor da string fornecida
            Retorna:
                Um int que representa a quantidade de palavras na string
	"""
    frase2 = frase.strip() #Elimina os espaços no começo e final da string
    palavras = frase2.split() #Divide as palavras da string
    return len(palavras)