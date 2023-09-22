def conta_frases(texto:str)->int:
    texto = (((texto.replace('...', '.')).replace('?', '.')).replace('!', '.'))
    return len(texto.split('.'))-1