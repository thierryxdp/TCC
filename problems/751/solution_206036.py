# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que recebe o valore de uma string e retorna a quantidades de palavras nessa string 
        Paramentro:
            Entradas:
                frase: str
                    Valor da string fornecida
            Retorna:
                Um int que representa a quantidade de palavras na string"""
	frase_sem_espaços = frase.strip() 
	palavras = frase_sem_espaços.split() 
    return len(palavras)