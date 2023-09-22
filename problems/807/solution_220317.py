def conta_frases(texto):
    """função que determina a quantidade de frases em um texto
    str -> int"""
    if '...' in texto:
        frases1 = (len(texto.split('.'))-3*(texto.count('...')))-1

    else: 
        frases1 = len(texto.split('.'))-1
    frases2 = len(texto.split('!'))-1
    frases3 = len(texto.split('?'))-1
    frases4 = len(texto.split('...'))-1
    
    qntfrases= frases1 + frases2 +frases3+frases4
    return qntfrases