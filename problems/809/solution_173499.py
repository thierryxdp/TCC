# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas de tam 3, gera uma lista 3 que intercala os elementos das duas primeiras listas"""
    return [*sum(zip(lista1, lista2), ())]