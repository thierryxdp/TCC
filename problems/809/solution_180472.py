# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que junta e intercala as listas 1 e 2. list, list ---> list"""
    L1=lista1
    L2=lista2
    L3= lista1 + lista2
    L3[1] = lista2[0]
    L3[2] = lista1[1]
    L3[3] = lista2[1]
    L3[4] = lista1[2]
    L3[5] = lista2[2]
    return L3