def acima_da_media(lista):
    x = sum(lista)/len(lista)
    listi2=[]
    for i in lista:
        if i>x:
            listi2.append(i)
            list.sort(listi2)
    return listi2