def acima_da_media(lista):
    med=sum(lista)/len(lista)
    for i in range(len(lista)):
        if lista[i] > med:
            return lista