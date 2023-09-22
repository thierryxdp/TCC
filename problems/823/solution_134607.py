# A função recebe uma lista com N-1 números inteiros não repetidos numerados de 1 até N e retorna
# o número X que está faltando nesta lista
# list->int
#
def faltante(lista):
    n=1
    while n <= len(lista)+1:
        if not n in lista:
            return n
        n=n+1