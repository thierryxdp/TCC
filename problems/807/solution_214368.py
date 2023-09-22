def conta_frases(texto):
    texto.replace('...','#').replace('?','#').replace('!','#').replace('.','#')
    return str.count(texto,"#")