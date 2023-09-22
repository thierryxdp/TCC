def faltante(lista):
    '''Função que recebe uma lista de inteiros consecutivos de
    1 a N e tamnaho N - 1 e retorne o inteiro faltando; list -> int'''
    parada = 1
    soma = 0
    while parada != lista[-1] + 1:
        soma += parada
        parada += 1
    if soma == sum(lista):
        return lista[-1] + 1
    else:
        return soma - sum(lista)