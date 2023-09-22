def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas_acima=[]
    for k in notas:
        if k>media:
            notas_acima.append(k)
    x=list.sort(notas_acima)
    return x