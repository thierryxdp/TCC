def acima_da_media(lista_notas):
    media = (sum(lista_notas))/(len(lista_notas))
    lista_maiores = []
    for nota in lista_notas:
        if nota > media: lista_maiores.append(nota)
    lista_maiores.sort()
    return lista_maiores