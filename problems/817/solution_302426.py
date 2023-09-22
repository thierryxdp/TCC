def acima_da_media(notas):
    list.sort(notas)
    acima = []
    for x in notas:
        if x>=5:
            list.append(acima,x)
    return acima