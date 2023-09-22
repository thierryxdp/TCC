def faltante(lista_num):
    """Função que dada uma lista com N - 1 contendo números inteiros, não repetidos, retorna o número
    inteiro x que pertence ao intervalo de [1,N], não pertencente a lista de entrada; list -> int"""

    num = len(lista_num) + 1
    num_soma = num*(num + 1) // 2
    num_faltante = num_soma - sum(lista_num)

    return num_faltante