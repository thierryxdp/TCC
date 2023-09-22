def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.join('', frase[::-1])
    frasef1 = str.split(frasef, ' ')
    frasef2 = str.join('', frasef1[::1])
    return frasef2