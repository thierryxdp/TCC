def freq_palavras(frases):
    frase_dividia = str.split(frases)
    palavras_contadas = {}
    for palavra in frase_dividia:
        repete = list.count(frase_dividia, palavra)
        palavras_contadas[palavra] = repete
    return palavras_contadas