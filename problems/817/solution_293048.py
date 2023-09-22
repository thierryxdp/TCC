def acima_da_media(lista_de_notas):
    lista_resultado = []
    for notas in lista_de_notas:
        if nota > 7:
            lista_resultado.append(nota)
    lista_resultado.sort()
    return lista_resultado