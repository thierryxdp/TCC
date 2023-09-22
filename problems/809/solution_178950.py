# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas lista1 e lista2 ambas de tamanho 3, retorna uma 
    lista que intercala os elementos da lista1 e lista2
    list,list -> list"""
    l1 = lista1
    l2 = lista2
    lista3 = [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]
    return lista3