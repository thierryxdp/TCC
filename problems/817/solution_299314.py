def acima_da_media(notas):
    acima = []
    med = sum(notas) / len(notas)
    for i in notas:
        if i > med:
            list.append(acima, i)
    list.sort(acima)
    return acima