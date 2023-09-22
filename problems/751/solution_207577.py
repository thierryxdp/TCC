# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def contador_palavras(texto: str):

	lista = texto.split(" ")

	novo_texto = "".join(lista)
	
	return novo_texto
	



string = contador_palavras('Porra que isso mano')
print(len(string))