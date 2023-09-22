"""Recebe um int e retorna a qnt de divisores que ele tem
int -> int"""


def qtd_divisores(n):
    qnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            qnt = qnt + 1
    return qnt