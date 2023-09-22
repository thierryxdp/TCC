def conta_frases(texto):
    x = texto.replace('...','#').replace('?','#').replace('!','#').replace('.','#')
    return str.count(x,"#")