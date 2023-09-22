def fatorial(n):
    n = list(range(1,n+1))
    produto = 1
    x=0
    while x < len(n):
        produto = produto*n[x]
        x = x + 1
    return produto