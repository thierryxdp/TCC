'''Retorna a quantidade de divisores que um numero n possui'''
#int -> int
def qtd_divisores(n):
    quantidade = 0
    for index in range(1, n + 1):
        if n%index == 0:
            quantidade = quantidade + 1
    return quantidade