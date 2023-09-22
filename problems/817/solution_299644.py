def acima_da_media(notas):
    x=sum(notas)/len(notas)
    list.append(notas,x)
    list.sort(notas)
    list.reverse(notas)
    notas[0:list.index(notas,x)]