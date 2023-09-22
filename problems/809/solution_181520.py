# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """A função intercala os elementos das listas 1 e 2, o 1º da lista 1, o 1ª da lista 2, o 2ª da lista 1, o 2ª da lista 2....
    assinatura: list --> list"""
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]