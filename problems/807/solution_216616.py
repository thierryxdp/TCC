def conta_frases(frase):
    '''conta a quantidade de frases seguidas por ponto (.,!,?,...).
   str -> int'''
    f = 0
    if '!' in frase:
        f = f + str.count(frase,"!")
    if '?' in frase:
        f = f + str.count(frase,"?")
    if '...' in frase:
        f = f + str.count(frase,str.replace(frase,"...","."))    
    if '.' in frase:
        f = f +  str.count(frase,str.replace(frase,"...",".")) 
    return f