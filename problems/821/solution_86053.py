"""Recebe um número e retorna seu fatorial
int -> int"""

def fatorial(n):
    i = 0
    while i < n:
        n = n*i
        i = i + 1
    return fat