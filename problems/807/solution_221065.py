def conta_frases (texto):
    frase1=texto.replace('!','#')
    frase2=texto.replace('...','#')
    frase3=texto.replace('.','#')
    frase4=texto.replace('?','#')
    fraset=texto.count('#')
    return fraset