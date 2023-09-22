def conta_frases(frase):
    "Conta o número de frases que aparecem neste texto. Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou reticências. Pontos de exclamação ou de interrogação não aparecerão repetidos em sequência no texto e esses símbolos só aparecem terminando uma frase."
    frase = frase.replace('!','.')
    frase = frase.replace('?','.')
    frase = frase.replace('...','.')
    frase = len(frase)
    return frase