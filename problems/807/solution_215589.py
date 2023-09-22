def conta_frases(frase):
    frase1 = str.partition(frase,'.')
    frase2 = str.partition(frase,'...')
    frase3 = str.partition(frase,'!')
    frase4 = str.partition(frase, '?')
    frasef = 0
    if frase1 = True:
        frasef = frasef + 1
    if frase2 = True:
        frasef = frasef + 1
    if frase3 = True:
        frasef = frasef + 1
    if frase4 = True:
        frasef = frasef +1 
    return frasef