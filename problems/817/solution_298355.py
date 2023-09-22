def acima_da_media(notas):
    media = sum(notas,1)
    y= len(notas)
    z= (media/y)
    x = [z]
    list.extend(notas,x)
    list.sort(notas)
    a= list.index(notas,z)
    b= notas[a+1:]
    return b