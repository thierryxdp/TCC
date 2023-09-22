"""Recebe um int e retorna se ele é um número primo
int -> boolean"""


def primo(n):
    qnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            qnt = qnt + 1
    return qnt == 2