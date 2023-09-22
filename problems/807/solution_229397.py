def conta_frases(texto):
    "dado um texto, retorna o numero de palavras dela str -> str"
    n1 = len(texto.split('.'))-1
    n2 = len(texto.split('!'))-1
    n3 = len(texto.split('?'))-1
    n4 = len(texto.split('...'))-1
    return n1+n2+n3+n4