# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
     """Função que recebe uma string e retorna o número de palavras da frase desconsiderando os espaços. str -> int"""
   	 	frase = frase.split()
     return len(frase)