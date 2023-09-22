def conta_frases(frase):
    """Retorna a quantidade de frases em um determinado texto.Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência (reticências). Pontos de exclamação ou de interrogação não aparecerão repetidos em sequência no texto e esses símbolos só aparecem no texto terminando uma frase.
    str-->int"""
    return frase.count("!")+frase.count(".")+frase.count("...")+frase.count("?")-3*frase.count("...")