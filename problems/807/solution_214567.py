def conta_frases(texto):
    """
    Função que recebe um texto e retorna o número de frases nesse texto.
    É considerado que cada frase no texto termina com um ponto final, um ponto de exclamaçãao,
    um ponto de interrogação ou três pontos em sequência (reticências).
    """
    texto = texto.replace('...', '//')
    texto = texto.replace('.', '//')
    texto = texto.replace('!', '//')
    texto = texto.replace('?', '//')
    
    return len(texto.split('//')) - 1