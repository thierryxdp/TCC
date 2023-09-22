def quant_palavras(frase):
    """Funcao que recebe o valore de uma string e retorna a quantidades de palavras nessa string 
        Paramentro:
            Entradas:
                frase: str
                    Valor da string fornecida
            Retorna:
                Um int que representa a quantidade de palavras na string
	"""
    frase_sem_espaços = frase.strip() #Elimina os espaços no começo e final da string
    palavras = frase_sem_espaços.split() #Divide as palavras da string
    return len(palavras)