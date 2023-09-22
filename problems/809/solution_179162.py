# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas lias l1 e l2 de tamanho 3, retorna uma lista l3 intercalando os elementos de l1 e l2"""
l3=lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]+lista1[3:]+lista2[3:]
	return l3