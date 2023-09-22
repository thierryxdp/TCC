def acima_da_media(notas):
	soma = sum(notas)
    media = soma/len(notas)
    lista2 = []
    for x in notas:
        if x>media:
            lista2.append(x)
    lista2.sort()
    return lista2