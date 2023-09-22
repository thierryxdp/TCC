def acima_da_media(notas):
    y = sum(notas)/len(notas)
    if int(y) in maiores(notas,y):
        return maiores(notas,y)[1:]
    else:
        return maiores(notas,y)