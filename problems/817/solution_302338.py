def acima_da_media(lista):
    med=sum(lista)/len(lista)
    r = []
    for i in range(len(lista)):
        if lista[i] > med:
            r.append(lista[i])
            r.sort()
            return r