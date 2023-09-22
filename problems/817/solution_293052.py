def acima_da_media(lista_de_notas):
    lista_resultado = []
    media = sum(lista_de_notas)/len(lista_de_notas)
    for nota in lista_de_notas:
        if nota > media:
            lista_resultado.append(nota)
    lista_resultado.sort()
    return lista_resultado