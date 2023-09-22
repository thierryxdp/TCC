# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(a1, a2, b1, b2, c1, c2):
    """intercala listas"""
	lista1 = [a1, a2, a3]
    lista2 = [b1, b2, b3]
    
    res = lista1 + lista2
    res[::2] = lista1
    res[1::2] = lisa2