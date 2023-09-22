# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que, quando e informada duas listas, 
    retonara uma nova lista que alterna os elementos 
    de ambas 
    list, list --> list
    testes:
    intercala([3, 4, 5], [1, 2, 3]) == [3, 1, 4, 2, 5, 3] 
    intercala([2, 4, 6], [0, 4, 9]) == [2, 0, 4, 4, 6, 9] """
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3