def conta_frases(frase):
    'Função que retorna o número de palavras da frase. str --> int'
    frase=str.strip(frase)
    frase=str.split(frase)
    return len(frase)