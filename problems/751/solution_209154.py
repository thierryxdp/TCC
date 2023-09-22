# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	"""Função que retorna a Quantidade de palavras contidas numa frase
    desconsiderando os espaços.
    entr:str
    saida:int"""
	Manipula=(str.replace(frase,' ','#'),)
	vms=(str.split(Manipula[0],"#"))
	conta=(len(vms))

	return conta