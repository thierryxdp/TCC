# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Função que dadas duas listas
L1 e L2 de tamanho 3,gera uma lista L3 que é
formada intercalando os elementos de L1 e L2.
list,list -> fatiamento'''
    L1 = lista1
    L2 = lista2
    L3 = L1 + L2
    L3[::2] = lista1
    L3[1::2] = lista2
    return L3