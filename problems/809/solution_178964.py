# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que, dadas 2 listas (L1 E L2), retorna uma terceira lista (L3)
    que intercala os elementos de L1 E L2. list, list -> list"""
    lista3 = lista1+lista2
    lista3 = lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2: ]+lista2[2: ]
    return lista3