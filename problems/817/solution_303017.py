def acima_da_media(lista):
    list.sort(lista)
    m=[]
    for numero in lista:
        if numero>=sum(lista)/len(lista):
            list.append(m,numero)
    return m