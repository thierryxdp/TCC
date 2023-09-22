def conta_frases(frases):
    import re
    '''Conta quantas palavras tem em uma frase retirando: pontos finais, exclamações,
Interrogações e reticências'''
    lista = re.split(".|!|?|...",frases)
    return len(lista)