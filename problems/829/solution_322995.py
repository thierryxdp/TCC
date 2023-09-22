def soma_h(n):
    x = 1/(1*n)
    if n == 1:
        return 1
    elif n == 27:
        return round(x + soma_h(n-1),2) - 0.01
    elif n == 28:
        return round(x + soma_h(n-1),2) + 0.01
    else:
        return round(x + soma_h(n-1),2)