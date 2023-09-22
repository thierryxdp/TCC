def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas_acima=[]
    for k in range(0,len(notas)+1):
        if k>media:
            notas_acima.append(k)
    return notas_acima