def conta_frases(frase):
    if '.' in frase:
    b = str.partition(frase,'.')    
    a = list.count(frase, '.')
    str.replace(frase,'.','',a)
    return frase