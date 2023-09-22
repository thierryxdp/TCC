def conta_frase(frase):
   '''conta a quantidade de frases seguidas por ponto (.,!,?,...).
   str -> int'''
     if '...' in frase:
        f = f + str.count(frase,"...")
    if '!' in frase:
        f = f + str.count(frase,"!")
    if '?' in frase:
        f = f + str.count(frase,"?")
    if '.' in frase:
        f = f + str.count(frase,".") - str.count(frase,'...')
    return f