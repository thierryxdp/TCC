# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
import math
def intercala(lista1, lista2):
    """Calcula e retorna uma terceira lista com intercalação de 2 outras listas. list, list -> list"""
    import itertools list(itertools.chain(*zip(lista1, lista2)))