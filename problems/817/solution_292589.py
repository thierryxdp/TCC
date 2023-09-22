def acima_da_media (lista_notas: list) ->list:
    """Retorna todas as notas acima da média - calculada a partir das notas
    em lista_notas - em lista_notas."""
    media = sum(lista_notas)/len(lista_notas)
    list.append(lista_notas, media)
    list.sort(lista_notas)
    contador = list.count(lista_notas, media)
    indice = list.index(lista_notas, media) + contador
    lista_final = lista_notas[indice:]
    return lista_final