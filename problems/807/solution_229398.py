def conta_frases(texto):
    "dado um texto, retorna o numero de palavras dela str -> str"
    for i in range len(texto)-1:
        if texto[i]==texto[i+1]=='.':
            n1 = len(texto.split('.')) - 3
        else:
            n1 = len(texto.split('.')) - 1
    n2 = len(texto.split('!'))-1
    n3 = len(texto.split('?'))-1
    n4 = len(texto.split('...'))-1
    return n1+n2+n3+n4