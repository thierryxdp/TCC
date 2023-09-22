def conta_frases(frase):
    """retorna o numero de palavras da frase"""
    pontos = ('.','!','?','...')       
    nfrases = str.split(frase,(pontos))
    return len(nfrases)