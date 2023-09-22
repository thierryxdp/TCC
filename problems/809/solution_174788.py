# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que ao receber 2 listas de tamanho 3,
    intercala os elementos da lista1 e lista2;
    tuple -> tuple"""
	return lista1[0:1] +lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]