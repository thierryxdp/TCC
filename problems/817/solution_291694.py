def acima_da_media(lista):
    maiores=[]
    for i in range(len(lista)):
        media+=lista[i]
    for i in range(len(lista)):
        if lista[i]>media:
            maiores.append(lista[i])
        else:
            continue
    maiores.sort()
    return maiores