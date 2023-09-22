def media(valores):
    return sum(valores)/len(valores)
def acima_da_media(notas):
    v=[]
    for x in notas:
        if x>media(notas):
            v=v+[x,]
    return sort(v)