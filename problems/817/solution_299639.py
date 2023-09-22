def acima_da_media(notas):
    x=sum(notas)/len(notas)
    list.append(notas,x)
    list.sort(notas)
     return notas[list.index(notas,x)+1:]