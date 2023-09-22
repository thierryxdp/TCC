def conta_frases(txt):
    frase=str.split(txt,'...')
    frase2=str(frase)
    frase3=str.split(frase2,'.')
    frase4=str(frase3)
    frase5=str.split(frase4,'!')
    frase6=str(frase5)
    frase7=str.split(frase6,'?')
    NF= len(frase7)
    return NF