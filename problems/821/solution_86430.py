def fatorial(n):
    " Fatorial de um numero dado."
     fat = 1
    while n>1:
        fat *= n
        n -= 1
    return fat