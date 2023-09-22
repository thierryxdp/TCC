# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(a1, a2, b1, b2, c1, c2):
    """intercala listas"""
	lista1 = [a1, a2, a3]
    lista2 = [b1, b2, b3]
    intercala = lista1 + lista2
    intercala[::2] = lista1
    intercala[1::2] = lista2
    print (intercala)