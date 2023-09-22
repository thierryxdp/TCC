# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    	A função recebe duas listas de tamanho 3 e intercala seus
        elementos.
        lista1 -> lista de tamanho 3
        lista2 -> lista de tamanho 3
        list, list -> list
    """
    l1=lista1
    l2=lista2
    l3=l1[0]+l2[0]+l1[1]+l2[1]+l1[2]+l2[2]
    return l3