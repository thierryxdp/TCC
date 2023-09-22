def maiores(numeros,n):
    list.append(numeros, n)
    list.sort(numeros)
    x = list.index(numeros, n)
    list.remove(numeros, n)
    return numeros[x:]

def acima_da_media(notas):
    y = sum(notas)/len(notas)
    if int(y) in maiores(notas,y):
        return maiores(notas,y)[1:]
    else:
        return maiores(notas,y)