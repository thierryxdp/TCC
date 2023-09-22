def fatorial(n):
    "calcula o faotrial do numero n. int->complex"
    fat= n
    while n>1:
        fat=fat*(n-1)
        n-=1
    return fat