def freq_palavras(frases):
    listapalavra = frases.split
    frequencia = []
    for pal in listapalavra:
        frequencia.append(listapalavra.count(pal))
    return {str(list(listapalavra + ':' + frequencia))}