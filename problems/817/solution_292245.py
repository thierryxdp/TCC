def maiores(lista,n):
    lista.append(n)
    lista.sort()

    return lista[lista.index(n)+1:]

def acima_da_media(notas):
    
    media = sum(notas)/len(notas)
    notasAcima = maiores(notas,media)
    if media in notasAcima:
        notasAcima.remove(media)

    return notasAcima