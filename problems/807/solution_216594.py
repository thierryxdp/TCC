def conta_frases(frase):
    '''conta a quantidade de frases seguidas por ponto (.,!,?,...).
   str -> int'''
    f = 0
    if '...' in frase:
        f = f + str.count(frase,"...")
    if '!' in frase:
        f = f + str.count(frase,"!")
    if '?' in frase:
        f = f + str.count(frase,"?")
    if '.' in frase:
        f = f + str.count(frase,".")
    in '.' in frase and '...' in frase:
        f = f + str.count(frase,"...")*3 - str.count(frase,".")
    return f