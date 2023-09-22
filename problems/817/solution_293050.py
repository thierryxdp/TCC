def acima_da_media(lista_de_notas):
    lista_resultado = []
    for nota in lista_de_notas:
        if nota > 5:
            lista_resultado.append(nota)
    lista_resultado.sort()
    return lista_resultado