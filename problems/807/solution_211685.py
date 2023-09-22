def conta_frases(texto):
    """Pede um texto com algumas frases e retorna
    o número de frases passadas, separadas por ponto final, reticências,
    exclamação ou interrogação.
    string->int"""
    #Substitui toda a pontuação do texto passado para pontos finais#
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'?','.')
    texto=str.replace(texto,'!','.')
    #Separa a string resultante em substrings de acordo com a posição dos pontos finais#
    contagem=str.split(texto,'.')
    return len(contagem)-1