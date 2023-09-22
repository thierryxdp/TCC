# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funcao que dadas duas listas de tamanho 3, retorna uma lista3 intercalando os elementos de L1 e L2
       list, list -> list"""
    lista3 = list()
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3