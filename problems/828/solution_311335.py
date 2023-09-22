"""Recebe um int e retorna se ele é um número primo
int -> boolean"""


def primo(n):
    for i in range(1, n+1):
        if n%i == 0:
            return False
        else:
            return True