def acima_da_media(notas):
    n_notas = len(notas)
    soma = sum(notas)
    media = soma/n_notas   
    list.sort(notas)
    acima = []
    for x in notas:
        if x>media:
            list.append(acima,x)
    return acima