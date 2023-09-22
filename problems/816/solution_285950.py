""" Nesta função eu tentei usar o key do sort, porém não obtive resultados
aí acabei usando esta função y que primeiro pega apenas os números maiores 
que x, e aí sim os ordena em ordem crescente.
list, int -> list
"""
def maiores(lista, x):
    y = [i for i in lista if i > x]
    acao1 = y.sort(reverse=False)
    return y