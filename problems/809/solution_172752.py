# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dadas duas listas 'lista1' e 'lista2', ambas com 3 elementos cada, retorna uma nova lista que 
    intercala os elementos das duas. Exemplo: lista1 = [1,3,5] e lista2 = [2,4,6] retornarão uma lista [1,2,3,4,5,6].
    list, list -> list"""
    return lista1[0]+lista2[0]+lista1[1]+lista2[1]+lista1[2]+lista2[2]