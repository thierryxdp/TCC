# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dado duas listas retorna outra intercalando ambas: list, list->list"""
    L3=L1[0:1]+L2[0:1]+L1[1:2]+L2[1:2]+L1[-1:-2]+L2[-1:-2]
    return L3