# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Esta função intercala os elementos de duas listas fornecidas pelo usuário"""
    L3 = lista1 [0:1] + lista2 [0:1] + lista1 [1:2] + lista2 [1:2] + lista1 [2:]+ lista2 [2:]
    return L3