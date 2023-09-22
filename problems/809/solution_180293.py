# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que  ́e formada
intercalando os elementos de L1 e L2; list,list -> list"""
    l1= lista1
    l2= lista2
    l3=zip(l1,l2)
    return l3