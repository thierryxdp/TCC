def qtd_divisores(n):
    i = 0
    cont = 0
    for i in (1,n):
        if n%i == 0:
        cont == cont + 1
        i = i + 1
        return cont