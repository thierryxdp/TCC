def acima_da_media(notas):
    media=sum(notas)/len(notas)
    list.sort(notas)
    for n in notas:
        if n>media:
            return notas[list.index(nitas,n):]