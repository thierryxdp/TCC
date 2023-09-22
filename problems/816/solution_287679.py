def maiores(numero,n):
    list.sort(numero)
    maiores = []
    for x in numero:
        if x>n:
            list.append(maiores,x)
    return maiores