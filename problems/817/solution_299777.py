def acima_da_media(
    notas: list[float]
        ) -> list[float]:
    '''Retorna as notas que estão acima da média'''

    # Calcular a média das notas
    media = sum(notas)/len(notas)

    # Recolhendo as notas estritamente maiores que a media
    acimaDaMedia = maiores(notas, media)

    return acimaDaMedia  # , media