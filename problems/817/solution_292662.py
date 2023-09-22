def acima_da_media(lista):
	media = sum(lista)/len(lista)
    x=[]
    for y in lista:
        if y > media:
            x.append(y)
    x.sort()
    return x