def fatorial(numero):
    i = 0
    fat = 1
    n = numero
    while i < numero:
        fat = fat * n
        n = n - 1
        i = i + 1
    return fat