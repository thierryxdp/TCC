# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(a1, a2, b1, b2, c1, c2):
    """intercala listas"""
	lista1 = [a1, b1, c1]
    lista2 = [a2, b2, c2]
    
    res = lista1 + lista2
    res[::2] = lista1
    res[1::2] = lisa2