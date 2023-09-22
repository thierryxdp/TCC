def conta_frases(frase):
    frase1 = str.partition(frase,'.')
    frase2 = str.partition(frase,'...')
    frase3 = str.partition(frase,'!')
    frase4 = str.partition(frase, '?')
    frasef = 0
    if frase1 == True:
        frasef = len(frase1)
    if frase2 == True:
        frasef = len(frase2)
    if frase3 == True:
        frasef = len(frase3)
    if frase4 == True:
        frasef = len(frase4)
    return len(frase1+frase2+frase3+frase4)