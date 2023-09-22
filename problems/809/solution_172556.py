# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas (lista1 e lista2) de tamanho 3, gera uma lista L3 intercalando seus elemento
    lista, lista -> lista""" 
    L3 = lista1+lista2
    L3 = L3[::3]+L3[1::3]+L3[2::3]
    return L3