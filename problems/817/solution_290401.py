def acima_da_media(notas):
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    index=list.index(notas,media)
    return notas[index+1:]