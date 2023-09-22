# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Esta e a funcao que dadas duas listas l1 e l2
    de tamanho 3, geram uma lista l3 que é formada 
    intercalando elementos de l1 e l2'''
    i=len(lista1)
	j=len(lista2)
	return lista1[0:i+1:1]+lista2[0:j+1:1]