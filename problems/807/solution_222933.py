def conta_frases(texto):
    """Função que recebe um texto e retorna o número de frases
    que sse texto contém. Cada frase é terminada com ponto final, 
    exclamação, interrogação ou reticências. Os pontos de interrogação
    e exclamação não aparecem repetidos em seqência e aparecem apenas no fim
    de uma frase.
    str->int
    """
    #Substituindo por "."
    texto = str.replace(texto, "...", ".")
    texto = str.replace(texto, "?", ".")
    texto = str.replace(texto, "!", ".")
    #Contar os pontos
    return str.count(texto, ".")