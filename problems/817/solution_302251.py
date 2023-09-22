def media(valores):
    return sum(valores)/len(valores)
def acima_da_media(notas):
    v=[]
    list.sort(notas)
    for x in notas:
        if x>media(notas):
            v=v+[x,]
    return v