def conta_frases (texto):
    text=texto
    text=text.replace('!','#')
    text=text.replace('...','#')
    text=text.replace('.','#')
    text=text.replace('?','#')
    fraset=text.count('#')
    return fraset