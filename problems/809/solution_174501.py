# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1: list, lista2: list) -> list:
    """Recebe 2 listas de tamanho 3 e retorna uma outra lista de tamanho 6, 
    cujos elementos são formados pelo primeiro elemento da lista1, primeiro
    elemento da lista2, segundo elemento da lista1... e assim sucessivamente."""
    lista_final = lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]
    return lista_final