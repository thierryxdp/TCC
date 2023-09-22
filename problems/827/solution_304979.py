def qtd_divisores(n):
    i = 0
    cont = 0
    for i in (1,n):
        if n%i == 0:
            i += 1
        	cont += 1
    else:
    return cont