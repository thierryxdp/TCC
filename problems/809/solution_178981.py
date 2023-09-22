# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Esta e a funcao que dadas duas listas l1 e l2 de 
    tamanho 3, gera uma lista l3 que é formada intercalando
    os elementos de l1 e l2.
    list, list -> list"""
	return lista1[0:-:2]+lista2[0::2]+lista1[1::2]+lista2[1::2]