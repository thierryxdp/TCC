def conta_frases(frase):
    var1 = str.split(frase,'...')
    var2 = str.split((str.strip(frase,'...'),'!')
    return len(var1)+len(var2)