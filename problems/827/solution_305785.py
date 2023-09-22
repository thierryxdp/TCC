def qtd_divisores(n):
    div = 0
    lista = list(range(n))
    for i in lista:
        if n%i==0:
            div+=1
    return div