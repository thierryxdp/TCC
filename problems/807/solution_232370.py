def conta_frases(frase):
    """Função que retorna a quantidade de palavras em uma frase; str -> int """
    ponto= frase.replace('!','.')
    ponto2= ponto.replace('?','.')
    ponto3= ponto2.replace('...','.')
    ponto4= ponto3.rstrip('.')
    frases=ponto4.split('.')
    return len(frases)