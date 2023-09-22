# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dadas duas listas l1 e l2 de tamanho 3, retorna uma lista l3 que é formada intercalando os elementos de l1 e l2"""
    l1 = lista1
    l2 = lista2
    l3 = [l1[0], l2[0], l1[1], l2[1], l1[2], l2[2]]
    return l3