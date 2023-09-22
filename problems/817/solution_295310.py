def maiores(lista,n):
    lista2=[]
    for x in lista:
        if x > n:
            lista2.append(x)
    list.sort(lista2)
    return lista2

def acima_da_media(notas):
    media=sum(notas)/len(notas)
    return maiores(notas,media)