# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """intercala listas"""
	lista1 = [1, 3, 5]
    lista2 = [2, 4, 6]
    intercala = lista1 + lista2
    intercala[::2] = lista1
    intercala[1::2] = lista2
    print (intercala)