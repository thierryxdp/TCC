# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna uma lista3(L3) dados lista 1 e lista 2, respectivamente, intercalando os elementos das duas. lista, lista --> lista"""
    L3 = [0, 0, 0, 0, 0, 0]
    L3[0] = lista1[0]
    L3[1] = lista2[0]
    L3[2] = lista1[1]
    L3[3] = lista2[1]
    L3[4] = lista1[2]
    L3[5] = lista2[2]
    return L3