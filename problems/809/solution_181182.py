# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas, e retorna uma terceira lista com os elementos das duas primeiras listas intercalados.
    casos de teste:
    ([1,2,3],[4,5,6]) == ([1,4,2,5,3,6])
    ([7,2,5],[8,9,1]) == ([7,8,2,9,5,1])
    ([0,8,3],[9,2,7]) == ([0,9,8,2,3,7])
    assinatura: list, list -> list"""
    intercala = lista1 + lista2
    intercala[::2] = lista1
    intercala[1::2] = lista2
    return intercala