# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna a lista 3 que é a intercalação entre a lista 1 e 2:
    int, int-> int"""
	return lista1[0:1]+lista2[0:1] + lista1[1:2]+lista2[1:2]+ lista1[2:3]+lista2[2:3]