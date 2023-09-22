def soma_h(n):
    x = 1/(1*n)
    if n == 1:
        return 1
    else:
        return (x + soma_h(n-1)