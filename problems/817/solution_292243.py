def maiores(lista,n):
    lista.append(n)
    lista.sort()

    return lista[lista.index(n)+1:]

def acima_da_media(notas):
    
    media = sum(notas)/len(notas)

    return maiores(notas,media)