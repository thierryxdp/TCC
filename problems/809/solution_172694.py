# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(L1, L2):
    '''Dadas duas listas (L1 e L2) de tamanho 3 gera uma lista L3 que
    que é formada intercalando os elementos de L1 e L2.

    list, list -> list'''

    L3 = L1[:1] + L2[:1] + L1[1:2] + L2[1:2] + L1[2:] + L2[2:]

    return L3