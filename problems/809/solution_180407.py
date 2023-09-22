# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dadas duas listas de tamanho 3 retorna uma terceira lista
    formada pelos elementos de lista1 e lista2 intercalados.
    assinatura: list, list --> list
    testes:
    intercala([1,3,5], [2,4,6]) == [1, 2, 3, 4, 5, 6]
    intercala([0,2,4], [1,3,5]) == [0, 1, 2, 3, 4, 5]
    intercala([3,5,7], [4,6,8]) == [3, 4, 5, 6, 7, 8]
    """
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3]