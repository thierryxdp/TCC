# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2 de taamnho 3, essa função retorna uma 
    terceira lista L3 que é formada intercalando elementos da lista 1 e da lista 2.
    list, list -> list"""
    L3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
    return L3