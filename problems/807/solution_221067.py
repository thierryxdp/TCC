def conta_frases (texto):
    text=texto
    frase1=text.replace('!','#')
    frase2=text.replace('...','#')
    frase3=text.replace('.','#')
    frase4=text.replace('?','#')
    fraset=text.count('#')
    return fraset