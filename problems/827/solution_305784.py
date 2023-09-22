def qtd_divisores(n):
    div = 0
    for i in list(range(n)):
        if n%i==0:
            div+=1
    return div