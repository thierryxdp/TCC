def acima_da_media(notas):
    n_notas = list.count(notas)
    soma = sum(notas)
    media = soma/n_notas   
    list.sort(notas)
    acima = []
    for x in notas:
        if x>media:
            list.append(acima,x)
    return acima