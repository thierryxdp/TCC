def acima_da_media(notas):
    """ Funcao que recebe uma lista com notas.
     	Retorna uma lista ordenada com as notas que ficaram acima da média;
        list -> list
    """
    media = sum(notas) / len(notas)
    notas_acima_da_media = []
    for nota in notas:
        if nota > media:
            notas_acima_da_media.append(nota)
            
    notas_acima_da_media.sort()
    return notas_acima_da_media