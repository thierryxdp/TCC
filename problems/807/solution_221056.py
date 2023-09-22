def conta_frases (texto):
    frase1=texto.split('!')
    frase2=texto.split('...')
    frase3=texto.split('.')
    frase4=texto.split('?')
    fraset= frase1, frase2, frase3, frase4
    return texto.count (fraset)