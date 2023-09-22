# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
  	#Retorna a quantidade de palavras de uma frase ignorando os possíveis espaços do começo e do fim.
	#string>int
    a=str.split(frase)
    return len(a)