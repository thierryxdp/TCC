def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.join('', frase[::-1])
    frasef = str.split(frasef, ' ')
    return frasef