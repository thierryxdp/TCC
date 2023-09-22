def conta_frases(frase):
    frase1 = str.partition(frase,'.')
    frase2 = str.partition(frase,'...')
    frase3 = str.partition(frase,'!')
    frase4 = str.partition(frase, '?')
    frasef = 0
    if frase1 == 0:
        frasef = frasef + 1
    if frase2 == 0:
        frasef = frasef + 1
    if frase3 ==0 :
        frasef = frasef + 1
    if frase4 == 0:
        frasef = frasef +1 
    return frasef