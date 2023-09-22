"""Recebe um número e retorna seu fatorial
int -> int"""

def fatorial(n):
    i = 1
    fat = 1
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat