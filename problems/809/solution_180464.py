# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que junta e intercala as listas 1 e 2. list, list ---> list"""
    L1 = lista1
    L2 = lista2
    L3 = L1 + L2
    L4 = L3
    L3[1] = L4[3]
    L3[3] = L4[4]
    return L3