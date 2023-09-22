def conta_frases(frase):
    frase1 = str.split(frase,'.')
    frase2 = str.split(frase,'...')
    frase3 = str.split(frase,'!')
    frase4 = str.split(frase, '?')
    frasef = ()
    if frase1 == True:
        frasef = frasef + 1
    if frase2 == True:
        frasef = frasef + 1
    if frase3 == True :
        frasef = frasef + 1
    if frase4 == True:
        frasef = frasef +1
    return len(frasef)