# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Função que intecala duas listas de tamanho 3, sendo que os elementos da primeira lista
    ocuparão os indices 0,2 e 4 e os elementos da segunda lista ocuparão os indices
    1,3,5.
    list, list --> list
    """
	a,b,c=lista2
    lista1[1::2]=a,b,c
    return lista1