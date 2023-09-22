def inverte(frase):
    frasef1 = str.split(frase, ' ')
    frasef2 = str.join('', frasef1[::-1])
    frasef4 = str.join('', frasef2[::1])
    return frasef4