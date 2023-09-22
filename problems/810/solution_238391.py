def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.join('', frase[::-1])
    frasefl = str.join('', frasef[::1])
    return frasefl