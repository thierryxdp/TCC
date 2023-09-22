# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """intercala os elementos de duas listas e um unica lista
    list -> list"""
    intercaladas = []
    for i in range(3):
		intercaladas.append(lista1[i])
		intercaladas.append(lista2[i])
	return intercaladas