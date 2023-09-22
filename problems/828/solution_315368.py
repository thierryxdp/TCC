def qtd_divisores(n):
    lista = range(1,n+1)
    divisores = []
    for x in lista:
        if n%x == 0:
            list.append(divisores,x)
    if len(divisores)>2:
        return False
    if n%1 == 0 and n%n == 0:
        return True