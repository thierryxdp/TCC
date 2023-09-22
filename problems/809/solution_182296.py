# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
	'''A função intecala os termos das listas 1 e 2 em ordem análoga às das listas geradoras'''
	lista = []
    A, B, C, = lista1
    D, E, F, = lista2
    lista += (A, D, B, E, C, F,)
    return lista