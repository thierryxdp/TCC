def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    frasef = str.join('', frase[-1])
    return frasef