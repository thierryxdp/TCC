# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """intercala listas"""
    from itertools import chain
    list(chain.from_iterable(zip(lista1, lista2)))