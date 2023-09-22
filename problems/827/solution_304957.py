def qtd_divisores(n):
    i = 1
    cont = 0
    for i in (n):
        if n%i == 0:
            cont = cont + 1
            i = i + 1
            return cont