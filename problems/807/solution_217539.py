def conta_frase(texto):
    if '.' and'...'and'!'and'?' in texto:
        texto= texto.split(' ')
        texto2=len(texto)
        return texto2