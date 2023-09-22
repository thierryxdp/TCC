def qtd_divisores(n):
    i=0
    div=0
    while i < n:
        if n%i == 0:
            div += 1
            i += 1
        else:
            i+=1