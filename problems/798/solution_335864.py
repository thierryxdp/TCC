def freq_palavras(frases):
    """Retorna a palavra e sua quantidade de aparicoes;
    	str -> dict"""
    freq = {}
    frases = frases.split()
    for palavra in frases:
        freq[palavra]=frases.count(palavra)
    return freq