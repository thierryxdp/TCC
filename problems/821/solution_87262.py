def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return ("O valor de %d! eh =" %n, fat)