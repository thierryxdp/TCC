def maiores(lista,n):
    lista.sort()
    new_list = []
    for x in lista:
        if x > n:
            new_list.append(x)
    return new_list

def acima_da_media(notas):
    n = sum(notas)/len(notas)
    return maiores(notas,n)