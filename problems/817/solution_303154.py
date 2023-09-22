def acima_da_media(notas):
    media=sum(notas)/len(notas)
    aprovados=[]
    for x in notas:
        if x > media:
            aprovados.append(x)
    list.sort(aprovados)        
    return aprovados