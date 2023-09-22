# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que junta e intercala as listas 1 e 2. list, list ---> list"""
    L1 = lista1
    L2 = lista2
    return [L1[0] + L2[0] + L1[1] + L2[1] + L1[2] + L2[2]]